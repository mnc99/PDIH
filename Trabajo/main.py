from calendar import month
import speech_recognition as sr
# Access to browser
import webbrowser
import time
# Library to play audio files right from the editor
import playsound
# Use to remove audio files
import os
# Generate a random name for the audio files
import random
from gtts import gTTS
from time import ctime
import datetime

# Main class of sr which contains all funcionality for speech recognition
r = sr.Recognizer()

# Function to record audio from microphone
def record_audio(ask = False):
    # Use the microphone as source of audio
    with sr.Microphone() as source:
        if ask:
            jarvis_speak(ask)
        audio = r.listen(source, phrase_time_limit=4)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio, language='es-ES')
        except sr.UnknownValueError:
            jarvis_speak('Lo siento, no te he entendido...')
        except sr.RequestError:
            jarvis_speak('Lo siento, servicio no disponible por el momento')
        return voice_data

# Function to make Jarvis speak
def jarvis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='es')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

def week_day_spanish(week_day):
    if week_day == 'Monday': week_day = 'Lunes'
    elif week_day == 'Tuesday': week_day = 'Martes'
    elif week_day == 'Wednesday': week_day = 'Miércoles'
    elif week_day == 'Thursday': week_day = 'Jueves'
    elif week_day == 'Friday': week_day = 'Viernes'
    elif week_day == 'Saturday': week_day = 'Sábado'
    else: week_day = 'Domingo'

    return week_day

def month_spanish(month_name):
    if month_name == 'January': month_name = 'Enero'
    elif month_name == 'February': month_name = 'Febrero'
    elif month_name == 'March': month_name = 'Marzo'
    elif month_name == 'April': month_name = 'Abril'
    elif month_name == 'May': month_name = 'Mayo'
    elif month_name == 'June': month_name = 'Junio'
    elif month_name == 'July': month_name = 'Julio'
    elif month_name == 'August': month_name = 'Agosto'
    elif month_name == 'September': month_name = 'Septiembre'
    elif month_name == 'October': month_name = 'Octubre'
    elif month_name == 'November': month_name = 'Noviembre'
    else: month_name = 'Diciembre'

    return month_name

# Voice commands
def respond(voice_data):
    if 'dime tu nombre' in voice_data:
        jarvis_speak('Mi nombre es Yarvis y soy tu asistente virtual')

    if 'qué hora es' in voice_data:
        now = datetime.datetime.now()
        hour = '{:02d}'.format(now.hour)
        minute = '{:02d}'.format(now.minute)
        jarvis_speak('Son las ' + hour + ':' + minute)

    if 'fecha' in voice_data:
        now = datetime.datetime.now()
        month_day = '{:02d}'.format(now.day)
        month_name = now.strftime("%B")
        month_name = month_spanish(month_name)
        year = '{:02d}'.format(now.year)
        week_day = now.strftime("%A")
        week_day = week_day_spanish(week_day)
        jarvis_speak('Es ' + week_day + ', ' + month_day + ' de ' + month_name + ' de ' + year)

    if 'buscar' in voice_data:
        search = record_audio('¿Qué quieres que busque?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        jarvis_speak('Esto es lo que he encontrado sobre ' + search)

    if 'localización' in voice_data:
        location = record_audio('¿Qué localización deseas buscar?')
        url = 'https://google.es/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        jarvis_speak('Aquí está la localización de ' + location)

    if 'hasta luego' in voice_data:
        jarvis_speak('¡Adiós!')
        exit()

time.sleep(1)
jarvis_speak('¿En qué puedo ayudarte?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
