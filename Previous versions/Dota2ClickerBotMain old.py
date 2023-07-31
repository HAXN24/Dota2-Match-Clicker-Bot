import PySimpleGUI as sg
import pyautogui
import threading
import time
import os
import sys



sg.theme('Dark Black')
layout = [
    [sg.Text("""Instructions: 
1.) Open Dota 2 
2.) Click Run to start bot

Note:
 • Dota must be open while using this program
 • Program will terminate once match found!
             """,
             size=(40, 9),)],
    [sg.Column([[sg.Button('Run', border_width=3, mouseover_colors=("white", "gray80"))]], justification='center'),
     sg.Column([[sg.Button("Cancel", border_width=3, mouseover_colors=("white", "gray80"))]], justification='center')],
    [sg.Output(size=(50, 10), key='-OUTPUT-', background_color='black', text_color='white',
               font=('Courier New', 10))],
]

# Create Window
window = sg.Window("Dota Match Clicker Bot", layout, finalize=True)



def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


# changing icon from the window GU
window.set_icon(resource_path(r'C:\Users\nicol\Desktop\Programming\Python Projects\Dota2ClickerBot\resources\jugg.ico'))




def countDown():
    count = 5
    while count > 0:
        print("Program terminating in " + str(count) + "...")
        time.sleep(1)
        count -= 1
    return "\nThanks for using Dota 2 clicker bot by HAXN24\nGoodbye!"

# button locator + click script


def click():
    time.sleep(1)
    print("Searching for match...\n")
    button = pyautogui.locateCenterOnScreen(
        resource_path(r'C:\Users\nicol\Desktop\Programming\Python Projects\Dota2ClickerBot\resources\button.png'), minSearchTime=3000)

    pyautogui.moveTo(button)
    pyautogui.click(button)
    pyautogui.click(button)
    print("Match accepted!\n")
    print(countDown())
    time.sleep(3)
    window.close()


isRunning = False

while True:
    event, values = window.read(timeout=100)

    if event == "Cancel" or event == sg.WIN_CLOSED:
        if isRunning:
            print("Terminating Program. Goodbye!")
            window.read(timeout=1000)
            break
        else:
            print("Terminating program. Goodbye!")
            window.read(timeout=1000)
            break

    elif event == "Run":
        if not isRunning:
            print("Script is running! Please open Dota 2 now :)\n")
            isRunning = True
            # multithreading to have the GUI and click script running at the same time!
            threading.Thread(target=click).start()
        else:
            print("Script is already running!!\n")

window.close()
