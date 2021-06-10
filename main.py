# import modules 
from tkinter import *
from lyrics_extractor import SongLyrics 
import os
from details import API
from details import ENGINE_ID
# user defined funtion 
def get_lyrics(): 
    global result
    global s
    extract_lyrics = SongLyrics(API,ENGINE_ID) 
    s=e.get()
    temp = extract_lyrics.get_lyrics(str(s)) 
    result = temp['lyrics']
def appenfile(fname,content):
    f=open(fname,"w+")
    f.write(content)
    f.close()
    os.startfile(fname)
# object of tkinter 
# and background set to light grey 
master = Tk() 
master.configure(bg='light grey') 
# Variable Classes in tkinter 
# Creating label for each information 
# name using widget Label 
Label(master, text="Enter name of song and artist: ", 
    bg="light grey").grid(row=0, sticky=W) 
# Creating lebel for class variable 
# name using widget Entry 
e = Entry(master, width=50) 
e.grid(row=0, column=1) 
# creating a button using the widget 
b = Button(master, text="Show", 
        command=lambda:[get_lyrics(),appenfile('%s.txt'%e.get().title(),res)], bg="Blue") 
b.grid(row=0, column=2, columnspan=2, 
    rowspan=2, padx=5, pady=5,) 
mainloop()
