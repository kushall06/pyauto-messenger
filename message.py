Python To Automate Messaging Apps
Author:Anonymous Noble

    
import pyautogui
import time

time.sleep(5)

text='Your Text Here'

while True:
    pyautogui.typewrite(text)

    time.sleep(1)
    pyautogui.press('enter')
    
