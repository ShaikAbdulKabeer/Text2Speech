#import libraries

from tkinter import *
from gtts import gTTS
from playsound import playsound
import webbrowser


################### Initialized window####################

root = Tk()
root.geometry('500x500')
root.resizable(10,10)
root.config(bg = '#E80F88')
root.title('TEXT TO SPEECH')
root.iconbitmap("text.ico")



#heading
Label(root, text = 'TEXT TO SPEECH' , fg = 'white',font='Mont 30 bold' , bg ='blue').place(x=90,y=10)
#Label(root, text ='@Shaik_Abdul_Kabeer' , font ='Opensans 15 bold', bg = 'white smoke').place(x=150,y=300)

def callback(url):
   webbrowser.open_new_tab(url)

#Create a Label to display the link
link = Label(root, text="@Shaik_Abdul_Kabeer",font=('Helveticabold', 15), fg="blue", cursor="hand2")
link.pack()
link.place(x=150,y=280)
link.bind("<Button-1>", lambda e:
callback("https://www.linkedin.com/in/shaik-abdul-kabeer-b8a9661a3/"))


#label
Label(root, text ='Enter Text', font ='Verdana 15 bold', bg ='white smoke').place(x=200,y=70)


#text variable
Msg = StringVar()


#Entry
entry_field = Entry(root,textvariable =Msg, width ='50')
entry_field.place(x=110 , y=120)


###################define function##############################

#Function to Convert Text to Speech in Python
def Text_to_speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('Audio.mp3')
    playsound('Audio.mp3')
    
    
#Function to Exit  
def Exit():
    root.destroy()

#Function to Reset  
def Reset():
    Msg.set("")

#Button
Button(root, text = "PLAY" , font = 'Verdana 15 bold', command = Text_to_speech, width =4).place(x=130, y=150)
Button(root,text = 'EXIT',font = 'Verdana 15 bold' , command = Exit, bg = 'Yellow').place(x=210,y=150)
Button(root, text = 'RESET', font='Verdana 15 bold', command = Reset).place(x=300 , y =150)


#infinite loop to run program
root.mainloop()