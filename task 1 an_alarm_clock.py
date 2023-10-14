# -*- coding: utf-8 -*-
"""An Alarm Clock.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1GBp8faVzHwIlBMffUaRA7R7Z7qHIRq57
"""

import datetime
import tkinter as tk
from tkinter import messagebox


def set_alarm():
    alarm_time = entry.get()
    current_time = datetime.datetime.now().strftime("%H:%M")

    if alarm_time == current_time:
        messagebox.showinfo("Alarm", "Wake up!")
    else:
        messagebox.showinfo("Alarm", "Alarm set for " + alarm_time)


root = tk.Tk()
root.title("Alarm Clock")

label = tk.Label(root, text="Enter alarm time (24-hour format):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Set Alarm", command=set_alarm)
button.pack()

root.mainloop()



