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
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            jarvis_speak('Sorry, I did not get that')
        except sr.RequestError:
            jarvis_speak('Sorry, my speech service is down')
        return voice_data

# Function to make Jarvis speak
def jarvis_speak(audio_string):
    tts = gTTS(text=audio_string, lang='en')
    r = random.randint(1, 1000000)
    audio_file = 'audio-' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(audio_string)
    os.remove(audio_file)

# Voice commands
def respond(voice_data):
    if 'what is your name' in voice_data:
        jarvis_speak('My name is Jarvis')

    if 'what time is it' in voice_data:
        now = datetime.datetime.now()
        hour = '{:02d}'.format(now.hour)
        minute = '{:02d}'.format(now.minute)
        jarvis_speak('It´s ' + hour + ':' + minute)

    if 'what is the date today' in voice_data:
        now = datetime.datetime.now()
        month_day = '{:02d}'.format(now.day)
        month_name = now.strftime("%B")
        year = '{:02d}'.format(now.year)
        week_day = now.strftime("%A")
        jarvis_speak('It´s ' + week_day + ', ' + month_name + ' ' + month_day + ', ' + year)

    if 'search' in voice_data:
        search = record_audio('What do you want to search for?')
        url = 'https://google.com/search?q=' + search
        webbrowser.get().open(url)
        jarvis_speak('Here is what I found for ' + search)

    if 'find location' in voice_data:
        location = record_audio('What is the location?')
        url = 'https://google.es/maps/place/' + location + '/&amp;'
        webbrowser.get().open(url)
        jarvis_speak('Here is the location of ' + location)

    if 'bye' in voice_data:
        jarvis_speak('Good bye!')
        exit()

time.sleep(1)
jarvis_speak('How can I help you?')
while 1:
    voice_data = record_audio()
    respond(voice_data)
