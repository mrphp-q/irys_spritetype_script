from PIL import ImageGrab
import pytesseract
from random import uniform
import time

# (опционально) путь к tesseract.exe
pytesseract.pytesseract.tesseract_cmd = r'C:\Users\HyperBeast_\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

# Снимок части экрана (левая, верхняя, правая, нижняя координаты)
bbox = (200, 400, 1150, 700)
img = ImageGrab.grab(bbox=bbox)

# Распознавание текста
start = time.time()
total = 0

while True:
    text_arr = pytesseract.image_to_string(img, lang='eng').replace("\n", ' ').split(' ')
    if time.time()-start <= 15:
        for text in text_arr:
            
            if text != "":
                for t in text:
                    end = time.time()
                    if end-start >= 15:
                        break
                    time.sleep(uniform(0.09, 0.2))
                    print(f"{t} - {end-start}")
                    total+=1
                print()
    else:
        break

print(f"Время: {end-start}\nСимволы: {total}")
