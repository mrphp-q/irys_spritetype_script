from PIL import ImageGrab
import pytesseract
from random import uniform
import time
import pyautogui


pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HyperBeast_\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

bbox = (200, 400, 1150, 700)

time.sleep(2) #Время на переход в нужное окно

start = time.time()
total = 0

while True:
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
