from tkinter import *
import time
import datetime
from playsound import playsound


# sets the alarm time and then when the time is reached stop and play the alarm sound
def alarm(set_alarm_timer):
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        print(now)
        print(set_alarm_timer)
        if now == set_alarm_timer:
            playsound('C:/Users/epicg/PycharmProjects/alarmClock/alarm.mp3')
            break


# sets the alarm time for when it should go off
def alarm_time_setter():
    if int(hour.get()) < 0 or int(hour.get()) > 23:
        raise ValueError('Hours should be between 0 and 23 hours.')
    if int(minute.get()) < 0 or int(minute.get()) > 60:
        raise ValueError('Minutes should be between 0 and 60.')
    set_alarm_timer = f"{hour.get()}:{minute.get()}:00"
    alarm(set_alarm_timer)


# initialisation of the window
tk = Tk()
tk.config(background='grey')
tk.title('Alarm Clock')
tk.geometry("400x200")
tk['background'] = '#856ff8'

# hours dropdown menu
hour = StringVar(tk)
hourSet = Entry(tk, textvariable=hour, bg='#12C8CB', width=5, font=('times', 15)).place(x=130, y=50)

# minutes dropdown menu
minute = StringVar(tk)
minutesSet = Entry(tk, textvariable=minute, bg='#12C8CB', width=5, font=('times', 15)).place(x=200, y=50)

# label for the hours
hourLabel = Label(tk, text="Hour", bg='#856ff8', font=("times", 15)).place(x=135, y=5)

# label for the minutes
minuteLabel = Label(tk, text="Minute", bg='#856ff8', font=("times", 15)).place(x=195, y=5)

# add the button to set the alarm time
setAlarmTime = Button(tk, text='Set Alarm', command=alarm_time_setter).place(x=160, y=100)

tk.mainloop()
