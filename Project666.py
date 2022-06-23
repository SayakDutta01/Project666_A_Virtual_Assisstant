from tkinter import *
import cv2
import PIL.Image, PIL.ImageTk
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import pyjokes
import smtplib
import psutil
import roman
import keyboard
from PIL import Image
import pyautogui
import requests
from requests import get
from bs4 import BeautifulSoup
import sys
import time

numbers = {'hundred': 100, 'thousand': 1000, 'lakh': 100000}
a = {'name': 'your email'}
engine = pyttsx3.init('sapi5')
#print(voices[5].id)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

window = Tk()

global var
global var1

var = StringVar()
var1 = StringVar()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def sendemail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('email id', 'password')  # email id - use any email id whose security/privacy is off
    server.sendmail('email id', to, content)
    server.close()


def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <= 12:
        var.set("Good Morning Sir !")
        window.update()
        speak("Good Morning Sir!")
    elif hour >= 12 and hour <= 18:
        var.set("Good Afternoon Sir!")
        window.update()
        speak("Good Afternoon Sir!")
    else:
        var.set("Good Evening Sir!")
        window.update()
        speak("Good Evening Sir!")
    strtime = datetime.datetime.now().strftime("%I:%M:%S %p")
    var.set(f"Its {strtime}")
    window.update()
    speak(f"Its {strtime}")
    var.set("Myself Project666, a personal digital assistant. Please tell me how can I help you !")
    window.update()
    speak("Myself Project666, a personal digital assistant. please tell me how can i help you !")


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        var.set("Listening...")
        window.update()
        print("Listening...")
        r.pause_threshold = 1
        r.energy_threshold = 400
        audio = r.listen(source)
    try:
        var.set("Recognizing...")
        window.update()
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
    except Exception:
        var.set("Press Speak to execute commands")
        print("Say that again please...")
        return "None"
    var1.set(query)
    window.update()
    return query


def followmycommand():
    btn0['state'] = 'normal'
    btn2['state'] = 'normal'
    btn3['state'] = 'normal'
    btn4['state'] = 'normal'
    btn5['state'] = 'normal'
    btn6['state'] = 'normal'

    btn0.configure(bg='orange')
    btn1.configure(bg='orange')
    btn2.configure(bg='orange')
    btn3.configure(bg='orange')
    btn4.configure(bg='orange')
    btn5.configure(bg='orange')
    btn6.configure(bg='orange')

    query = takeCommand().lower()

    if 'exit' in query:
        var.set("Bye sir !, Have a nice day.")
        btn1.configure(bg='#5C85FB')
        btn2['state'] = 'normal'
        btn0['state'] = 'normal'
        window.update()
        speak("Bye sir !, Have a nice day.")
        sys.exit()

    # elif 'what is' in query:
    #     if 'open wikipedia' in query:
    #         webbrowser.open_new_tab("https://www.wikipedia.org")
    #     else:
    #         try:
    #             speak("searching sir")
    #             query = query.replace("what is", "")
    #             results = wikipedia.summary(query, sentences=1)
    #             var.set(results)
    #             window.update()
    #             speak(results)
    #         except Exception as e:
    #             var.set('sorry sir could not find any results')
    #             window.update()
    #             speak('sorry sir could not find any results')
    elif "open wikipedia" in query:
        speak("Searching wikipedia.....")
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=3)
        speak("According to wikipedia")
        speak(results)

    elif 'search in google about' in query:
        var.set("This is what I found on google")
        window.update()
        speak('This is what I found on google')
        query = query.replace("search in google about", "")
        webbrowser.open_new_tab(f"https://www.google.com/search?q=" + query)

    elif "write a note" in query:
        var.set("What should I write Master")
        window.update()
        speak("What should I write Master")
        note = takeCommand()
        file = open('C:\\Users\\SAYAK DUTTA\Desktop\\file.txt', 'w')
        file.write(note)

    elif "show me the note" in query:
        var.set("Showing Notes")
        window.update()
        speak("Showing Notes")
        file = open('C:\\Users\\SAYAK DUTTA\Desktop\\file.txt', "r")
        print("Project666: ", file.read())
        speak(file.read(6))

    elif 'open notepad' in query:
        var.set("Opening notepad")
        speak('opening notepad')
        path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Accessories\\notepad.exe"
        os.startfile(path)

    elif 'type' in query:
        var.set("What should I type sir ?")
        window.update()
        speak("What should I type sir ?")
        query = query.replace("type", "")
        comm = takeCommand()
        keyboard.write(comm)

    elif 'search in youtube about' in query:
        var.set("This is what I found on youtube")
        window.update()
        speak('This is what I found on youtube')
        query = query.replace('search in youtube about', '')
        webbrowser.open_new_tab('https://www.youtube.com/results?search_query=' + query)

    elif 'open a website' in query:
        var.set("Tell me the name of the website you want to open.")
        window.update()
        speak("Tell me the name of the website you want to open")
        Website_name = takeCommand().lower()
        Website_open = "https://www." + Website_name + '.com'
        webbrowser.open_new_tab(Website_open)

    elif 'open youtube' in query:
        var.set('opening Youtube')
        window.update()
        speak('opening Youtube')
        webbrowser.open("https://www.youtube.com")

    # elif "weather" or  "how the weather outside"or "Please tell me the weather report" in query:
    #     var.set("Here is your report sir")
    #     window.update()
    #     speak("Here is your report sir")
    #     url = "https://www.google.com/search?sxsrf=ACYBGNSQwMLDByBwdVFIUCbQqya-ET7AAA%3A1578847393212&ei=oUwbXtbXDN-C4-EP-5u82AE&q=weather&oq=weather&gs_l=psy-ab.3..35i39i285i70i256j0i67l4j0i131i67j0i131j0i67l2j0.1630.4591..5475...1.2..2.322.1659.9j5j0j1......0....1..gws-wiz.....10..0i71j35i39j35i362i39._5eSPD47bv8&ved=0ahUKEwiWrJvwwP7mAhVfwTgGHfsNDxsQ4dUDCAs&uact=5"
    #     webbrowser.open(url)  # opens the webrowser

    elif 'tell me my battery status' in query:
        battery = psutil.sensors_battery()
        percentage = battery.percent
        var.set(f"Battery is at {percentage} percent")
        window.update()
        speak(f"Battery is at {percentage} percent")
        if percentage >= 75:
            statement1 = "We have enough battery to continue our work. No need of charging sir."
            var.set(statement1)
            window.update()
            speak(statement1)
        elif percentage >= 40 and percentage <= 75:
            statement2 = "We have enough battery to continue our work. But then also you should plug in the charger."
            var.set(statement2)
            window.update()
            speak(statement2)
        elif percentage >= 15 and percentage <= 39:
            statement3 = "We didn't have enough battery to continue our work. Please plug in the charger sir. "
            var.set(statement3)
            window.update()
            speak(statement3)
        elif percentage >= 0 and percentage <= 14:
            statement4 = "We have no battery to continue our work. Please connect your device to charger otherwise your system will shutdown."
            var.set(statement4)
            window.update()
            speak(statement4)

    elif 'new tab' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + t')
    elif 'close this tab' in query or 'close tab' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + w')
    elif 'previous page' in query:
        speak("Ok sir.")
        keyboard.press_and_release('alt + left arrow')
    elif 'forward page' in query:
        speak("Ok sir.")
        keyboard.press_and_release('alt + right arrow')
    elif 'home page' in query:
        speak("Ok sir.")
        keyboard.press_and_release('alt + home')
    elif 'bookmark' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + d')
    elif 'history' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + h')
    elif 'turn on incognito' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + shift + n')
    elif 'refresh' in query or 'reload' in query:
        speak("Ok sir.")
        keyboard.press_and_release('F5')
    elif 'switch tab to right' in query or 'switch to right tab' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + tab')
    elif 'switch tab to left' in query or 'switch to left tab' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + shift + tab')
    elif 'close all tabs' in query or 'close chrome' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + shift + w')
    elif 'open previously closed tab' in query:
        speak("Ok sir.")
        keyboard.press_and_release('ctrl + shift + t')
    elif 'pause' in query or 'wait' in query:
        keyboard.press('k')
    elif 'play' in query or 'resume' in query:
        keyboard.press('space bar')
    elif 'restart' in query:
        keyboard.press('0')
    elif 'skip' in query:
        keyboard.press('l')
    elif 'back' in query:
        keyboard.press('j')
    elif 'full screen' in query:
        keyboard.press('f')
    elif 'cinema mode' in query:
        keyboard.press('t')
    elif 'miniplayer' in query:
        keyboard.press('i')
    elif 'next' in query:
        keyboard.press_and_release('shift + n')

    elif 'take a screenshot' in query:
        img = pyautogui.screenshot()
        var.set("what do you want to save it as?")
        window.update()
        speak("what do you want to save it as?")
        filename = takeCommand()
        img.save(filename + ".png")
        var.set("Do you want me to show it ?")
        window.update()
        speak("do you want me to show it ?")
        ans = takeCommand()
        if "yes" in ans:
            os.startfile(filename + ".png")
        if "no" in ans:
            var.set("As you wish sir !")
            window.update()
            speak("As you wish sir !")

    elif 'open course error' in query:
        var.set('opening course era')
        window.update()
        speak('opening course era')
        webbrowser.open("https://www.coursera.com")

    elif 'open google' in query:
        var.set('opening google')
        window.update()
        speak('opening google')
        webbrowser.open("https://www.google.com")

    elif 'hello' in query:
        var.set('Hello Master')
        window.update()
        speak("Hello Master")

    elif 'open stackoverflow' in query:
        var.set('opening stackoverflow')
        window.update()
        speak('opening stackoverflow')
        webbrowser.open('https://www.stackoverflow.com')

    elif "play music" in query:
        var.set("Sure Master")
        window.update()
        speak("Sure master")
        music_dir = "C:\\Users\\SAYAK DUTTA\\Desktop\\My Music"
        songs = os.listdir(music_dir)
        r = random.choice(songs)
        os.startfile(os.path.join(music_dir, r))

    elif 'tell me the time ' in query:
        strtime = datetime.datetime.now().strftime("%I:%M:%S %p")
        var.set("Sir the time is %s" % strtime)
        window.update()
        speak("Sir the time is %s" % strtime)

    elif "tell me my ip address" in query:
        ip = get('https://api.ipify.org').text
        speak(f"YOUR IP ADDRESS IS {ip}")

    elif 'tell me the date' in query:
        strdate = datetime.datetime.today().strftime("%d %m %y")
        var.set("Sir today's date is %s" % strdate)
        window.update()
        speak("Sir today's date is %s" % strdate)

    elif 'thank you' in query:
        var.set("Welcome Sir")
        window.update()
        speak("Welcome Sir")

    elif 'what can you do for me' in query:
        var.set('I can do multiple tasks for you sir. tell me whatever you want to perform Master')
        window.update()
        speak('I can do multiple tasks for you sir. tell me whatever you want to perform Master')

    elif 'how old are you' in query:
        var.set("I am a little baby Master")
        window.update()
        speak("I am a little baby Master")

    elif 'open media player' in query:
        var.set("opening VLC media Player")
        window.update()
        speak("opening V L C media player")
        path = "%ProgramFiles(x86)%\\Windows Media Player\\wmplayer.exe"  # Enter the correct Path according to your system
        os.startfile(path)

    elif 'what is your name' in query:
        var.set("Myself Project666 Master")
        window.update()
        speak('Myself Project666 Master')

    elif 'who is your creator' in query:
        var.set('My Creator is Mr. Sayak Dutta')
        window.update()
        speak('My Creator is Mr. Sayak Dutta')

    elif 'Hello' in query:
        var.set('Hello  Master! My self Project666')
        window.update()
        speak('Hello Master! My self Project666')

    elif 'open pycharm' in query:
        var.set("Opening Pycharm")
        window.update()
        speak("Opening Pycharm")
        path = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2018.3.2\\bin\\pycharm64.exe"  # Enter the correct Path according to your system
        os.startfile(path)

    elif 'open sublime text' in query:
        print("Project666 : Opening Sublime text")
        speak('opening sublime text')
        Apppath = "C:\\Program Files\\Sublime Text 3\\sublime_text.exe"
        os.startfile(Apppath)

    elif 'volume up' in query or 'increase the volume' in query:
        print("Project666 : Increasing the volume")
        pyautogui.press("volumeup")
    elif 'volume down' in query or 'decrease the volume' in query:
        print("Project666 : Decreasing the volume")
        pyautogui.press("volume down")
    elif 'volume mute' in query or 'mute' in query:
        print("Project666 : Muting the volume")
        pyautogui.press("volumemute")

    elif 'close sublime text' in query:
        print("Project666 : Closing sublime text 3")
        speak("closing sublime text")
        os.system("taskkill /f /im sublime_text.exe")

    elif 'open command prompt' in query:
        print("Project666 : Opening Command Prompt ")
        speak('opening command prompt')
        os.system("start cmd")

    elif 'close command prompt' in query:
        print("Project666: Closing command prompt")
        speak("Closing command Prompt")
        os.system("taskkill /f /im cmd.exe")

    elif 'open zoom' in query:
        print("Project666 : Opening Zoom")
        speak('opening zoom')
        zoompath = "C:\\Users\\SAYAK DUTTA\\AppData\\Roaming\\Zoom\\bin\\Zoom.exe"
        os.startfile(zoompath)

    elif 'close zoom' in query:
        print("Project666 : Closing zoom ")
        speak('closing zoom')
        os.system("taskkill /f /im Zoom.exe")

    # elif 'open adobe photoshop ' in query:
    #     print("PROJECT666 : Opening Adobe photoshop 2020 ")
    #     speak('opening adobe photoshop 2020')
    #     adobepath = ""
    #     os.startfile(adobepath)

    # elif 'close adobe photoshop  ' in query:
    #     print("Project666 : Closing Adobe photoshop")
    #     speak('closing Adobe photoshop')
    #     os.system("taskkill /f /im Photoshop.exe")

    elif 'open  Mc Afree antivirus ' in query:
        print("Project666 : Opening Mc Afree antivirus ")
        speak('opening Mc Afree antivirus')
        Adwarepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\McAfee"
        os.startfile(Adwarepath)

    elif 'open visual studio code ' in query:
        print("Project666 : Opening Visual Studio Code")
        speak('opening visual studio code ')
        vscodepath = "C:\\Users\\SAYAK DUTTA\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
        os.startfile(vscodepath)

    elif 'close visual studio code' in query:
        print("Project666 : Closing Visual Studio Code")
        speak('Closing Visual Studio Code')
        os.system("taskkill /f /im Code.exe")

    elif 'open whatsapp' in query:
        print("Project666 : Opening Whatsapp ")
        speak('opening whatsapp')
        WhatsApppath = "C:\\Users\\SAYAK DUTTA\\Desktop\\WhatsApp"
        os.startfile(WhatsApppath)

    elif 'close whatsapp' in query:
        print("Project666 : Closing Whatsapp")
        speak('Closing whatsapp')
        os.system("taskkill /f /im WhatsApp.exe")

    # elif 'open unity' in query:
    #     print("Project666 : Opening Unity ")
    #     speak('opening unity hub')
    #     unitypath = "C:\\Program Files\\Unity Hub\\Unity Hub.exe"
    #     os.startfile(unitypath)
    #
    # elif 'close unity' in query:
    #     print("Project666 : Closing Unity Hub")
    #     speak('Closing Unity Hub')
    #     os.system("taskkill /f /im Unity Hub.exe")

    # elif 'open blender' in query:
    #     print("Project666 : Opening Blender ")
    #     speak('opening blender')
    #     blenderpath = "C:\\Program Files\\Blender Foundation\\Blender 2.90\\blender.exe"
    #     os.startfile(blenderpath)

    # elif 'open android studio' in query:
    #     print("Project666 : Opening Andriod Studio")
    #     speak('opening android studio')
    #     CodePath = "C:\\Program Files\\Android\\Android Studio\\bin\\studio64.exe"
    #     os.startfile(CodePath)

    elif 'open powerpoint' in query:
        print("PROJECT666 : Opening Ms PowerPoint")
        speak('opening ms powerpoint ')
        powerPath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office PowerPoint 2007"
        os.startfile(powerPath)

    elif 'close powerpoint' in query:
        print("PROJECT666 : Closing ms powerpoint")
        speak('Closing ms powerpoint')
        os.system("taskkill /f /im powerpnt.exe")

    elif 'tell me the temperature' in query:
        Search_tem = "temperature in West Bengal"
        url = f"https://www.google.com/search?q={Search_tem}"
        r = requests.get(url)
        data = BeautifulSoup(r.text, "html.parser")
        temp = data.find("div", class_="BNeawe").text
        print(f"Current {Search_tem} is {temp}")
        speak(f"Current {Search_tem} is {temp}")

    elif 'shutdown the system' in query:
        print(" PROJECT666 : Do you really want to shutdown your Computer?")
        speak("Do you really want to shutdown Your Computer?")
        reply = takeCommand().lower()
        if 'yes' in reply:
            print(" Project66 : Shutting Down System")
            speak("Shutting Down System")
            os.system('shutdown /s /t 1')  # HERE [1] means Second.
        if 'no' in reply:
            print("Project666 : As you wish sir!")
            speak("As you wish sir!")

    elif 'restart' in query or 'reboot' in query or ' reboot the system' in query:
        print(" Project666 : Do you really want to reboot the system?")
        speak("Do you really want to reboot the system?")
        REPLY = takeCommand().lower()
        if 'yes' in REPLY:
            print(" Project666 : Rebooting System...")
            speak(" Rebooting System")
            os.system("shutdown /r /t 1")
        if 'no' in REPLY:
            print("Project666 : As you wish sir! ")
            speak("As you wish sir!")

    elif 'email to me' in query:
        try:
            var.set("What should I say")
            window.update()
            speak('what should I say')
            content = takeCommand()
            to = a['name']
            sendemail(to, content)
            var.set('Email has been sent!')
            window.update()
            speak('Email has been sent!')

        except Exception as e:
            print(e)
            var.set("Sorry Sir! I was not able to send this email")
            window.update()
            speak('Sorry Sir! I was not able to send this email')

    elif "tell me a joke" in query:
        joke = pyjokes.get_joke()
        speak(joke)

    elif "open python" in query:
        var.set("Opening Python Ide")
        window.update()
        speak('opening python Ide')
        os.startfile(
            'C:\\Users\\SAYAK DUTTA\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Python 3.9\\IDLE (Python 3.9 64-bit)')  # Enter the correct Path according to your system

    # elif 'open code blocks' in query:
    #     var.set('Opening Codeblocks')
    #     window.update()
    #     speak('opening Codeblocks')
    #     os.startfile(
    #         "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe")  # Enter the correct Path according to your system

    # elif 'open anaconda' in query:
    #     var.set('Opening Anaconda')
    #     window.update()
    #     speak('opening anaconda')
    #     os.startfile(
    #         "C:\\Users\\mridu\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Anaconda3 (64-bit)\\Anaconda Navigator")  # Enter the correct Path according to your system

    elif 'calculation' in query:
        sum = 0
        var.set('Yes Master, please tell the numbers')
        window.update()
        speak('Yes Master, please tell the numbers')
        while True:
            query = takeCommand()
            if 'answer' in query:
                var.set('here is result' + str(sum))
                window.update()
                speak('here is result' + str(sum))
                break
            elif query:
                if query == 'x**':
                    digit = 30
                elif query in numbers:
                    digit = numbers[query]
                elif 'x' in query:
                    query = query.upper()
                    digit = roman.fromRoman(query)
                elif query.isdigit():
                    digit = int(query)
                else:
                    digit = 0
                sum += digit

    elif "toss" in query or "flip" in query or "coin" in query:
        moves = ["head", "tails"]
        cmove = random.choice(moves)
        speak("The computer chose " + cmove)

    elif 'calculate' in query:
        import wolframalpha
        app = wolframalpha.Client("U6KYX7-34G87A2RUX")
        var.set("What should I calculate?")
        window.update()
        speak("What should I calculate?")
        ans = takeCommand().lower()
        res = app.query(ans)
        var.set(f"Answer = {next(res.results).text}")
        speak(next(res.results).text)
        speak("Is the answer")

    elif 'tell me my location' in query or 'locate' in query:
        query = query.split(" ")
        location = query[2]
        speak("Hold on Sir, I will show you where " + location + " is.")
        webbrowser.open_new_tab(f'https://www.google.co.in/maps/place/ {location}')

    '''
    elif 'enter student details' in query:
            s = Student()
            var.set('Name of the student')
            window.update()
            speak('Name of the student')
            name = takeCommand()
            var.set('standard in which he/she study')
            window.update()
            speak('standard in which he/she study')
            standard = takeCommand()
            var.set('Role Number')
            window.update()
            speak('Role number')
            rollno = takeCommand()
            s.Enterdetalis(name,standard,rollno)
            var.set('Details are saved')
            window.update()
            speak('Details are saved')

        elif 'show me details' in query:
            var.set('Name: '+name+' Standard: '+ standard+' Roll No.: '+ rollno)
            window.update()'''



    if 'click photo' in query:
        stream = cv2.VideoCapture(0)
        grabbed, frame = stream.read()
        if grabbed:
            cv2.imshow('picture', frame)
            cv2.imwrite('picture.jpg', frame)
        stream.release()

    # elif 'record video' in query:
    #     cap = cv2.VideoCapture(0)
    #     out = cv2.VideoWriter('Video.mp4', -1, 20.0, (640, 480))
    #     while (cap.isOpened()):
    #         ret, frame = cap.read()
    #         if ret:
    #
    #             out.write(frame)
    #
    #             cv2.imshow('frame', frame)
    #             if cv2.waitKey(1) & 0xFF == ord('q'):
    #                 break
    #         else:
    #             break
    #     cap.release()
    #     out.release()
    #     cv2.destroyAllWindows()
    # '''
    #     elif 'read the photo' in query: #If you have Pytesseract installed for Optical Character Recognition
    #         try:
    #             im = Image.open('pic.jpg')
    #             text = pytesseract.image_to_string(im)
    #             speak(text)
    #         except Exception as e:
    #             print("Unable to read the data")
    #             print(e)
    #         '''


def update(ind):
    frame = frames[(ind) % 100]
    ind += 1
    label.configure(image=frame)
    window.after(100, update, ind)


def screenshot():
    img = pyautogui.screenshot()
    var.set("what do you want to save it as?")
    window.update()
    speak("what do you want to save it as?")
    filename = takeCommand()
    img.save(filename + ".png")
    var.set("Do you want me to show it ?")
    window.update()
    speak("do you want me to show it ?")
    ans = takeCommand()
    if "yes" in ans:
        os.startfile(filename + ".png")
    if "no" in ans:
        var.set("As you wish sir !")
        window.update()
        speak("As you wish sir !")


def ClickPhoto():
    stream = cv2.VideoCapture(0)
    grabbed, frame = stream.read()
    if grabbed:
        cv2.imshow('picture', frame)
        cv2.imwrite('picture.jpg', frame)
        stream.release()


def Time():
    strtime = datetime.datetime.now().strftime("%I:%M:%S %p")
    var.set(f"Its {strtime}")
    window.update()
    speak(f"Its {strtime}")


def Date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    date = int(datetime.datetime.now().day)
    var.set(f"The current date is {date}:{month}:{year} ")
    window.update()
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)


def Type():
    # This function will type whatever you say
    var.set("What should I type Master ?")
    window.update()
    speak("What should I type Master ?")
    comm = takeCommand()
    keyboard.write(comm)
    keyboard.press('enter')


label2 = Label(window, textvariable=var1, bg='#FAB60C')
label2.config(font=("Courier", 20))
var1.set('User Said : ')
label2.pack()

label1 = Label(window, textvariable=var, bg='#ADD8E6')
label1.config(font=("Courier", 20))
var.set('Welcome Sir')
label1.pack()

frames = [PhotoImage(file='C:\\Users\\SAYAK DUTTA\\Desktop\\Assistant.gif', format='gif -index %i' % (i))
          for i in range(100)]
window.title('Projecte666, A Personal Assistant By RED STAR')

label = Label(window, width=900, height=500)
label.pack()
window.after(0, update, 0)

wishme()

btn0 = Button(text='SPEAK', width=20, command=followmycommand, bg='#5C85FB')
btn0.config(font=("Courier", 12))
btn0.pack()

btn1 = Button(text='SCREENSHOT', width=20, command=screenshot, bg='#5C85FB')
btn1.config(font=("Courier", 12))
btn1.pack()

btn3 = Button(text='TAKE PHOTO', width=20, command=ClickPhoto, bg='#5C85FB')
btn3.config(font=("Courier", 12))
btn3.pack()

btn4 = Button(text='TIME', width=20, command=Time, bg='#5C85FB')
btn4.config(font=("Courier", 12))
btn4.pack()

btn5 = Button(text='DATE', width=20, command=Date, bg='#5C85FB')
btn5.config(font=("Courier", 12))
btn5.pack()

btn6 = Button(text='TYPE', width=20, command=Type, bg='#5C85FB')
btn6.config(font=("Courier", 12))
btn6.pack()

btn2 = Button(text='EXIT', width=20, command=sys.exit, bg='#5C85FB')
btn2.config(font=("Courier", 12))
btn2.pack()

window.mainloop()
