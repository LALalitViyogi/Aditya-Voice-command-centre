#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
import wikipedia
from datetime import datetime
import speech_recognition as sr
from tkinter import *
from tkinter import messagebox as mb


# In[ ]:


class Aditya:
    
    def __init__(self):
        self.win=Tk()
        self.win.geometry('450x400')
        self.win.resizable(10,10)
        self.win.title('Aditya Voice Command Center')
        self.win.configure(bg='#AD0202')
        Label(self.win, text='Viyogi Learnings', font=('times new roman',24),width=30).pack()
        Button(self.win, text='Start', font=('times new roman',14),width=15,command=self.start).place(x=140,y=100)
        Button(self.win, text='Stop', font=('times new roman',14),width=15, command= self.quitnow).place(x=140,y=200)
        self.win.mainloop()
        
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    
    def wishme(self):
        hours=int(datetime.now().time().hour)
        if (hours)<12:
            self.speak("Good morning sir, i hope you are feeing fresh")
        elif hours>12 and hours<18:
            self.speak("Good After Noon sir, Is everything ok")
        elif hours>18 and hours<21 :
            self.speak("Good Evening sir, it is perfect timings for doing work")
        elif hours>21:
            self.speak("Good Night sir,i think something is necessary")
        else:
            self.speak("It is too late for bed sir")
        self.takecommand()
        
        
    def speak(self,audio):
        self.engine.say(audio)
        self.engine.runAndWait()
    
    def takecommand(self):
        r=sr.Recognizer()
        with sr.Microphone() as source:
            self.speak("Listening now")
            r.pause_threshold=0.8
            audio=r.listen(source)
        try:
            self.speak("its working")
        except Exception as e:
            self.speak("we got an exception")
 #now we making quit now function   
    
    def quitnow(self):
        self.speak("You want me to shut down")
        quit()
    
    def start(self):
        self.wishme()

if __name__=='__main__':
    Root=Aditya()
    



# In[ ]:





# In[ ]:




