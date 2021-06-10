from tkinter import *
from lyrics_extractor import SongLyrics
import os
from details import GCS_API_KEY
from details import GCS_ENGINE_ID
def appenfile(fname,content):
    f=open(fname,"w+")
    f.write(content)
    f.close()
    os.startfile(fname)
def get_lyrics():
    extract_lyrics = SongLyrics(str(GCS_API_KEY),str(GCS_ENGINE_ID))
    s=e.get()
    temp = extract_lyrics.get_lyrics(str(s))
    result = temp['lyrics']
    appenfile(('%s.txt'%(e.get().title())),result)
master = Tk()
master.configure(bg='light grey')
Label(master, text="Enter name of song and artist: ",bg="light grey").grid(row=0, sticky=W)
e = Entry(master, width=50)
e.grid(row=0, column=1)
b = Button(master, text="Show",command=lambda:[get_lyrics()], bg="Blue")
b.grid(row=0, column=2, columnspan=2,rowspan=2, padx=5, pady=5,)
mainloop()
