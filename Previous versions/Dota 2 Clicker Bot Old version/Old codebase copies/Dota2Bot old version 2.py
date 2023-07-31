from pyautogui import *
import pyautogui
import time

print("Program started")


pixel = pyautogui.pixel(1277, 702)  # Pixel location
pixel_color = (72, 193, 118)  # Expected RGB color


Flag = False

while not Flag:

    pyautogui.moveTo(1277, 702)
    time.sleep(2.5)
    if pixel is not None and pyautogui.pixelMatchesColor(1277, 702, pixel_color, tolerance=30):
        pyautogui.click(1277, 702)
        print("Match accepted!")
        Flag = True
    else:
        time.sleep(1)
        # Pause for 1 second before checking again
        print("Still waiting for match...")
