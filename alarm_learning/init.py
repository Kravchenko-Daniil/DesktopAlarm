import datetime
from pygame import mixer

def validate_time(time):
    if len(time) != 8:
        return 'Не правильны формат времени'
    elif time[2] != ':':
        return f"Не правильны формат времени. Поменяйте символ {time[2]} на двоеточие"
    elif time[5] != ':':
        return f"Не правильны формат времени. Поменяйте символ {time[5]} на двоеточие"
    else:
        if int(time[0:2]) > 23:
            return 'Часы указаны не верно'
        elif int(time[3:5]) > 59:
            return 'Чинуты указаны не верно'
        elif int(time[6:8]) > 59:
            return 'Секунды указаны не верно'
        else:
            return 1

while True:
    alarm_time = input('Введите время в формате часы:минуты:секунды\nВремя: ')
    valid_time = validate_time(alarm_time)
    if valid_time == 1:
        print('время указано верно')
    else:
        print(f"Ошибака\n{valid_time}")
    break

alarm_hour = int(alarm_time[0:2])
alarm_min = int(alarm_time[3:5])
alarm_sec = int(alarm_time[6:8])

while True:
    now_time = datetime.datetime.now().time()
    now_hour = now_time.hour
    now_min = now_time.minute
    now_sec = now_time.second

    if now_hour == alarm_hour and now_min == alarm_min and alarm_sec == now_sec:
        print('Пора вставать')
        mixer.init()
        mixer.music.load("file/mine.mp3")
        mixer.music.play(-1)

        a = input("Press yes: ")

        while True:
            if a != 'yes':
                a = input("Press yes: ")
            else:
                break
        break
