import pyttsx3
import PyPDF2
import tkinter as tk
from tkinter import *
from tkinter import filedialog

root = Tk()#creating GUI window
root.geometry('300x250')#geometry of window
root.title("Browse E-book")

Label(root, text="AUDIOBOOK",font= "Calibri 20", padx= 10, pady= 10).pack()
pathlabel = Label(root)
pathlabel.pack()

# BROWSING file through my PC
def browse():
    global fileReader
    global file
    file = filedialog.askopenfilename(title='Select e-book', filetype= (('PDF Files',"*.pdf"), ('All Files','*')))
    fileReader= PyPDF2.PdfReader(open(file,'rb'))
    pathlabel.config(text = file)

global speaker
speaker = pyttsx3.init() #initializing an instance

voices = speaker.getProperty('voices')#get available voices

# Male Voice
def male():
    if var1.get()== 0:
       speaker.setProperty('voice', voices[0].id)

# Female Voice
def female():
    if var2.get()== 1:
        speaker.setProperty('voice', voices[1].id)

# READING & SAVING the file
def save():
    for page_num in range(len(fileReader.pages)):
        text = fileReader.pages[page_num].extract_text()
        speaker.say(text)
        speaker.runAndWait()
    speaker.stop()
    
    speaker.save_to_file(text, 'audio.mp3')
    speaker.runAndWait()
    Label(root, text= "The Audio File is Saved").pack()

# Button for Browsing
Button(root, text= "Browse a File", pady= 5, command= browse).pack()

# Checkbuttons for deciding male or female voice
var1= IntVar()
Checkbutton(root, text= "Male Voice", onvalue= 0, offvalue= 10, variable= var1, command= male).pack()
var2= IntVar()
Checkbutton(root, text= "Female Voice", onvalue= 1, offvalue= 10, variable= var2, command= female).pack()

# Button for Reading & Saving the audiobook
Button(root, text= "Create and Save the Audio File", pady= 5, command= save).pack()

root.mainloop()