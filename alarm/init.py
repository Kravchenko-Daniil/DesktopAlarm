from pygame import mixer
from datetime import datetime

def dateToTimeClear(a):
    a = str(a)
    a = a.split(' ')[1]
    if len(a) > 1:
        a = a.split('.')[0]
    return a
    
end_time = dateToTimeClear(datetime.strptime(input('Type time H:M:S'), '%H:%M:%S'))

while True:
    start_time = dateToTimeClear(datetime.now())
    print(start_time)

    if start_time == end_time:
        mixer.init()
        mixer.music.load("alarm.mp3")
        mixer.music.play()

        a = input("Pres yes: ")

        while True:
            if a == 'yes':
                break
            else:
                a = input("Enter yes: ")

        break
