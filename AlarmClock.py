import datetime
import os
import time

import pygame
pygame.init()
pygame.mixer.init()


class Clocks:
    def __init__(self):
        self.data = []

    def append(self, repeat_interval, time=datetime.datetime.now(), count_of_repeat=1, music='file.mp3'):
        self.data.append({'time': time, 'count_of_repeat': count_of_repeat, 'repeat_interval': repeat_interval,
                          'sound': music})

    def alarm(self):
        musics = []
        for item in self.data:
            if datetime.datetime.now() > item['time']:
                item['count_of_repeat'] -= 1

                musics.append(item['sound'])
                if item['count_of_repeat'] == 0:
                    del self.data[self.data.index(item)]
                    continue
                item['time'] = max(item['time'], datetime.datetime.now()) + item['repeat_interval']
        if musics:
            self.play_musics(musics)

    def play_musics(self, musics):
        for music in musics:
            pygame.mixer.Sound(music).play(loops=2)

    def stop_music(self):
        pygame.mixer.stop()

clock = Clocks()
clock.append(datetime.timedelta(seconds=60), count_of_repeat=-1, music='Pirates.mp3')
while True:
    clock.alarm()
