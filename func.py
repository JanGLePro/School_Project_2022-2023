import datetime
import webbrowser

from stt import clock
import requests
from webbrowser import open_new_tab
from pathlib import Path
import os
import keyboard
import pyautogui
from AlarmClock import Clocks
from tts import speaker
import random
from googletrans import Translator  # pip install googletrans==3.1.0a0

translator = Translator()

os.system('chcp 1251')

webbrowser.register('Chrome', None,
                    webbrowser.BackgroundBrowser('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe'))


def out_all_networks():
    mas = []
    output = os.popen('netsh wlan show profiles').read()
    for item in output.split('\n'):
        item = list(item.split(': '))
        if len(item) == 1:
            continue
        title = item[-1]
        mas.append(title)
    speaker(' ...'.join(mas))


def connect_network(title):
    os.system(f'netsh wlan connect name="{title}"')


def get_weather(city_name):
    API_key = "d879234d7b125e8f3ed1e2d29adbeef9"
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    weather_data = requests.get(base_url, params={'appid': API_key, 'q': city_name, 'cnt': '4',
                                                  'units': 'metric'}).json()

    if weather_data['message'] == 0:
        w = weather_data['list'][0]
        temp = w['main']['temp']
        feels_like = w['main']['feels_like']
        humidity = str(w['main']['humidity']) + '%'
        weather = w['weather'][0]['main']
        speaker(f'{translate_my_word(weather, "en", "ru")} ... температура {temp}, ощущается как {feels_like},'
                f'влажность {humidity}')
    else:

        speaker('неправильное название города')


def web_search(text):
    webbrowser.get(using='Chrome').open_new_tab('https://yandex.ru/search/?text=' + text)


def how_time():
    h, m = datetime.datetime.now().hour, datetime.datetime.now().minute
    x = y = ''
    if 2 <= h % 20 <= 4:
        x = 'а'
    elif 5 <= h % 20 <= 20 or h % 20 == 0:
        x = 'ов'
    if m % 10 == 1 and m // 10 != 1:
        y = 'а'
    elif 2 <= m % 10 <= 4 and m // 10 != 1:
        y = 'ы'
    speaker(f'сейчас {h} час{x}, {m} минут{y}')


def shutdown(t):
    os.system(f'shutdown -s -f -t {t}')


def reboot(t):
    os.system(f'shutdown -r -f -t {t}')


def hibernation():
    os.system('shutdown -h')


def blocking():
    os.system('Rundll32.exe user32.dll,LockWorkStation')


def log_out():
    os.system('shutdown -l')


def cancellation():
    os.system('shutdown -a')


def math_it(message):
    try:
        speaker(eval(message))
    except:
        speaker("U're FUCKING LOOSER")


def mute():
    os.system('setvol mute')


def unmute():
    os.system('setvol unmute')


def volume(n):  # 0 < n < 100
    n = max(min(n, 100), 0)
    if n == 0:
        mute()
    else:
        unmute()
        os.system(f'setvol {n}')


def lightness(n):  # 0 < n < 100
    n = max(min(n, 100), 0)
    os.system('powershell (Get-WmiObject -Namespace root/WMI'
              f' -Class WmiMonitorBrightnessMethods).WmiSetBrightness(1,{n})')


def passive():
    return ...


def joke():
    jokes = ['Как смеются программисты? ... ехе ехе ехе',
             'ЭсКьюЭль запрос заходит в бар, подходит к двум столам и спрашивает .. «можно присоединиться?»',
             'Программист это машина для преобразования кофе в код']

    speaker(random.choice(jokes))


def get_help():
    # help
    text = ["Я умею:"]
    text += ["произносить время"]
    text += ["рассказывать анекдоты"]
    text += ["открывать браузер"]
    text += ['запускать гибернацию']
    text += ['блокировать компьютер']
    text += ['выходить из пользователя']
    text += ['выключать и перезагружать, а также отменять']
    text += ['менять звук и яркость']
    text += ['говорить погоду']
    text += ['переподключать интернет и ставить будильник']
    speaker(' ...'.join(text))


def play_greetings():
    speaker('привет, меня зовут Олег. Я ваш голосовой помощник')


def translate_my_word(word, src='ru', dest='en'):

    result = translator.translate(word, src=src, dest=dest)
    return result.text


def alarm_func(hours, minutes):
    h, m = datetime.datetime.now().hour, datetime.datetime.now().minute
    if h and m:
        hours -= h
        minutes -= m
        if hours < 0:
            hours += 24
        if minutes < 0:
            minutes += 60
            hours -= 1
        clock.append(datetime.timedelta(seconds=11), datetime.datetime.now() +
                     datetime.timedelta(hours=hours, minutes=minutes), 7)

        
def changing_the_layout():
    keyboard.press_and_release('win + space')


def scroll_down():
    pyautogui.scroll(5)


def scroll_up():
    pyautogui.scroll(-5)


def click():
    pyautogui.click()
