import pyttsx3
import speech_recognition as sr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
# import Emma
# from Emma import takecommand
import sys

# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)

# def takecommand1():
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Listening...")
#             r.pause_threshold = 1
#             audio = r.listen(source)#, timeout=4, phrase_time_limit=7)
        
#         try:
#             print("Recognizing...")
#             query = r.recognize_google(audio, language='en-in')
#         #     print(f"user said: {query}")

#         except Exception as e:
#             # speak("Say that again please...")
#             return "none"
#         query=query.lower()
#         return query

# def speak1(audio):
#     engine.say(audio)
#     print(audio)
#     engine.runAndWait()

def acc_info():
    with open('acc_info.txt','r') as f:
        info = f.read().split()
        email = info[0]
        password = info[1]
    return email,password

email, password = acc_info()

# speak1("what should i tweet")
# tweet=takecommand1().lower()


tweet = "Hello world, this is Emma a virtual assistant."

options = Options()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

driver.get("https://twitter.com/login")

email_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input'
login_xpath = '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div'

time.sleep(2)
driver.find_element_by_xpath(email_xpath).send_keys(email)
time.sleep(0.5)
driver.find_element_by_xpath(password_xpath).send_keys(password)
time.sleep(0.5) 
driver.find_element_by_xpath(login_xpath).click()

tweet_xpath = '//*[@id="react-root"]/div/div/div[2]/header/div/div/div/div[1]/div[3]/a/div'
message_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div'
post_xpath = '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div[3]/div/div/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]'

time.sleep(4)

driver.find_element_by_xpath(tweet_xpath).click()
time.sleep(2)
driver.find_element_by_xpath(message_xpath).send_keys(tweet)
time.sleep(2) 
driver.find_element_by_xpath(post_xpath).click()

sys.exit()