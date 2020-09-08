seconds = 0
minutes = 5
hours = 0
pause = 1

import time
from tkinter import *

top = Tk()

from turtle import *
setup()
tl = Turtle()

def pausefunc():
    pause *= -1

B = Button(top, text ="Pause", command = pausefunc)
    
B.pack()


while True:
    if pause == 1:
        tl.clear()
        tl.write(str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(seconds).zfill(2), font = ('arial', 25, 'normal'))
        seconds = seconds - 1
        time.sleep(1)
        
        if seconds < 0 :
            seconds = 59
            minutes = minutes - 1
        
        if minutes < 0:
            minutes = 59
            hours = hours - 1
    

top.mainloop()

