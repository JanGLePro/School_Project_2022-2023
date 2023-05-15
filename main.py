import config
import stt
from fuzzywuzzy import fuzz
from pymorphy2 import MorphAnalyzer as MA
from mega_dict import mega_dict, math_dict
from func import *
withouth_data = ['hibernation', 'blocking', 'log_out', 'cancellation', 'mute', 'unmute',
                 'passive', 'play_greetings', 'joke', 'get_help', 'how_time', 'out_all_networks', 'click',
                 'changing_the_layout']
ma = MA()


print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            speaker("Что?")
        else:
            execute_cmd(cmd['cmd'], voice)


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 30}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            print(cmd)
            vrt = fuzz.ratio(cmd, x)
            if cmd in x or x in cmd and vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = 100
                break
            elif vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd, text_message):
    if cmd in withouth_data:
        eval(cmd)()
    else:
        text_message = [str(mega_dict[ma.parse(i)[0].normal_form]) if ma.parse(i)[0].normal_form in mega_dict
                        else i for i in text_message.split()]
        n = 0
        for i in text_message:
            if i.isdigit():
                n += int(i)

        if cmd == 'get_weather':
            for word in text_message:
                if 'Geox' in ma.parse(word)[0].tag:
                    get_weather(ma.parse(word)[0].normal_form)
                    break
        elif cmd == 'connect_network':
            mas = {i: 0 for i in out_all_networks()}
            maxim = 0
            item = None
            for word in text_message[2:]:
                for i in mas:
                    mas[i] += max(fuzz.ratio(translate_my_word(word), i), fuzz.ratio(word, i))
                    maxim = max(maxim, mas[i])
                    if mas[i] > maxim:
                        maxim = mas[i]
                        item = i
            connect_network(item)
        elif cmd == 'web_search':
            text_message = ' '.join(text_message)
            text_message = min([text_message.replace(x, '', 1) for x in config.VA_CMD_LIST['web_search']],
                               key=lambda x: len(x)).replace('олег', '', 1).lstrip()
            web_search(text_message)
        # alarm
        elif cmd == 'alarm_func':
            h = m = None
            fh = False
            for i in text_message:
                if i.isdigit():
                    if h is None:
                        h = int(i)
                    elif len(i) < len(str(h)) and not fh:
                        h += int(i)
                        fh = True
                    elif m is None:
                        m = int(i)
                    elif len(i) < len(str(m)):
                        m += int(i)
            print(h, m)
            alarm_func(h, m)
        elif cmd == 'math_it':
            for i in range(len(text_message)):
                if text_message[i].isdigit():
                    math_it(' '.join([math_dict[x] if x in math_dict else x for x in text_message[i:]]).replace(' на ',
                                                                                                                '', 1))
                    break
        else:
            eval(cmd)(n)



# начать прослушивание команд
stt.va_listen(va_respond)
print(666)