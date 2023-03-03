import datetime
import pyglet


class Clocks:
    def __init__(self, time=datetime.datetime, count_of_repeat=1, repeat_interval=dict):
        self.data = [{'time': time, 'count_of_repeat': count_of_repeat, 'repeat_interval': repeat_interval}]
        self.sound = pyglet.media.load('file.mp3', streaming=False)
        
    def append(self, time=datetime.datetime, count_of_repeat=1, repeat_interval=dict):
        self.data.append({'time': time, 'count_of_repeat': count_of_repeat, 'repeat_interval': repeat_interval})

    def check(self, dic):
        dic['count_of_repeat'] -= 1
        if dic['count_of_repeat'] == 0:
            return False

        time_d = dic['repeat_interval']
        dic['time'] += datetime.timedelta(days=time_d['days'], hours=time_d['hours'],
                                          minutes=time_d['minute'])
        return dic

    def alarm(self):
        for item in self.data:
            if datetime.datetime.now() > item['time']:
                self.play()
                new = self.check(item)
                self.data.pop(self.data.index(item))
                if new:
                    self.data.append(new)

    def play(self):
        self.sound.play()

clock = Clocks(time=datetime.datetime(year=2023, month=3, day=3, hour=14, minute=47), count_of_repeat=3,
               repeat_interval={'days': 0, 'hours': 0, 'minute': 1})
while True:
    clock.alarm()
