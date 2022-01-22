import pygame
from gtts import gTTS
from time import sleep
import os
import speech_recognition as sr


def speak(text):
    tts = gTTS(text=text, lang='en')
    filename = 'voice.mp3'
    tts.save(filename)
    pygame.mixer.init()
    pygame.mixer.music.load("voice.mp3")
    pygame.mixer.music.set_volume(0.7)
    pygame.mixer.music.play(0)

    while(pygame.mixer.music.get_busy()):
        pass


def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        try:
            said = r.recognize_google(audio)
            print(said)
        except Exception as e:
            print("Exception " + str(e))

        return said


# speak("hello")
text = get_audio()

if "hello" in text:
    speak("Hello there you freak")
