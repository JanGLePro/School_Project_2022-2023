import datetime
import pyglet


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
            pyglet.media.load(music, streaming=False).play()


clock = Clocks()
clock.append(time=datetime.datetime.now(), count_of_repeat=3, repeat_interval=datetime.timedelta(seconds=10))
clock.append(repeat_interval=datetime.timedelta(seconds=35), count_of_repeat=2, music='top.mp3')
while True:
    clock.alarm()
