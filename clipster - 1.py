## Title: Clipster
## Made by: Priyesh Sharma

import pyperclip
import keyboard
from tkinter import *

def copy_to_programs():
    
    global listbox, window
    window = Tk()
    listbox = Listbox(window, selectmode='single', highlightthickness=2, width=30, height=30, font=('times',13))
    
    for item in buffer:
        listbox.insert(END, item)
        
    listbox.pack()

    listbox.bind('<<ListboxSelect>>', paste_to_window)

    window.mainloop()

    return

def paste_to_window(e):

    pyperclip.copy(listbox.get(int(listbox.curselection()[0])))
    print(pyperclip.paste())

    window.destroy()

    return

def copy_to_clipster():
    
    buffer.append(pyperclip.paste())
    print(buffer)

    return

shortcut_to_paste = 'ctrl+shift+c'
shortcut_to_copy = 'ctrl+c'
buffer = []

keyboard.add_hotkey(shortcut_to_paste, copy_to_programs)
keyboard.add_hotkey(shortcut_to_copy, copy_to_clipster)
