import PySimpleGUI as sg
from pyautogui import *
import pyautogui

# NOTE: this is the old verison of the codebase where we locate the button using customized coordinates (2440x1440p resolution) and without referencing "button.png" screenshot.


sg.theme('Dark Black')
layout = [

    [sg.Text("""Instructions: 
1.) Open Dota 2 
2.) Click Run to start bot
Note:
             
 • Dota must be left open while using this program
 • Program will terminate once match found!
             """,
             size=(40, 9),)],
    [sg.Column([[sg.Button('Run', border_width=3, mouseover_colors=("white", "gray80"))]], justification='center'),
     sg.Column([[sg.Button("Cancel", border_width=3, mouseover_colors=("white", "gray80"))]], justification='center')],
    [sg.Output(size=(50, 10), key='-OUTPUT-', background_color='black', text_color='white',
               font=('Courier New', 10))],

]

# Create Window
window = sg.Window("Dota Match Clicker Bot- by HAXN24",
                   layout, finalize=True)


# gif jugg waiting

# changing icon from the window GUI
window.set_icon(
    r'insert abs path of jugg.ico')
event, values = window.read()

Flag = False
# while not Flag:
while not Flag:

    if event == "Cancel" or event == sg.WIN_CLOSED:
        print("Terminating Program")
        Flag = True

    elif event == "Run":
        print("Dota 2 Clicker Bot Initiated!")
        pixel = pyautogui.pixel(1277, 702)  # Pixel location
        pixel_color = (72, 193, 118)  # Expected RGB color

        while not Flag:

            pyautogui.moveTo(1277, 702)

            if pixel is not None and pyautogui.pixelMatchesColor(1277, 702, pixel_color, tolerance=30):
                pyautogui.click(1277, 702)
                print("Match accepted! Terminating Program")
                Flag = True
            else:
                # Pause for 1 second before checking again
                if event == "Cancel" or event == sg.WIN_CLOSED:
                    print("Terminating Program")
                    Flag = True
                    window.close()
                else:
                    event, values = window.read(timeout=2000)
                    print("Waiting for match...")


window.close()
