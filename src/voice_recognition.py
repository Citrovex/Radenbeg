from typing import Callable
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


def listen(callback: Callable[[str]]):
    if callback:
        while True:
            with sr.Microphone() as source:
                audio = r.listen(source)
                audio_text = r.recognize_google(audio, language="uk-UA")
                callback(audio_text)
