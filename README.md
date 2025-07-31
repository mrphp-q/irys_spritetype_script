# 🤖 SpriteType AutoTyper (Iris Test Network)

A Python script that automates the SpriteType typing on the **Iris Test Network** by using OCR (Optical Character Recognition) and simulating human-like typing behavior.

The script captures a defined region of the screen, extracts visible text using Tesseract OCR, and types it automatically. It can also locate and click the "Submit" button between rounds.

---

## 📌 Features

- Automatically types words in the SpriteType typing test
- OCR-based text recognition using Tesseract
- Simulates realistic typing speed with random delays
- Automatically clicks the "Submit" button
- Can be interrupted with the `ESC` key or by closing the console

---

## ⚙️ Requirements

- Python 3.8+
- Tesseract OCR (installed separately)
- Python packages:
  - `pytesseract`
  - `Pillow`
  - `pyautogui`
  - `keyboard`

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/spritetype-auto-typer.git
cd spritetype-auto-typer
```

### 2. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

Download and install Tesseract OCR from:  
🔗 https://github.com/tesseract-ocr/tesseract

After installation, find the path to `tesseract.exe`. Example:

```
C:\Program Files\Tesseract-OCR\tesseract.exe
```
or
```
C:\Users\YOURNAME\AppData\Local\Programs\Tesseract-OCR\tesseract.exe
```

### 4. Set the correct path in the script

Open `main.py` and modify this line:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Path\To\tesseract.exe'
```

✅ This step is required!

---

## ▶️ Usage

1. Open the SpriteType test in your browser (Iris Test Network)
2. Run the script:

```bash
python main.py
```

3. You will have **2 seconds** to switch to the browser window
4. The script will:
   - Take screenshots of the defined region
   - Use OCR to extract text
   - Type the words automatically
   - Locate and click the "Submit" button (if found)

💡 Tip: After launching the script, **minimize the terminal window** so it doesn’t block the browser content.

---

## ⚠️ Usage Notes & Tips

- 🖥 **Keep the browser window on top.**  
  Make sure no other windows (like the terminal or file explorer) are covering the area where the text appears.

- 🪟 **Minimize the console.**  
  The terminal window can be minimized after launch to avoid interfering with the screenshot region.

- 🛑 **Stopping the script:**
  - Press `ESC` to stop the current typing loop.
  - If `ESC` does not work (e.g., due to focus issues), close the console window or press `Ctrl+C` in the terminal to stop the script manually.

---

## 🖼️ Submit Button Image

The script tries to find and click a "Submit" button using an image named `submit.png`.  
Make sure this image:
- Exists in the project folder
- Clearly shows the button from your screen (resolution & scaling must match)

---

## 🧭 Screen Region

The script uses a fixed screen region to capture text:

```python
bbox = (200, 400, 1150, 700)
```

Adjust this to match the position of the typing area on your screen if needed.

---

## 📁 Project Structure

```
spritetype-auto-typer/
├── main.py
├── submit.png
├── requirements.txt
├── LICENSE
└── README.md
```

---

## 📄 License

This project is licensed under the **MIT License**.  
See the [LICENSE](LICENSE) file for full details.

---

## ✍️ Author

**Morph**  
GitHub: [@MiForgeMC](https://github.com/MiForgeMC)

---

## ⚠️ Disclaimer

This script is for educational and testing purposes only.  
Do not use it to violate the terms of service of any platform or game.