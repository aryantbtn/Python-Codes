# Digital Clock with Python
# In this Section, we will saw that how to craete a digital clock using python. This is a simple task to get started with the Tkinter library in python, which is a built-in package that compes with Python. Tkinter has a some cool features that can be used to built simple apps.
'''from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("Digitaal Clock (using tkinder)")
app_window.geometry("435x170")
# app_window.resizable(1,1)
text_font = ("Boulder",  70, 'bold')
backGround = "#f2BC07"
foreGround = "#363634"
borderWidth = 30

label = Label(app_window, font = text_font, bg=backGround, fg=foreGround, bd=borderWidth)
label.grid(row=0, column=1)

def digital_clock():
    live_time = time.strftime("%H:%M:%S")
    label.config(text=live_time)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()'''