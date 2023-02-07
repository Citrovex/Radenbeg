import pyttsx3
engine = pyttsx3.init()


def say(text: str):
    if (text):
        engine.say(text)
        engine.runAndWait()
