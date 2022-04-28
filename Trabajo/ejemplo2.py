import speech_recognition as sr

# Crear una instancia de la clase Recognizer y Microphone.
r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    audio = r.listen(source)

print(r.recognize_google(audio))