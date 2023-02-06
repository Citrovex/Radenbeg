import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Reading Microphone as source
# listening the speech and store in audio_text variable
with sr.Microphone() as source:
    print("Talk")
    audio = r.listen(source)
    audio_text = r.recognize_google(audio, language="uk-UA")
    print(audio_text)

    print("Time over, thanks")
