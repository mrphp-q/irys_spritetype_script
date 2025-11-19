from PIL import ImageGrab
import pytesseract
from random import uniform
import time
import pyautogui
import keyboard


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HyperBeast_\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

bbox = (200, 400, 1150, 700)

time.sleep(2) #Time to move to the desired window
total = 0


for i in range(1000):
    start = time.time()
    while True:
        total+=1
        if keyboard.is_pressed('esc'):
            print("Остановка по ESC")
            break
        img = ImageGrab.grab(bbox=bbox)
        text_arr = pytesseract.image_to_string(img, lang='eng').replace("\n", ' ').split(' ')
        if time.time()-start <= 15:
            for text in text_arr:
                
                if text != "":
                    end = time.time()
                    if end-start >= 15:
                        break
                    time.sleep(0.1)
                    pyautogui.write(text, interval=uniform(0.05, 0.15))
                    pyautogui.press("space")
        else:
            break
    time.sleep(1)
    while True:
        try:
            loc = pyautogui.locateOnScreen("submit.png")
            pyautogui.click(pyautogui.center(loc))
        except:
            break
        time.sleep(5)
    for i in range(3):
        pyautogui.click(x=800, y=700)
        time.sleep(1)
    pyautogui.press("Tab", presses=2, interval=1)
    time.sleep(2)
    print(total)