import config
import stt
from fuzzywuzzy import fuzz
import datetime
from num2words import num2words as num2text  #pip install num2words
import webbrowser
from func import *
withouth_data = ['shutdown', 'reboot', 'hibernation', 'blocking', 'log_out', 'cancellation', 'mute', 'unmute',
                 'passive', 'play_greetings', 'joke', 'get_help', 'web_search']


print(f"{config.VA_NAME} (v{config.VA_VER}) начал свою работу ...")


def va_respond(voice: str):
    print(voice)
    if voice.startswith(config.VA_ALIAS):
        # обращаются к ассистенту
        cmd = recognize_cmd(filter_cmd(voice))

        if cmd['cmd'] not in config.VA_CMD_LIST.keys():
            tts.speaker("Что?")
        else:
            execute_cmd(cmd['cmd'], voice)


def filter_cmd(raw_voice: str):
    cmd = raw_voice

    for x in config.VA_ALIAS:
        cmd = cmd.replace(x, "").strip()

    for x in config.VA_TBR:
        cmd = cmd.replace(x, "").strip()

    return cmd


def recognize_cmd(cmd: str):
    rc = {'cmd': '', 'percent': 0}
    for c, v in config.VA_CMD_LIST.items():

        for x in v:
            vrt = fuzz.ratio(cmd, x)
            if vrt > rc['percent']:
                rc['cmd'] = c
                rc['percent'] = vrt

    return rc


def execute_cmd(cmd, voice):
    if cmd in withouth_data:
        eval(cmd)()
    else:
        data = []
        ...

        eval(cmd)(*data)


# начать прослушивание команд
stt.va_listen(va_respond)