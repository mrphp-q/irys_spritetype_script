from PIL import ImageGrab
import pytesseract
from random import uniform
import time
import pyautogui
import keyboard


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HyperBeast_\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

bbox = (200, 400, 1150, 700)

time.sleep(2) #Время на переход в нужное окно



for i in range(10):
    start = time.time()
    total = 0
    while True:
        if keyboard.is_pressed('esc'):
            print("Остановка по ESC")
            break
        img = ImageGrab.grab(bbox=bbox) #Считываю изображние
        text_arr = pytesseract.image_to_string(img, lang='eng').replace("\n", ' ').split(' ') #Преобразую изображение в массив слов
        print(text_arr)
        if time.time()-start <= 15:
            for text in text_arr:
                
                if text != "":
                    # for t in text:
                    #     end = time.time()
                    #     if end-start >= 15:
                    #         break
                    #     # time.sleep(uniform(0.09, 0.2))
                    #     # print(f"{t} - {end-start}")
                        
                    # # print()

                    end = time.time()
                    if end-start >= 15:
                        break
                    time.sleep(0.1)
                    pyautogui.write(text, interval=uniform(0.05, 0.15))
                    total+=1
                    pyautogui.press("space")
        else:
            break
    print(f"Время: {end-start}\nСимволы: {total}")

    time.sleep(1)
    while True:
        try:
            loc = pyautogui.locateOnScreen("submit.png")
            pyautogui.click(pyautogui.center(loc))
        except:
            break
        time.sleep(5)
    # loc = pyautogui.locateOnScreen("again.png")
    # pyautogui.click(pyautogui.center(loc))
    for i in range(3):
        pyautogui.click(x=800, y=700)
        time.sleep(1)
    pyautogui.press("Tab", presses=2, interval=1)
    time.sleep(2)