import datetime
import pyglet


class Clocks:
    def __init__(self, time=datetime.datetime, count_of_repeat=1, repeat_interval=dict):
        self.data = [{'time': time, 'count_of_repeat': count_of_repeat, 'repeat_interval': repeat_interval}]
        self.sound = pyglet.media.load('file.mp3', streaming=False)

    def append(self, time=datetime.datetime, count_of_repeat=1, repeat_interval=dict):
        self.data.append({'time': time, 'count_of_repeat': count_of_repeat, 'repeat_interval': repeat_interval})

    def alarm(self):
        flag = False
        for item in self.data:
            if datetime.datetime.now() % item['repeat_interval'] == 0:

                if datetime.datetime.now() > item['time']:
                    flag = True
                    item['count_of_repeat'] -= 1
                    if item['count_of_repeat'] == 0:
                        del self.data[self.data.index(item)]

                    time_d = item['repeat_interval']
                    item['time'] += datetime.timedelta(days=time_d['days'], hours=time_d['hours'],
                                                      minutes=time_d['minute'])
        if flag:
            self.play()

    def play(self):
        self.sound.play()

clock = Clocks(time=datetime.datetime(year=2023, month=3, day=3, hour=14, minute=47), count_of_repeat=3,
               repeat_interval=datetime.timedelta(minute=1))
while True:
    clock.alarm()
