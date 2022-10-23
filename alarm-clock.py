import tkinter as tk
import time
import winsound


# Initializing window

root = tk.Tk()
root.geometry('512x384')
root.resizable(False, False)
root.config(bg = '#004080')
root.title('Alarm Clock')


# Variables

hour = tk.StringVar()
minutes = tk.StringVar()
seconds = tk.StringVar()


# Adding labels and entries

header_label = tk.Label(text = 'Alarm clock', font = 'courier 15 bold', fg = 'white', bg = '#ff7f00')
select_time_label = tk.Label(text = 'Select time: ', font = 'courier 10 bold', fg = 'white', bg = '#004080')
hour_label = tk.Label(text = 'HOUR', font = 'courier 10', fg = 'black', bg = '#004080')
minutes_label = tk.Label(text = 'MINUTES', font = 'courier 10', fg = 'black', bg = '#004080')
seconds_label = tk.Label(text = 'SECONDS', font = 'courier 10', fg = 'black', bg = '#004080')
hour_entry = tk.Entry(textvariable = hour, width = 4)
minutes_entry = tk.Entry(textvariable = minutes, width = 4)
seconds_entry = tk.Entry(textvariable = seconds, width = 4)
alarm_label = tk.Label(font = 'arial 10 bold', bg = '#004080')

header_label.place(relx = .5, y = 50, anchor = tk.CENTER)
select_time_label.place(x = 100, y = 150)
hour_label.place(x = 250, y = 125, anchor = tk.N)
minutes_label.place(x = 325, y = 125, anchor = tk.N)
seconds_label.place(x = 400, y = 125, anchor = tk.N)
hour_entry.place(x = 250, y = 150, anchor = tk.N)
minutes_entry.place(x = 325, y = 150, anchor = tk.N)
seconds_entry.place(x = 400, y = 150, anchor = tk.N)
alarm_label.place(relx = .5, y = 275, anchor = tk.CENTER)


# Clock

show_time_label = tk.Label(fg = 'white', bg = 'black')
show_time_label.pack(side = 'bottom')

def show_time():
    show_time_label.config(text = time.strftime('%H:%M:%S'))
    show_time_label.after(100, show_time)

show_time()


# Alarm functions

def alarm(x):    
    if x == time.strftime('%H:%M:%S'):
        alarm_label.config(text = 'WAKE UP!')
        winsound.PlaySound('clock-sound.wav', winsound.SND_ASYNC)
    else:
        alarm_label.after(1000, alarm, x)

def alarm_timer(*args):
    set_alarm = f'{hour.get()}:{minutes.get()}:{seconds.get()}'
    alarm_label.config(text = f'Alarm is set to {set_alarm}')
    alarm(set_alarm)


# Reset function

def reset():
    hour.set('')
    minutes.set('')
    seconds.set('')
    alarm_label.config(text = '')


# Exit function

def exit():
    root.destroy()


# Buttons

set_alarm_button = tk.Button(text = 'Set alarm', fg = 'white', bg = '#ff7f00', command = alarm_timer)
root.bind('<Return>', alarm_timer)
reset_button = tk.Button(text = 'Reset', command = reset)
exit_button = tk.Button(text = 'Exit', command = exit)

set_alarm_button.place(relx = .5, y = 225, anchor = tk.CENTER)
reset_button.place(x = 200, y = 300)
exit_button.place(x = 275, y = 300)

root.mainloop()