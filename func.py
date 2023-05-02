import requests
from webbrowser import open_new_tab
from pathlib import Path
import os
from voice import speaker

os.system('chcp 1251')


def out_all_networks():
    mas = []
    output = os.popen('netsh wlan show profiles').read()
    for item in output.split('\n'):
        item = list(item.split(': '))
        if len(item) == 1:
            continue
        title = item[-1]
        mas.append(title)
    return mas


def connect_network(title):
    os.system(f'netsh wlan connect name="{title}"')


def variables(mas):
    outp = []
    for i in mas['alternative']:
        outp.append(i['transcript'])
    return outp


def get_weather(city_name):
    outp = []
    API_key = "d879234d7b125e8f3ed1e2d29adbeef9"
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    weather_data = requests.get(base_url, params={'appid': API_key, 'q': city_name, 'cnt': '4',
                                                  'units': 'metric'}).json()

    if weather_data['message'] == 0:
        for i in range(4):
            w = weather_data['list'][i]
            time = w['dt_txt'].split()[0].split('-')
            time = '.'.join(time[::-1]) + ' ' + w['dt_txt'].split()[-1]
            temp = w['main']['temp']
            feels_like = w['main']['feels_like']
            humidity = str(w['main']['humidity']) + '%'
            weather = w['weather'][0]['main']
            outp.append({'time': time, 'temp': temp,
                         'feels_like': feels_like, 'humidity': humidity, 'weather': weather})
        return outp

    return 'неправильное название города'


def web_search(inp):
    open_new_tab(inp)


def search_on_disks(name, disk):
    k = 0
    flag = False
    a = None
    while k <= 10:
        alb = sorted(Path(f'{disk}:/').glob('*/' * k + f'{name}.*'))
        if alb:
            for a in alb:
                print(a)
                ans = input('это то?\n')
                if ans.lower() != 'нет':
                    flag = True
                    break
        if flag:
            break        
        k += 1
    return a


def shutdown():
    os.system(f'shutdown -s -f -t 10')


def reboot():
    os.system(f'shutdown -r -f -t 10')


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