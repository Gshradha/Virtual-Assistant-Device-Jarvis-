import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import pyaudio
import os
import smtplib
import subprocess as sp

 

engine =pyttsx3 .init('sapi5')
voices= engine.getProperty('voices')
#print(voices[1].id)
engine.setProperty('voices',voices[0].id)
   
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("hello,good morning!")
    elif(hour>12 and hour<18):
        speak("good afternoon")
    else:
        speak('good evening')
    speak("I am jarvis  ,please tell me how can  i help u?") 


def takecommand():
    ''' it takes microphone input from the user and return string output '''
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("...listening")
        r.pause_thresold =2
        r.energy_threshold=100
        audio = r.listen(source)
    try:
        print("recognizing...")  
        query=r.recognize_google(audio, language='en_in')  
        print(f"user said: {query}\n")

    except Exception as e:
         print("say that again please..")
         return "None"
    return query 

if __name__== "__main__":
    wishme()
    while True:
     query=takecommand().lower()
     #logic for exceuting tasks based on query

     if 'wikipedia'  in query:
          print('searching wikipedia...')
          query=query.replace("wikipedai","")
          results=wikipedia.summary(query,sentences=2)
          speak("according to wikipedia..")
          print(results)
          speak(results)
     elif 'open youtube' in query:
          webbrowser.open("youtube.com")

     elif 'live cricket score' in query:
         webbrowser.open("https://www.cricbuzz.com/cricket-match/live-scores")    

     elif 'open google' in query:
         webbrowser.open("google.com")
     elif 'open cricbuzz' in query:
         webbrowser.open("cricbuzz.com")      

     elif 'stack overflow' in query:
         webbrowser.open("stackoverflow.com") 
      
     elif 'the time' in query:
         strtime= datetime.datetime.now().strftime("%H:%M:%S")
         print(strtime)
         speak(f"madam ,the time is:{strtime}") 

     elif 'play music'in query:
         music_dir='C:\\Users\HP\Desktop\song'
         song=os.listdir(music_dir)
         print(song)
         os.startfile(os.path.join (music_dir,song[0]))
     elif 'open visual code'  in query:
         codePath="C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
         os.startfile(codePath) 
     elif 'who is jarvis' in query:
         speak('jarvis is an artifical intelligence device, jarvis want love.')
         print('jarvis is an artifical intelligence device, jarvis want love.')

     elif 'open notepad' in query:
         programName="notepad.exe"
         filename="file.tet"
         sp.Popen([programName,filename])
     elif 'open facebook' in query:
         webbrowser.open('https://www.facebook.com/') 
     
     elif 'open lms' in query:
        webbrowser.open('https://lms.itmgoi.in/')
    

     elif 'jarvis escape' in query:
         speak('thanku so much.')
         exit()
    

























         
            
     
    
     










  