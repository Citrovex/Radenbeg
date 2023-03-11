import speech_recognition as sr

from .configurator import getConfig

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()


def listen(autoContinue=False):
    config = getConfig()

    firstRun = True
    while firstRun or autoContinue:
        with sr.Microphone() as source:
            try:
                audio = r.listen(source)
                audio_text = r.recognize_google(audio, language=config['language']['code'])
                yield audio_text
            except sr.UnknownValueError as _e:
                pass

        if firstRun:
            firstRun = False
