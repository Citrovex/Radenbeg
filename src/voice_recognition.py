from typing import Callable
import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


def listen(callback: Callable[[str], None], autoContinue = False):
    firstRun = True
    if callback:
        while firstRun or autoContinue:
            with sr.Microphone() as source:
                audio = r.listen(source)
                audio_text = r.recognize_google(audio, language="uk-UA")
                callback(audio_text)
            
            if firstRun:
                firstRun = False
