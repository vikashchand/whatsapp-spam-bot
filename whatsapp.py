import pyautogui
import time
time.sleep(1)

for i in range(10): 

   pyautogui.typewrite("Hi ,I am Spammer!")
   pyautogui.press('enter')
   time.sleep(0.1)
