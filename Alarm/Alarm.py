from datetime import datetime
from pygame import mixer


mixer.init()


class Alarm:
    def __init__(self):
        self.currentTime = datetime.now().strftime("%H:%M:%S")
        self.userTime = input("Write a time (03:50:01):")
        mixer.music.load("Components/AlarmClockMelody.mp3")
        self.alarm_clock()

    def alarm_clock(self):
        while True:
            self.currentTime = datetime.now().strftime("%H:%M:%S")
            if self.userTime == self.currentTime:
                mixer.music.play(-1)
                if input("Do you wont to stop alarm?\n") == "yes":
                    mixer.music.stop()
                    break


Alarm()
