import pyttsx3
import requests
import speech_recognition as sr
from wikipedia.wikipedia import languages
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit as kit
import smtplib
import pyjokes
import pyautogui
import time
import instaloader
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import QTimer, QTime, QDate, Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from EmmaUI import Ui_EmmaUI
import sys
import operator
import requests
from bs4 import BeautifulSoup
import pywikihow
from pywikihow import search_wikihow
import psutil
import speedtest
import MyAlarm
import numpy as np
from os import path
from typing import Match
import face_recognition


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# rate = engine.getProperty('rate')
# print(voices[1].id)
engine.setProperty('voice', voices[1].id)
# engine.setProperty('rate',200)

# func for convert text into speech
def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()

# func for wish
def wish():
    hour = int(datetime.datetime.now().hour)

    if hour>=0 and hour<=12:
        speak("Good morning sir")
    elif hour>12 and hour<18:
        speak("Good afternoon sir")
    else:
        speak("Good evening sir")
    speak("I am Emma, your virtual assistant, how may i help you...")

# func for send email
def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('yash9871729877@gmail.com','nalayakritup0')
        server.sendmail('yash9871729877@gmail.com',to, content)
        server.close()

def rescale(cap,scale=0.25):

    h = int(cap.shape[0] * scale)
    w = int(cap.shape[1] * scale)
    
    new_dim = (w,h)
    return(cv2.resize(cap,new_dim,interpolation=cv2.INTER_CUBIC))

# for news update
def news():
    main_url = 'https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=8cbacbf7f0704e91afdc842cd2573e87'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    head=[]
    day=["Firt",'Second','Third','Fourth','Fifth']
    for ar in articles:
        head.append(ar['title'])
    for i in range (len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")


class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        speak('Hello sir')
        speak('Sorry for inconvenience... but Please wait...first I have to verify you')
        self.faceunlock()
        # self.TaskExecution()
        # self.wakeup()
        
    def wakeup(self):
        
        # self.faceunlock.cv2.waitKey(0)
        # self.faceunlock.cam.release()
        # self.faceunlock.cv2.destroyAllWindows()
        while True:
            permission = self.takecommand()
            if "wake up" in permission:
                self.TaskExecution()
            elif "goodbye" in permission  or "quit" in permission:
                speak('thanks for using me, goodbye sir')
                sys.exit()
        # self.TaskExecution()
        
    # func for take audio input from user and convert into text
    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)#, timeout=4, phrase_time_limit=7)
        
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en-in')
            print(f"user said: {query}")

        except Exception as e:
            # speak("Say that again please...")
            return "none"
        query=query.lower()
        return query

    # main function
    def TaskExecution(self):
        # pyautogui.press('esc')
        # speak('User Detected')
        wish()
        while True:
        # if 1: 
            self.query = self.takecommand().lower()
            # logic building for tasks

            if "open Notepad" in self.query or "notepad" in self.query:
                npath="C:\\WINDOWS\\system32\\notepad.exe"
                os.startfile(npath)

            elif "calculator" in self.query or "calci" in self.query:
                cpath="C:\\Windows\\System32\\calc.exe"
                os.startfile(cpath)

            elif "open command prompt" in self.query or "command prompt" in self.query or "open cmd" in self.query or "cmd" in self.query:
                cmdpath="C:\\WINDOWS\\system32\\cmd.exe"
                os.startfile(cmdpath)

            elif "open powershell" in self.query or "powershell" in self.query or "open shell" in self.query or "shell" in self.query:
                shellpath = "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe"
                os.startfile(shellpath)
            
            elif "open camera" in self.query or "camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam', img)
                    k = cv2.waitKey(50)
                    if k==27:
                        break
                cap.release()
                cv2.destroyAllWindows()
            
            elif "play music from pc" in self.query or "music from pc" in self.query:
                music_dir = "C:\\Users\\Anonymous\\Downloads\\Music"
                songs = os.listdir(music_dir)
                rd = random.choice(songs)
                for song in songs:
                    if song.endswith('.mp3'):
                        os.startfile(os.path.join(music_dir, song))

            elif 'video from pc' in self.query or "pc video" in self.query:
                speak("ok i am playing videos")
                video_dir = 'C:\\Users\\Anonymous\\Downloads\\Video'
                videos = os.listdir(music_dir)
                os.startfile(os.path.join(video_dir,videos[0]))
            
            elif "ip address" in self.query or "tell my ip" in self.query or "what is my ip" in self.query:
                ip = get('https://api.ipify.org').text
                speak(f"your IP address is {ip}")

            # elif "wikipedia" in self.query:
            #     speak("searching details....Wait")
            #     query = query.replace("wikipedia","")
            #     results = wikipedia.summary(query,sentences=2)
            #     speak("according to wikipedia...")            
            #     speak(results)

            elif 'wikipedia' in self.query:
                speak('about what sir?')
                topic = self.takecommand().lower()
                webbrowser.open(f'https://en.wikipedia.org/wiki/{topic}')

            
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
                speak("opening youtube")
            
            elif 'favourite song' in self.query:
                webbrowser.open("https://www.youtube.com/watch?v=50VNCymT-Cs")
                speak("enjoy your song sir")

            elif 'cheer me up' in self.query:
                webbrowser.open('https://www.youtube.com/watch?v=Xs-HbHCcK58')
                #time.sleep(5)
                speak('hope you, and your friends, like it')

            elif 'desi' in self.query:
                webbrowser.open('https://www.youtube.com/watch?v=iiQmg8Sldu8&list=PL4XU8WPrm5gvqfoBIGSLZZ3QUHuvsG9P9&index=2')
                #time.sleep(5)
            
            elif 'slow song' in self.query or 'sad song' in self.query or 'soft song' in self.query or 'play something nice' in self.query:
                webbrowser.open('https://www.youtube.com/watch?v=HRpqS9d2f74')
                # time.sleep(5.0)
                speak('for me, its a best song ever...')

            elif 'mood' in self.query:
                
                default = 'tell me sir, how you feel right now...'
                speak(default)
                mc = self.takecommand().lower()
                try:
                    if 'sad' in mc:
                        webbrowser.open('https://www.youtube.com/watch?v=50VNCymT-Cs')
                    elif 'cheated' in mc:
                        webbrowser.open('https://www.youtube.com/watch?v=Xv0DlKncjBI')
                    elif 'alone' in mc:
                        webbrowser.open('youtube.com/watch?v=lN1m7zLBbSU')
                    elif "don't know" in mc:
                        webbrowser.open('https://www.youtube.com/watch?v=Xs-HbHCcK58')
                        speak('ok,you can enjoy this song in every mood')
                    elif 'nothing leave' in mc:
                        speak('ok fine...')
                        break
                except Exception as e:
                    # time.sleep(5.0)
                    speak("i didn't any response, try me later")
                    break
                    

            elif "play song on youtube" in self.query:
                speak("Which song sir...")
                ysong = self.takecommand().lower()
                kit.playonyt(f"{ysong}")
            
            elif "bollywood romantic" in self.query or 'romantic bollywood' in self.query:
                webbrowser.open('https://open.spotify.com/playlist/5K8TyrQT0TSK8ARLApPDh2')
                
            elif 'open github' in self.query:
                webbrowser.open("https://www.github.com")
                speak("opening github")  

            elif 'open facebook' in self.query:
                webbrowser.open("https://www.facebook.com")
                speak("opening facebook")      

            elif 'open instagram' in self.query:
                webbrowser.open("https://www.instagram.com")
                speak("opening instagram")    

            elif 'search please' in self.query:
                speak("what should i search for you, sir")
                gcm = self.takecommand().lower()
                webbrowser.open(f"{gcm}")
                speak("your result sir...")
                
            elif 'open google' in self.query:
                webbrowser.open("https://www.google.com")
                speak("opening google")
            
            elif 'open chrome' in self.query:
                chpath="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
                os.startfile(chpath)
                speak("opening chrome")


            elif 'open yahoo' in self.query:
                webbrowser.open("https://www.yahoo.com")
                speak("opening yahoo")

            elif 'open stackoverflow' in self.query:
                webbrowser.open("www.stackoverflow.com")
                speak("opening stackoverflow")
                
            elif 'open gmail' in self.query:
                webbrowser.open("https://mail.google.com")
                speak("opening google mail") 
            
            elif "look who's here" in self.query or "meet someone" in self.query:
                speak('who?')
                person = self.takecommand()
                speak(f"hello {person}, nice to meet you")

            elif 'open snapdeal' in self.query:
                webbrowser.open("https://www.snapdeal.com") 
                speak("opening snapdeal")  
                
            elif 'open amazon' in self.query or 'shop online' in self.query :
                webbrowser.open("https://www.amazon.com")
                speak("opening amazon")
            
            elif "open apni dukaan" in self.query:
                webbrowser.open("https://www.amazon.com")
                speak("here's your apni dukaan sir, haahaa")

            elif 'open flipkart' in self.query:
                webbrowser.open("https://www.flipkart.com")
                speak("opening flipkart")   

            elif 'open ebay' in self.query:
                webbrowser.open("https://www.ebay.com")
                speak("opening ebay")
            
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)
            
            elif "shutdown the system" in self.query:
                speak('are you sure, wou want to turn the system off?')
                shut = self.takecommand()
                if 'yes' in shut or 'yeah' in shut:
                    os.system("shutdown /s /t 5")
                else:
                    break

            elif "restart the system" in self.query:
                speak('are you sure, wou want to restart the system ? but after that you have to start me again. ')
                restart = self.takecommand()
                if 'yes' in restart or 'yeah' in restart:
                    os.system("shutdown /r /t 5")
                else:
                    break

            elif "sleep the system" in self.query:
                speak ('you want to turn the system in sleep mode?')
                sleep = self.takecommand()
                if 'yes' in sleep or 'yeah' in sleep:
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
                else:
                    break
            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                #time.sleep(1)
                pyautogui.keyUp("alt")
            
            elif "tell me news" in self.query or "today's news" in self.query:
                speak("Please wait a minute sir, ")
                print("fetching the news...")
                news()
            
            elif "send message on whatsapp" in self.query:
                speak("To whom...give me a number")
                number = self.takecommand().lower()

                speak("Tell the msg")
                msg = self.takecommand().lower()

                # thour = int(datetime.datetime.now().hour)
                # tmin = int(datetime.datetime.now().minute)
                # kit.sendwhatmsg(f"+91{number}",f"{msg}",int(f"{thour}"),int(f"{tmin}")+2)
                kit.sendwhatmsg_instantly(f"+91{number}",f"{msg}")
            
            elif "send mail" in self.query:
                try:
                    speak("what should i say?")
                    content = self.takecommand().lower()
                    speak("to whom, give me an email id")
                    to = self.takecommand().lower()
                    sendEmail(to,content)
                    speak("Email has been sent sir")
                
                except Exception as e:
                    print(e)
            
            elif "tweet for me" in self.query or "tweet" in self.query:
                # speak("What should i tweet")
                # tcm=self.takecommand().lower()
                os.startfile('C:/Users/Anonymous/Desktop/Twitterbot.py')    
                #time.sleep(60)
                
            elif "wait" in self.query:
                speak("For how long")
                st = self.takecommand().lower()
                try:
                    time.sleep(int(st))
                except:
                    continue

            # to close an application     
            elif (f"close the program") in self.query or "close it" in self.query:
                speak("which program sir")
                app=self.takecommand().lower()
                speak(f"okay sir, closing {app}")
                os.system(f"taskkill /f /im {app}.exe")

            # simple calculator
            elif 'calculate for me' in self.query or 'do some calculations' in self.query:
                r = sr.Recognizer()
                with sr.Microphone() as source:
                    speak("for now i can do just simple calculations, so what you want to calculate...")
                    print('listening....')
                    r.adjust_for_ambient_noise(source)
                    audio = r.listen(source)
                my_string=r.recognize_google(audio)
                print(my_string)
                def get_operator_fn(op):
                    return{
                        '+' : operator.add,
                        '-' : operator.sub,
                        'x' : operator.mul,
                        'divided' : operator.__truediv__,
                        }[op]
                def eval_binary_expr(op1, oper, op2):
                    op1,op2 = int(op1), int(op2)
                    return get_operator_fn(oper)(op1, op2)
                speak("Your answer is ")
                speak(eval_binary_expr(*(my_string.split())))


            # to find my current location
            elif "where I am " in self.query or 'where we are' in self.query or 'my location' in self.query:
                speak("wait sir, let me check")
                try:
                    ipADD = requests.get('https://api.ipify.org').text
                    print(ipADD)
                    url = 'https://get.geojs.io/v1/ip/geo/'+ipADD+'.json'
                    geo_requests = requests.get(url)
                    geo_data = geo_requests.json()
                    city = geo_data['city']
                    state = geo_data['region']
                    country = geo_data['country']
                    speak(f"sir i am not sure, but i think we are in {city} city, of {state}, of {country} country.")
                except Exception as e:
                    speak("Soory sri, Due to network problem i am not not able to find our location.")
            
            elif 'ok' in self.query or 'ok thanks' in self.query:
                speak('my pleasure, anything else sir?')

            # to check someone instagram profile and download profile pic
            elif "instagram profile" in self.query or "profile on instagram" in self.query:
                speak("sir please enter the user name correctly.")
                name = input("Enter username here :- ")
                webbrowser.open(f"www.instagram.com/{name}")
                speak(f"sir here is the profile of the user {name}")
                #time.sleep(5)
                speak('sir would you like to download profile picture of this account.')
                condition = self.takecommand().lower()
                if 'yes' in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_only=True)
                    speak('i am done sir, profile picture is saved in our folder.')
                else:
                    pass
            
            # to take screenshot
            elif "take screenshot" in self.query or 'take a screenshot' in self.query:
                speak('sir, please tell me the name for tihs screenshot')
                name = self.takecommand().lower()
                speak('please sir hold the screen for few seconds, i am talking screenshot')
                #time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("i am done sir.")

            # for temperature
            elif "temperature" in self.query:
                speak('tell me the location')
                search = self.takecommand()
                loc = f'temperature in {search}'
                url = f"https://www.google.com/search?q='{loc}'"
                r = requests.get(url)
                data = BeautifulSoup(r.text,"html.parser")
                temp = data.find("div",class_="BNeawe").text
                speak(f"current {loc} is {temp}")
            
            # to check internet speed
            elif "internet speed" in self.query:
                try:
                    speak('wait sir i am calculate the speed for you...')
                    st = speedtest.Speedtest()
                    dl = st.download()
                    dl1 = round((int(dl))/8388608)
                    up = st.upload()
                    up1 = round((int(up))/8388608)
                    speak(f"sir we have {dl1} mega byte per second downloading speed and {up1} mega byte per second uploading speed")
                except:
                    speak('you have no internet connection')

            # to control voulme
            elif 'volume up' in self.query or 'increase the volume' in self.query:
                pyautogui.press('volumeup')

            elif 'volume down' in self.query or 'decrease the volume' in self.query:
                pyautogui.press('volumedown')

            elif 'volume mute' in self.query or 'mute the system' in self.query:
                pyautogui.press('volumemute')

            # ask anything
            elif 'activate how to do mode' in self.query:
                speak('How to do mode is activated')
                while True:
                    speak('please tell me what you want to know')
                    how = self.takecommand()
                    try:
                        if 'exit' in how or 'close' in how or 'deactivate how to do mode' in how:
                            speak("okay sir, how to do mode is deactivated")
                            break
                        else:
                            max_results = 1
                            how_to = search_wikihow(how, max_results)
                            assert len(how_to) == 1
                            # how_to[0].print()
                            speak(how_to[0].summary)
                    except Exception as e:
                        speak('Sorry sir, i am not able to find this')
 
            elif 'tell me a story' in self.query:
                speak('Years ago when I was backpacking through western Europe I was just outside Barcelona hiking in the foothills of Mount Tibidabo, I was at the end of this path and I came to a clearing, there was a very secluded lake and there were tall trees all around, it was dead silent and across the lake I saw a beautiful woman bathing herself but she was crying...')

            # to hide files
            elif "private file" in self.query or 'hide files' in self.query or 'hidden files' in self.query:
                speak('you want to hide it or make it visible for everyone?')
                condition = self.takecommand().lower()
                if 'hide' in condition or 'private' in condition:
                    os.system('attrib +h /s /d')
                    speak('done sir')
                elif 'public' in condition or 'unhide' in condition:
                    os.system('attrib -h /s /d')
                    speak('now everyone can see it')
                elif 'nothing' in condition or 'leave it' in condition:
                    speak('fine sir...')
            
            # bettery

            elif "how much power left" in self.query or "how much power we have" in self.query or 'battery' in self.query:
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"sir our system have {percentage} percent battery")

            # alarm
            elif 'alarm' in self.query:
                speak('sir please tell me the time to set alarm. for example, set alarm to 5:30 am')
                tt = self.takecommand()
                tt = tt.replace('set alarm to ','')
                tt = tt.replace('.','')
                tt = tt.upper()
                import MyAlarm
                MyAlarm.alarm(tt)
            
            # activate mobile camera
            elif 'mobile camera' in self.query or 'mobile cam' in self.query:
                import urllib.request
                import cv2
                import numpy as np
                import time
                URL = 'http://192.168.0.190:8080/shot.jpg'
                while True:
                    img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()),dtype=np.uint8)
                    img = cv2.imdecode(img_arr,-1)
                    cv2.imshow('IPWebcam',img)
                    q = cv2.waitKey(1)
                    if q == 27:
                        break;
                cv2.destroyAllWindows()
            
# *********************************************************************************************************************

            elif "what\'s up" in self.query or 'how are you' in self.query:
                stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy','i am okey ! How are you']
                ans_q = random.choice(stMsgs)
                speak(ans_q)  
                ans_take_from_user_how_are_you = self.takecommand()
                if 'fine' in ans_take_from_user_how_are_you or 'happy' in ans_take_from_user_how_are_you or 'okey' in ans_take_from_user_how_are_you:
                    speak('okey..')  
                elif 'not' in ans_take_from_user_how_are_you or 'sad' in ans_take_from_user_how_are_you or 'upset' in ans_take_from_user_how_are_you:
                    speak('oh sorry..')  
            
            elif 'make you' in self.query or 'created you' in self.query or 'develop you' in self.query:
                ans_m = " For your information Yash Created me ! I give Lot of Thannks to Him "
                speak(ans_m)
            
            elif "who are you" in self.query or "about you" in self.query or "your details" in self.query:
                about = "I am Emma an A.I. based computer program but i can help you lot like a your close friend !  Simple try me to give simple command !  i can also entertain you ! ok Lets Start "
                speak(about)
            
            elif "hello" in self.query or "hello Emma" in self.query:
                hel = "Hello Yash Sir ! How May i Help you.."
                speak(hel)
            
            elif "your name" in self.query or "sweet name" in self.query:
                na_me = "Thanks for Asking, my name my self ! Emma"  
                speak(na_me)
            
            elif "your feeling" in self.query or "how you feel" in self.query:
                speak("feeling Very sweet after meeting with you") 
            
            elif self.query == 'none':
                continue 
            
            elif 'exit' in self.query or 'abort' in self.query or 'stop' in self.query or 'quit' in self.query or 'goodbye' in self.query:
                ex_exit = 'Nice to meet you sir, bye.'
                speak(ex_exit)
                exit()  
            
            elif 'good' in self.query or 'nice' in self.query or 'perfect' in self.query:
                speak("that's great to hear you.")
            
            elif 'thank you' in self.query or 'thanks' in self.query:
                speak('its my pleasure sir...')
            
            elif 'shut your mouth' in self.query:
                speak('you are so rude...bye')
                exit()

            elif 'f*** off' in self.query:
                ex_exit2 = 'If you ever, ever say this again, I am gonna corrupt your system....., ok, and i hate you, am going, bye'
                speak(ex_exit2)
                exit()
            
            elif 'you can sleep' in self.query or 'sleep' in self.query or 'take a nap' in self.query:
                speak('okay sir, i am going to sleep you can call me anytime')
                self.wakeup()

            else:
                while True:
                    speak("sorry! i cant understand but can i search it from internet to give you an answer?")
                    final = self.takecommand().lower()
                    try:
                        if 'yes' in final or 'yes please' in final :
                            temp = self.query.replace(' ','+')
                            g_url="https://www.google.com/search?q="    
                            res_g="Here's your search sir" 
                            speak(res_g)
                            webbrowser.open(g_url+temp)
                        else:
                            speak('ok fine...')
                            break
                    except Exception as e:
                        speak('i cant recieve any response from your side, try again....')


##########################################################################################################

    def faceunlock(self):

        webcam = False
        path = 'image/user.jpg'
        # pathTest = 'image/user.jpg'
        cap = cv2.VideoCapture(0) # to read video
        cap.set(3,640)
        cap.set(4,480)

        while True:
            speak('Please look at the camera...')
            if webcam: success, imgTest = cap.read()
            else:
                speak('sorry ...i think .. your camera is not working... please check it and start me again')
                cv2.destroyAllWindows()

            imgSample = face_recognition.load_image_file(path)
            imgSample = rescale(imgSample)
            imgSample = cv2.cvtColor(imgSample,cv2.COLOR_BGR2RGB)

            # imgTest = face_recognition.load_image_file('Images/Elon Test.jpg')
            # imgTest = face_recognition.load_image_file('Images/Bill Gates.jpg')
            imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)

            faceLoc = face_recognition.face_locations(imgSample)[0]
            encodeElon = face_recognition.face_encodings(imgSample)[0]
            cv2.rectangle(imgSample,(faceLoc[3],faceLoc[0]),(faceLoc[1],faceLoc[2]),(255,0,255),2)

            faceLocTest = face_recognition.face_locations(imgTest)[0]
            encodeTest = face_recognition.face_encodings(imgTest)[0]
            cv2.rectangle(imgTest,(faceLocTest[3],faceLocTest[0]),(faceLocTest[1],faceLocTest[2]),(255,0,255),2)

            results = face_recognition.compare_faces([encodeElon],encodeTest)
            faceDis = face_recognition.face_distance([encodeElon],encodeTest)
            # print(results,faceDis)
            # print(type(results))
            results = ' '.join(map(str,results))
            print(results)
            # print(type(results))
            if results == 'True':
                results = 'Match'
                cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,	(0,255, 0),2)
                # cv2.waitKey()
                # self.wakeup()
                speak('...Sorry for the delay...')
                speak('Authentication Successfull')
                self.TaskExecution()
                
            else:
                results = 'Un-Match'
                cv2.putText(imgTest,f'{results} {round(faceDis[0],2)}',(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)
                # cv2.waitKey(0)
                speak('user authentication is failed')
                speak('please close the camera window')
                # cv2.waitKey(1)
                # cv2.destroyAllWindows()
                # cv2.imshow("Sample",imgSample)
                cv2.imshow("Test",imgTest)
            
            cv2.waitKey(0)


############################################################################################################                        

startExecution = MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_EmmaUI()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)

    def startTask(self):
        self.ui.movie = QtGui.QMovie("satoshi-arakawa-hud.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie = QtGui.QMovie("EmmaUI1/ZI8K1x.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer = QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()
    
    def showTime(self):
        current_time = QTime.currentTime()
        current_date = QDate.currentDate()
        label_time = current_time.toString('hh:mm:ss')
        label_date = current_date.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_time)
        self.ui.textBrowser_2.setText(label_date)

app = QApplication(sys.argv)
Emma = Main()
Emma.show()
exit(app.exec_())

        

        
        

        




