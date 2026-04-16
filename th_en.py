import keyboard
import pyperclip
import time

th_to_en = {
    "ๅ": "1","+": "!","๑": "@","/": "2","-": "3","๒": "#","ภ": "4","๓": "$","ถ": "5",
    "๔": "%","ุ": "6","ู": "^","ึ": "7","฿": "&","ค": "8","๕": "*","ต": "9","๖": "(",
    "จ": "0","๗": ")","ข": "-","๘": "_","ช": "=","๙": "+","ๆ": "q","๐": "Q","ไ": "w",
    "\"": "W","ำ": "e","ฎ": "E","พ": "r","ฑ": "R","ะ": "t","ธ": "T","ั": "y","ํ": "Y",
    "ี": "u","๊": "U","ร": "i","ณ": "I","น": "o","ฯ": "O","ย": "p","ญ": "P","บ": "[",
    "ฐ": "{","ล": "]","|": "}","ฃ": "\\","ฅ": "|","ฟ": "a","ฤ": "A","ห": "s","ฆ": "S",
    "ก": "d","ฏ": "D","ด": "f","โ": "F","เ": "g","ฌ": "G","้": "h","็": "H","่": "j",
    "๋": "J","า": "k","ษ": "K","ส": "l","ศ": "L","ว": ";","ซ": ":","ง": "'",".": "\"",
    "ผ": "z","(": "Z","ป": "x",")": "X","แ": "c","ฉ": "C","อ": "v","ฮ": "V","ิ": "b",
    "ฺ": "B","ท": "m","?": "M","ม": ",","ฒ": "<","ใ": ".","ฬ": ">","ฝ": "/","ฦ": "?"
}

en_to_th = {v: k for k, v in th_to_en.items()}


def swap_text(text):
    result = ""
    for char in text:
        if char in th_to_en:
            result += th_to_en[char]
        elif char in en_to_th:
            result += en_to_th[char]
        else:
            result += char
    return result


def swap_selected():
    # copy
    keyboard.send("ctrl+c")
    time.sleep(0.05)

    text = pyperclip.paste()
    if not text:
        return

    swapped = swap_text(text)

    pyperclip.copy(swapped)

    # paste back (replace selected)
    keyboard.send("ctrl+v")


# hotkey
keyboard.add_hotkey("ctrl+q", swap_selected)

print("Ready: Press Ctrl+Q to swap TH/EN")
keyboard.wait()