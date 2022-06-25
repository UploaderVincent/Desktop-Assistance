from tkinter import *
import speech_recognition as sr
import webbrowser
import pyttsx3
from datetime import datetime
import subprocess


root = Tk()
root.geometry("500x500")
root.configure(background="Crimson")

label=Label(root,text="Welcome To Your Personal Desktop Assistant(It Will Do What You Say)",bg="Crimson",font=("Bahnschrift Light",15,"bold"))
label.place(relx=0.5,rely=0.1,anchor=CENTER)

text_to_speech=pyttsx3.init()

def speak(audio):
    text_to_speech.say(audio)
    text_to_speech.runAndWait()

def r_audio():
    speak("How can I help you..?")
    speech_recognisor= sr.Recognizer()
    with sr.Microphone() as source:
        audio= speech_recognisor.listen(source)
        voice_data=''
        try:
            voice_data=   speech_recognisor.recognize_google(audio, language='en-in')

        except sr.UnknownValueError:
            print('Please repeat I did not get that')
            speak("Please repeat I did not get that")

        respond(voice_data)


def respond(voice_data):
    voice_data = voice_data.lower()
    print(voice_data)
    if "name" in voice_data:
        speak("My name is Jarvis")
        print('My name is Jarvis')

    if "time" in voice_data:
        speak("Current Time is")
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(current_time)
        print(current_time)

        if "search" in voice_data:
            speak("Opening Google")
            print("Opening Google")
            webbrowser.get().open("https://www.google.com/")

        if "videos" in voice_data:
            speak("Opening YouTube")
            print("Opening YouTube")
            webbrowser.get().open("https://www.youtube.com/")

        if "text editor" in voice_data:
            speak("Opening the app")
            print("Opening the app")
            subprocess.Popen(["notepad.exe"])


btn= Button(root, text="Start",bg="purple", fg="white", padx=10, pady=3,font=("Arial",11, "bold"), relief=FLAT, command=r_audio)
btn.place(relx=0.5,rely=0.5,anchor=CENTER)
        
    



root.mainloop()
        
