import pyttsx3
# from chat import client,server
# import struct
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import webbrowser
import os        #for using os files
import smtplib   #for gmail
from twilio.rest import Client 
from pygame import mixer
# import ctypes
new=2

engine=pyttsx3.init('sapi5')
emailDictonary={
    "shilpi":"",
    "sachin":"sachinkumar.kumar28@gmail.com",
    "shivam":""
}
voices=engine.getProperty('voices')
print(voices)
print(voices[1].id)

engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',185)  

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendMessage():
    account_sid = ''
    auth_token = ''
    client = Client(account_sid, auth_token)
    #speak("whom do u want to send message")

    message = client.messages .create(body = takeCommand(), from_='', to ='+') 
    print(message.sid) 
  

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif(hour>=12 and hour<18):
        speak("Good AfterNoon")
    # elif(hour>=18 and hour<20):
    #     speak("Good Evening")
    else:
        speak("Good Evening")

    speak("I am Jarvis sir. Please Tell me How may i help you")

def takeCommand():
    # it takes microphone input from user and return string output
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.adjust_for_ambient_noise(source) #remove noise 
        r.energy_threshold=400 #isilie use kia hai agr ghr mai noise hai to bhi awaj sune
        r.pause_threshold = 1 #ye isilie hai taki hum 1 second ka pause leske bich mai
        audio=r.listen(source)
    
    try:
        print("Recognizing.....")
        query=r.recognize_google(audio,language='en-in')
        print(f"user said:{query}\n")
    except Exception as e:
        # print(e)->printing error

        print("Say that again please....")
        speak("Say that again please....")
        return "None" 

    return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com', 587) 
    server.ehlo() 
    server.starttls() 
      
    # Enable low security in gmail 
    server.login('sachinkumar.kumar28@gmail.com','') 
    server.sendmail('sachinkumar.kumar28@gmail.com', to, content) 
    server.close() 
  

if __name__ == "__main__":
    
# For 32 bit it will return 32 and for 64 bit it will return 64
# import struct
    # print(struct.calcsize("P") * 8)

    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia..")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
        # elif 'chat' in query:
        #     client
        elif 'open youtube' in query:
            # webbrowser.open('youtube.com')
            webbrowser.open("https://www.youtube.com/",new=new)
            # webbrowser.Chrome.open(youtube.com,url=https://www.youtube.com/)
            # webbrowser.Chrome('youtube.com')
        elif 'open google' in query:
            webbrowser.open('google.com')
        elif 'message' in query:
            sendMessage()
        elif 'open stack overflow' in query:
            webbrowser.open('https://stackoverflow.com/',new=new)
        
        elif 'play music' in query:
            speak("which music you want me to play sachin? ")
            playMusic=takeCommand().lower()
            playMusic=playMusic.replace("play ","")
            music_dir="G:\\MyMusics"
            songs=os.listdir(music_dir)
            print(songs)
            for i in songs:
                if playMusic in i.lower():
                    speak("playing your music")
                    mixer.init()
                    mixer.music.load(os.path.join(music_dir,i))
                    mixer.music.play()
                    # os.startfile()
                    # print(filedes)
                    
        elif 'pause music' in query:
            mixer.music.pause()
        elif 'play again' in query:
            mixer.music.unpause()
        elif 'stop music' in query:
            mixer.music.stop()
            
        
        elif 'the time' in query:
            time = str(datetime.datetime.now()) 
      # the time will be displayed like this "2020-06-05 17:50:14.582630" 
    # nd then after slicing we can get time 
            print(time) 
            hour = time[11:13] 
            min = time[14:16] 
            speak(f"The time is sir {hour} hours and {min} minutes")
        # elif 'open code' in query:
        elif 'introduction of debate system' in query:
            speak("""Debate is a process that involves formal discussion on a particular topic. In a debate, opposing arguments are put forward to argue for opposing viewpoints. Debate occurs in public meetings, academic institutions, and legislative assemblies. It is a formal type of discussion, often with a moderator and an audience, in addition to the debate participants.Logical consistency, factual accuracy and some degree of emotional appeal to the audience are elements in debating, where one side often prevails over the other party by presenting a superior context or framework of the issue.
             In a formal debating contest, there are rules for participants to discuss and decide on differences, 
             within a framework defining how they will do it.""")
        elif 'open debate system' in query:
            speak("opening Debate system. Please wait")
            chatSystempath="G:\\Chat-system-project\\server.py"
            os.startfile(chatSystempath)
        # elif 'first client' in query:
            # speak("opening Debate system. Please wait")
            chatSystempath="G:\\Chat-system-project\\client.py"
            os.startfile(chatSystempath)
            chatSystempath="G:\\Chat-system-project\\client2.py"
            os.startfile(chatSystempath)
        elif 'open code' in query:
            speak("opening Vs code")
            vscodePath="C:\\Users\\Sachin Kumar\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(vscodePath)
        
        elif 'send email' in query or 'send mail' in query:
            try:
                speak("whom do you want to send mail say sir ?")
                content1=takeCommand().lower()
                if content1 in emailDictonary:
                    speak("sending your mail to"+content1)
                to=emailDictonary[content1]
                speak("what should i say sir ?")
                content=takeCommand()
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry Boss. This enail is not available")
        
                

        elif "what is" in query or "who is" in query: 
              
            # Use the same API key  
            # that we have generated earlier 
            client = wolframalpha.Client("") 
            query=query.replace("what is","") or query.replace("who is","")
            res = client.query(query) 
              
            try: 
                print (next(res.results).text) 
                speak (next(res.results).text) 
            except StopIteration: 
                print ("No results") 
                 
        
        elif 'artifical intelligence' in query:
            speak("artifical intelligence")
        
        elif 'thank you' in query or 'thanks' in query:

            speak("Never mind Boss")
        
        elif 'is love' in query: 
            speak("It is 7th sense that destroy all other senses") 

        elif 'how are you' in query: 
            speak("I am good sir. Thanks to you")
  
        elif "who are you" in query: 
            speak("I am your virtual assistant. created by sachin") 
  
        elif 'reason for you' in query: 
            speak("I was created as a Minor project by Sachin") 
        
        elif "who i am" in query: 
            speak("If you talk then definately your human.") 
  
        
        elif "why you came to world" in query: 
            speak("Thanks to Sachin. I cannot tell you more. It's a secret")
        
        
        elif 'rest' in query:
            speak("see you soon boss. Bye-Bye")
            engine.stop()
            exit()

            
