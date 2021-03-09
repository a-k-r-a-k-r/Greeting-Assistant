import os
import time
import pyttsx3
import datetime
import requests


#Functions
def get_data():
    global current_time_hour, current_time_minute, current_time_session, current_date, current_month, current_year, current_day
    today = datetime.datetime.now()
    current_time_hour = int(today.strftime("%I"))  #eg: 10
    current_time_minute = int(today.strftime("%M"))  #eg: 40
    current_time_session = today.strftime("%p")  #eg: AM
    current_date = int(today.strftime("%d")) #eg: 31
    current_month = today.strftime("%B") #eg: March
    current_year = int(today.strftime("%Y") ) #eg: 2021
    current_day = today.strftime("%A")  #eg: Sunday


def speak():
    pyttsx3.speak("{} a k r".format(greeting))    #replace it with your name
    pyttsx3.speak("Today is {} {} {} {}".format(current_day, current_month, current_date, current_year))
    time.sleep(.5)
    pyttsx3.speak("Time is {} {} {}".format(current_time_hour, current_time_minute, current_time_session))
    pyttsx3.speak("Opening your GitHub account for you")


def open_github():
    os.system("firefox www.github.com/a-k-r-a-k-r")    #replace with the url of your account


def check_net():
    try:
        if requests.get('https://8.8.8.8').ok:
            time.sleep(1)
            pyttsx3.speak("Have a nice day a k r")
            open_github()            
    except:
        time.sleep(1)
        pyttsx3.speak("Unable to open GitHub. Looks like you are offline")


get_data()

'''
    Good morning   : 00 - 11 and AM
    Good afternoon  : 12 - 2 and PM
    Good evening  :  3 - 6 and PM
    Welcome : 7 - 12 and PM
'''
if (current_time_hour < 12 and current_time_session == "AM"):
    greeting = "Good Morning"
elif (current_time_hour < 3 and current_time_session == "PM"):
    greeting = "Good Afternoon"
elif (current_time_hour < 7 and current_time_session == "PM"):
    greeting = "Good Evening"
elif (current_time_hour < 12 and current_time_session == "PM"):
    greeting = "Welcome"


speak()
check_net()      #Replace if necessary, with the function that you need