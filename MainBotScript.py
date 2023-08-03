import PySimpleGUI as sg
import pyautogui
import threading
import time
import os
import sys
import emailMessengerScriptModule
from datetime import datetime

# cmd script pyinstaller --onefile --icon="jugg.ico" --add-data "resources;resources" --noconsole Dota2ClickerBotMainUpdated.py

# TO DO:
# go right back to "searching" if a match has been canceled
# How to make this program work for non developer users.
# Figuring out how to stop the clickThread if the click script/function is running or if a match has been found.

sg.theme('Dark Black')
layout = [
    [sg.Text("""Instructions: 
1.) Open Dota 2 
2.) Click Run to start bot

Note:
 • Dota must be open while using this program
 • Program will terminate once match found!
             """,
             size=(40, 9), )],
    [sg.Column([[sg.Button('Run', border_width=3, mouseover_colors=("white", "gray80"))]], justification='center'),
     sg.Column([[sg.Button("Cancel", border_width=3, mouseover_colors=("white", "gray80"))]], justification='center')],
    [sg.Output(size=(50, 10), key='-OUTPUT-', background_color='black', text_color='white',
               font=('Courier New', 10))],
]

# Create Window
window = sg.Window("Dota Match Clicker Bot", layout, finalize=True)

# Get the directory of the script
script_dir = os.path.dirname(os.path.abspath(__file__))
resources_path = os.path.join(script_dir, 'resources')
icon_path = os.path.join(resources_path, 'jugg.ico')
button_path = os.path.join(resources_path, 'button.png')

# changing icon from the window GUI
window.set_icon(icon_path)


# Sends email if a match has been accepted & found
def send_email():
    try:
        emailMessengerScriptModule.sendEmail()
        print("Email sent successfully!\n")
    except Exception as e:
        print(f"Error sending email: {e}\n")


# Function to start the countdown and terminate program if matchFound is True
def terminate_program_if_match_found(match_found):
    if match_found:
        count = 5
        while count > 0:
            print("Program terminating in " + str(count) + "...")
            time.sleep(1)
            count -= 1
        print("\nThanks for using Dota 2 clicker bot by HAXN24\nGoodbye!")
        time.sleep(2)
        window.close()


# Event to terminate click thread
STOP_EVENT = threading.Event()

# Flag if a match has been found
matchFound = False

# Flag to indicate if the click thread is running
clickThreadRunning = False


# Function to stop the click thread
def stop_click_thread():
    STOP_EVENT.set()
    threading.Thread(target=terminate_program_if_match_found,
                     args=(matchFound,)).start()


# script for accept button locator and clicks it
def click():
    global matchFound, clickThreadRunning
    clickThreadRunning = True
    time.sleep(1)
    button = pyautogui.locateCenterOnScreen(button_path, minSearchTime=3000)
    if not STOP_EVENT.is_set():
        matchFound = True
        pyautogui.moveTo(button)
        pyautogui.click(button)
        print(f"Match accepted! {datetime.now()}\n")
        send_email()
        stop_click_thread()


# terminate program if script is running
def terminateProgram():
    print(
        "Program Terminating!\nThanks for using Dota 2 clicker bot by HAXN24\nGoodbye!")
    STOP_EVENT.set()
    window.read(timeout=2000)
    window.close()


# flag for script if running
scriptRunning = False

while True:
    event, values = window.read()
    if event == "Cancel" or event == sg.WIN_CLOSED:
        if scriptRunning:
            terminateProgram()
            break
        else:
            terminateProgram()
            break
    elif event == "Run":
        if not scriptRunning:
            print("Script has started! Please open Dota 2 now.\n")
            window.read(timeout=1000)
            print("Searching for match...\n")
            scriptRunning = True
            STOP_EVENT.clear()
            # multithreading to have the GUI and click script running at the same time!
            clickThread = threading.Thread(target=click)
            clickThread.start()
        elif scriptRunning:
            scriptRunning = True
            print("Script is already running!!\n")
        else:
            if event == "Cancel" or event == sg.WIN_CLOSED:
                stop_click_thread()
window.close()
sys.exit()
