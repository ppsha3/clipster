## Title: Clipster
## Made by: Priyesh Sharma

from keyboard import add_hotkey
import pyautogui 
import pyperclip
import time
from tkinter import *

def popup():

    global listbox
    
    listbox = Listbox(window, selectmode='single', width=30, height=30, font=('times',13))

    for item in buffer:
        listbox.insert(END, item)

    listbox.pack()
    listbox.bind('<<ListboxSelect>>', paste_to_programs)
    
    window.mainloop()

    return

def paste_to_programs(e):

    pyperclip.copy(listbox.get(int(listbox.curselection()[0])))
    pyperclip.paste()
    
    pyautogui.click(mouse_loc[0], mouse_loc[1])
    pyautogui.hotkey("ctrl", "v")

    window.destroy()

    return

def add_to_clipster():

    buffer.append(pyperclip.paste())
    print(buffer)
    
    return    


mouse_loc = pyautogui.position()
buffer = []

window = Tk()
window.bind("ctrl+shift+c", popup)
window.bind("ctrl+c", add_to_clipster)
window.withdraw()

##keyboard.add_hotkey('ctrl+shift+c', popup)
##keyboard.add_hotkey('ctrl+c', add_to_clipster)

