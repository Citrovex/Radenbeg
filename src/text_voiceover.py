import os

from gtts import gTTS
import playsound

from .configurator import getConfig


conf = getConfig()

def say(text: str):
    while True:
        try:
            # Create an instance of gTTS class
            speech = gTTS(text=text, lang=conf['language']['code'])

            # Save the speech audio file temporarily
            speech.save("temp.mp3")

            # Play the audio file
            playsound.playsound("temp.mp3")

            # Delete the temporary file
            os.remove("temp.mp3")

            break

        except playsound.PlaysoundException as _e:
            pass

        except Exception as e:
            print("Error: could not play sound. Error:", e)
            break
        