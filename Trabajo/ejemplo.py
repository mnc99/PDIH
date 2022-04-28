import speech_recognition as sr

# Crear una instancia de la clase Recognizer.
r = sr.Recognizer()

# Instancia de la clase AudioFile
harvard = sr.AudioFile("harvard.wav")
with harvard as source:
    # Capta los datos del archivo de audio en una variable de tipo AudioData 
    audio = r.record(source) 

# Mostrar por pantalla el audio transcrito
print(r.recognize_google(audio))