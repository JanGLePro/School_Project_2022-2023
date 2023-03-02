import requests
from webbrowser import open_new_tab
from pathlib import Path


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
