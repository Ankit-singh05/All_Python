import queue
import threading
import time
import speech_recognition as sr
import pyttsx3
from groq import Groq

# -----------------------
# 1. SPEECH SETUP
# -----------------------
recognizer = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("🎤 Listening...")
        # calibrate once quickly
        recognizer.adjust_for_ambient_noise(source, duration=0.7)
        audio = recognizer.listen(source, phrase_time_limit=6)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except Exception as e:
        print("STT Error:", e)
        return ""

# -----------------------
# 2. TTS: worker + queue (with debug & exception handling)
# -----------------------
tts_queue = queue.Queue()

def tts_worker():
    try:
        # create engine inside thread (important on Windows)
        engine = pyttsx3.init(driverName='sapi5')  # explicit driver on Windows
    except Exception as e:
        print("Failed to init pyttsx3 engine in thread:", e)
        return

    while True:
        text = tts_queue.get()
        if text is None:
            print("[TTS] Received shutdown signal. Exiting worker.")
            tts_queue.task_done()
            break

        try:
            print("[TTS] Speaking:", repr(text[:80]))
            engine.say(text)
            engine.runAndWait()
            print("[TTS] Finished speaking.")
        except Exception as e:
            # catch and show any runtime error
            print("[TTS] Error during speak:", e)
        finally:
            # mark the job done so join() can return
            tts_queue.task_done()

# start worker thread as daemon
tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def speak(text):
    tts_queue.put(text)

# -----------------------
# 3. GROQ SETUP (replace YOUR_KEY)
# -----------------------
client = Groq(api_key="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")

def ask_groq(prompt):
    chat = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
    )
    # basic error handling
    if hasattr(chat, "choices") and len(chat.choices) > 0:
        return chat.choices[0].message.content
    else:
        print("Groq returned no choices:", chat)
        return "Sorry, I could not get an answer."

# -----------------------
# 4. MAIN LOOP
# -----------------------
print("Voice Assistant Ready! Say 'stop' to exit.")

try:
    while True:
        user_input = listen()
        if not user_input:
            continue

        if user_input.lower() in ["exit", "stop", "quit"]:
            print("Stopping…")
            # signal worker to exit after finishing queued items
            tts_queue.put("Goodbye!")
            tts_queue.join()       # wait for Goodbye to finish
            tts_queue.put(None)    # cause worker to shutdown
            tts_queue.join()
            break

        ai_response = ask_groq(user_input)
        print("AI:", ai_response)

        # enqueue speech and WAIT until it's spoken before listening again
        speak(ai_response)
        # Wait for the queue to be emptied (i.e. speech finished)
        tts_queue.join()
        # small safety pause
        time.sleep(0.1)

except KeyboardInterrupt:
    print("Interrupted by user — shutting down.")
    tts_queue.put(None)
    tts_queue.join()
