import queue
import threading
import speech_recognition as sr
import pyttsx3
from groq import Groq, APIError, RateLimitError, Timeout
import time
import logging

# -------------------------- Logging Setup --------------------------
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# -------------------------- 1. GROQ SETUP --------------------------
client = Groq(api_key="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")  # ← CHANGE THIS!

def ask_groq(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500,
            timeout=20  # seconds
        )
        return response.choices[0].message.content.strip()

    except RateLimitError:
        logger.error("Rate limited by Groq. Slowing down...")
        return "I'm being rate-limited. Please wait a moment and try again."
    except Timeout:
        logger.error("Groq request timed out")
        return "The AI is taking too long to respond. Try again."
    except APIError as e:
        logger.error(f"Groq API error: {e}")
        return "Sorry, there's an issue with the AI service."
    except Exception as e:  # Only unknown errors reach here (very rare)
        logger.critical(f"Unexpected Groq error: {e}")
        return "Something went wrong on my side."

# -------------------------- 2. SPEECH RECOGNITION --------------------------
recognizer = sr.Recognizer()

def listen() -> str:
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
            return text.lower()
        except sr.WaitTimeoutError:
            return ""  # No speech detected
        except sr.UnknownValueError:
            print("I couldn't understand what you said.")
            return ""
        except sr.RequestError as e:
            logger.error(f"Speech recognition service error: {e}")
            print("Speech recognition is offline.")
            return ""
        except Exception as e:
            logger.error(f"Microphone error: {e}")
            return ""

# -------------------------- 3. RELIABLE TTS (NO BROAD EXCEPT) --------------------------
tts_queue = queue.Queue()

def tts_worker():
    while True:
        item = tts_queue.get()
        if item is None:
            break

        text = item.strip()
        if not text:
            tts_queue.task_done()
            continue

        engine = None
        try:
            engine = pyttsx3.init()
            engine.setProperty('rate', 180)
            engine.setProperty('volume', 1.0)

            print(f"Speaking: {text}")
            engine.say(text)
            engine.runAndWait()

        except RuntimeError as e:
            logger.warning(f"TTS RuntimeError (common on some systems): {e}")
        except AttributeError as e:
            logger.error(f"TTS AttributeError - engine corrupted: {e}")
        except Exception as e:
            logger.error(f"Unexpected TTS error: {type(e).__name__}: {e}")
        finally:
            if engine:
                try:
                    engine.stop()
                except:
                    pass
            tts_queue.task_done()

# Start TTS thread
tts_thread = threading.Thread(target=tts_worker, daemon=True)
tts_thread.start()

def speak(text: str):
    if text and text.strip():
        tts_queue.put(text.strip())

def shutdown_tts():
    tts_queue.put(None)
    tts_thread.join(timeout=3)

# -------------------------- 4. MAIN LOOP --------------------------
if __name__ == "__main__":
    print("\nVOICE ASSISTANT STARTED! (Say 'exit' to stop)\n")
    speak("Hello! I'm ready. How can I help you?")

    try:
        while True:
            user_input = listen()

            if not user_input:
                continue

            if user_input in ["exit", "stop", "quit", "bye", "goodbye"]:
                speak("Goodbye! See you next time!")
                break

            print("Thinking...")
            response = ask_groq(user_input)
            print(f"AI: {response}\n")
            speak(response)

    except KeyboardInterrupt:
        print("\nStopped by user.")
        speak("Shutting down. Bye!")

    finally:
        shutdown_tts()
        print("Assistant fully stopped.")