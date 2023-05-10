import pyttsx3
engine = pyttsx3.init()
voice_speed = 140
engine.setProperty('rate', voice_speed)


def speaker(text):
    engine.say(text)
    engine.runAndWait()