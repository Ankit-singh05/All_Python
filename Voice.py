import queue
import threading
import speech_recognition as sr
import pyttsx3
from groq import Groq, APIError, RateLimitError, Timeout
import time
import logging
import pvporcupine
import pyaudio
import struct

# -------------------------- Logging --------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------------- 1. GROQ SETUP --------------------------
client = Groq(api_key="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")

def ask_groq(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500,
            timeout=20
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        logger.error(f"Groq error: {e}")
        return "Sorry, I had a problem connecting."

# -------------------------- 2. WAKE WORD DETECTION (HEY GROK) --------------------------
WAKE_WORD = "hey grok"

# Get your free Porcupine access key: https://console.picovoice.ai/
PORCUPINE_ACCESS_KEY = "YOUR_PICOVOICE_ACCESS_KEY_HERE"   # ← GET FREE KEY HERE

try:
    porcupine = pvporcupine.create(
        access_key=PORCUPINE_ACCESS_KEY,
        keyword_paths=[pvporcupine.KEYWORD_PATHS["hey grok"]]  # Built-in "hey grok"
    )
    pa = pyaudio.PyAudio()
    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length
    )
    print("WAKE WORD DETECTION ACTIVE → Say 'Hey Grok' to wake me up!")
    WAKE_WORD_WORKS = True
except Exception as e:
    print(f"Porcupine wake word failed: {e}")
    print("Falling back to always-listening mode...")
    WAKE_WORD_WORKS = False

# -------------------------- 3. SPEECH RECOGNITION --------------------------
recognizer = sr.Recognizer()

def wait_for_wake_word() -> bool:
    if not WAKE_WORD_WORKS:
        return True  # Always "wake" if wake word not available
    print("Listening for wake word... (say 'Hey Grok')")
    while True:
        pcm = audio_stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        keyword_index = porcupine.process(pcm)
        if keyword_index == 0:
            print("Wake word detected! 'Hey Grok!'")
            speak("Yes? How can I help you?")
            return True

def listen() -> str:
    with sr.Microphone() as source:
        print("Listening for your question...")
        recognizer.adjust_for_ambient_noise(source, duration=0.7)
        try:
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=15)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return ""
        except sr.UnknownValueError:
            print("I didn't catch that.")
            return ""
        except Exception as e:
            logger.error(f"Mic error: {e}")
            return ""

# -------------------------- 4. SLOW & CLEAR TTS --------------------------
tts_queue = queue.Queue()

def tts_worker():
    while True:
        item = tts_queue.get()
        if item is None:
            break
        text = item.strip()
        if not text:
            continue
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 135)     # Super slow & clear
            engine.setProperty('volume', 1.0)
            print(f"Speaking: {text}\n")
            engine.say(text)
            engine.runAndWait()
            time.sleep(2.0)   # Long natural pause
        except Exception as e:
            logger.error(f"TTS error: {e}")
        finally:
            if 'engine' in locals():
                try: engine.stop()
                except: pass
        tts_queue.task_done()

tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def speak(text: str):
    if text and text.strip():
        tts_queue.put(text.strip())

# -------------------------- 5. MAIN LOOP WITH WAKE WORD --------------------------
if __name__ == "__main__":
    print("\nHEY GROK VOICE ASSISTANT - WAKE WORD READY\n")
    speak("Wake word detection is active. Say 'Hey Grok' anytime!")

    try:
        while True:
            # 1. Wait for wake word
            if not wait_for_wake_word():
                continue

            # 2. Listen to your question
            user_input = listen()
            if not user_input:
                speak("I didn't hear anything. I'm going back to sleep.")
                time.sleep(1)
                continue

            if user_input in ["exit", "stop", "quit", "bye", "goodbye", "nevermind"]:
                speak("Okay, going back to sleep. Say 'Hey Grok' when you need me!")
                continue

            # 3. Think and respond
            print("Thinking...")
            time.sleep(1.2)
            response = ask_groq(user_input)
            print(f"AI: {response}\n")
            speak(response)

            time.sleep(2.5)  # Give you time to reply or say next thing

    except KeyboardInterrupt:
        speak("Goodbye forever!")
    finally:
        tts_queue.put(None)
        if WAKE_WORD_WORKS:
            porcupine.delete()
            audio_stream.close()
            pa.terminate()
        print("Assistant shut down.")