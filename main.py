import speech_recognition as sr
from func import variables

languages = {1: 'ru-RU', 2: 'en-EN'}

r = sr.Recognizer()
mic = sr.Microphone()

with mic as source:
    print('говорите')
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)

rezult_ru = variables(r.recognize_google(audio, language=languages[1], show_all=True))
rezult_en = variables(r.recognize_google(audio, language=languages[2], show_all=True))
print(rezult_ru, rezult_en)