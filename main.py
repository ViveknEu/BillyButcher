
#nig
from tkinter import *
import os
from datetime import datetime
import tkinter.ttk as ttk
from tkinter.constants import *
try:
    import pywhatkit
except:
    print("you are offline")
import speech_recognition as sr
import pyttsx3


def speaker(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()


def time_teller():
    now = datetime.now()
    current_time = now.strftime("%H:%M")
    reply_print("The current time is "+current_time)



apps=["chrome,browser,chrome browser",
      "msedge,edge,edge browser",
      "devcpp,c++ compiler,c compiler,ccompiler,c++ ide",
      "msword,word,winword",
      "powerpnt,ppt,powerpoint",
      "excel,msexcel",
      "photoshop,photo editor",
      "brave,brave browser",
        "settings,setting,control panel",
      "blender,3d art",
      "store,msstore,microsoft store",
      "pycharm,python ide,python"
      ]
commands=['"C:\Program Files\Google\Chrome\Application\chrome.exe"',
          '"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"',
          '"C:\Program Files (x86)\Dev-Cpp\devcpp.exe"',
        "start winword",
          "start powerpnt",
          "start excel",
        '"C:\Program Files\Adobe\Adobe Photoshop 2021\Photoshop.exe"',
        '"C:\Program Files\BraveSoftware\Brave-Browser\Application\\brave.exe"',
        "start control.exe",
        '"C:\Program Files\WindowsApps\BlenderFoundation.Blender_3.2.2.0_x64__ppwjx1n5r4v9t\Blender\\blender.exe"',
          "start ms-windows-store:",
        '"C:\Program Files\JetBrains\PyCharm Community Edition 2022.1.3\\bin\pycharm64.exe"'
          ]


def searcher(search_text):
    try:
        pywhatkit.search(search_text)
        reply_print("There you go\n"
                "Your search results are in chrome tabs")
    except:
        reply_print("You  are offline\n"
                    "Can't search the web")

def opener(app_name):                           #open apps
    global apps,commands
    for i in range(len(apps)):
        if app_name in apps[i].split(sep=","):
            os.system(commands[i])
            reply_print("okay, I will open " + app_name)
            return
    reply_print("The app was not found\n"
                        "May be the app is not installed.")
"""
def plus_adder(message):
    re_message=""
    for i in message.split():
        if i!="play":
            re_message=i+"+"
        else:
            continue
    return (re_message[0:len(re_message)-1])
    """

def decider(message):                            #finds what to do as per input
    try:
        if "open" in message.split():
            opener(extrator(message,exc="open"))
        elif "search" in message.split():
            searcher(extrator(message,exc="search"))
        elif "who" in message.split() and "are" in message.split() and ("you" in message.split() or "you?" in message.split()):
            reply_print("I am Billy Butcher")
        elif "who" in message.split() and "is" in message.split():
            searcher(extrator(message,exc="who",exc1="is"))
        elif "what" and "time" in message.split():
            time_teller()
        #elif "play" in message.split():
            #searcher("https://www.youtube.com/results?search_query="+plus_adder(message))
        else:
            searcher(message)
    except:
        searcher(message)


def extrator(message,exc="",exc1=""):                           #removes the particular word
    exc_message=""
    for i in message.lower().split():
        if i == exc or i == exc1:
            continue
        else:
            exc_message=exc_message+i+" "
    return (exc_message[0:len(exc_message)-1])

def applist():
    applist_window=Toplevel()
    applist_window.geometry("360x240")
    applist_window.resizable(False,False)
    applist_window.title("Apps currently supported")
    Label(applist_window,text="Chrome\n"
                              "Microsoft Edge\n"
                              "Dev-C++\n"
                              "Microsoft Word\n"
                              "Microsoft powerpoint\n"
                              "microsoft excel\n"
                              "photoshop\n"
                              "brave browser\n"
                              "blender\n"
                              "microsoft store\n"
                              "Pycharm\n").pack(anchor="center")
    Button(applist_window,text="OK",command=applist_window.destroy).place(x=165,y=200)
    applist_window.mainloop()


def info():                                                             #help window
    info_window=Toplevel()
    info_window.title("HELP")
    info_window.geometry('260x180')
    info_window.resizable(False,False)
    Label(info_window,text="(1)Tap on speak button to speak your command\n\n"
                           "(2)Type your command if you want\n\n"
                           "*Note: accept 3-4 lines of commands\n\n"
                           "       try to spell the words correctly").pack()
    Button(info_window,text="OK",command=info_window.destroy).place(x=113,y=130)
    info_window.mainloop()


def listen():                                                   #voice recognition
    r = sr.Recognizer()
    try:
            # use the microphone as source for input.
        with sr.Microphone() as source2:
            # wait for a second to let the recognizer
            # adjust the energy threshold based on
            # the surrounding noise level
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("Lisetning")
            Canvas1 = Canvas(window, background="#deb961", borderwidth="2")                          # reply text
            Canvas1.create_text(5,50,text="Listening...",fill="#801811",anchor="w",font='Arial 10')
            Canvas1.place(relx=0.017, rely=0.348, relheight=0.394, relwidth=0.458)
            audio2 = r.listen(source2,phrase_time_limit=5)                                                              # listens for the user's input
            MyText = r.recognize_google(audio2)                                                     # Using google to recognize audio
            MyText = MyText.lower()
            message_print(MyText)
            decider(MyText)

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
        reply_print("Your are offline\n"
                        "This feature doesn't work while offline")

    except sr.UnknownValueError:
        print("unknown error occured")
        reply_print("I don't think I understood that...")


def event_detector(event):
    message_print(Entry1.get().lower())
    decider(Entry1.get().lower())


def reply_print(message):                               #printing replay to the canvas
    Canvas1 = Canvas(window, background="#2e2d2d", borderwidth="2")
    Canvas1.create_text(5, 50, text="BILLY:\n"+message, fill="#cccaca", anchor="w", font='Times 11')
    Canvas1.place(relx=0.017, rely=0.348, relheight=0.394, relwidth=0.458)
    window.update()
    speaker(message)


def message_print(message):                                #printing the message into canvas
    Canvas2 = Canvas(window, background="#2e2d2d", borderwidth="2")
    Canvas2.create_text(5,50, text="YOU:\n"+message, fill="#cccaca",anchor='w',font=('Times 11'))
    Canvas2.place(relx=0.536, rely=0.07, relheight=0.394, relwidth=0.44)
    window.update()
def temp_text(event):
    Entry1.delete(0, "end")



window = Tk()
icon=PhotoImage(file="icon.png")
window.geometry("605x287+282+134")
window.minsize(120, 1)
window.iconphoto(False,icon)
window.maxsize(1370, 749)
window.resizable(False,False)
window.title("Billy Butcher")
window.configure(borderwidth="4")
window.configure(background="#1e1f1e")
window.configure(cursor="arrow")
Canvas1=Canvas(window,background="#2e2d2d",borderwidth="2")     #reply text
Canvas1.create_text(70,95, text="No reply from Billy", fill="#cccaca", anchor="w", font='Times 11')
Canvas1.place(relx=0.017, rely=0.348, relheight=0.394, relwidth=0.458)
Canvas2=Canvas(window,background="#2e2d2d",borderwidth="2")    #message_text
Canvas2.create_text(80,95, text="No Query asked.. ", fill="#cccaca",anchor='w',font=('Times 11'))
Canvas2.place(relx=0.536, rely=0.07, relheight=0.394, relwidth=0.44)
Button1=Button(window,background="#000000",foreground="#cccaca",text="Speak",command=listen)                 #mic button
Button1.place(relx=0.886, rely=0.801, height=31, width=47)
Button2=Button(window,text="?",background="#000000",foreground="#cccaca",command=info)
Button2.place(relx=0.017, rely=0.035, height=24, width=27)
Button3=Button(window,text="Apps",background="#000000",foreground="#cccaca",command=applist)
Button3.place(relx=0.080, rely=0.035, height=24, width=36)
Entry1=Entry(window,background="#a3a2a2")                      #message box
Entry1.insert(0,"Type your query here...")
Entry1.place(relx=0.017, rely=0.801, height=30, relwidth=0.833)
Entry1.bind("<FocusIn>", temp_text)
# noinspection PyTypeChecker
Entry1.bind('<Return>', event_detector)
window.mainloop()
