import tkinter as tk
from gtts import gTTS
import os
from langdetect import detect

def detect_language(line):
    try:
        return detect(line)
    except:
        return 'en'


root = tk.Tk()
root.title("Text2Speech")
root.geometry("800x400")
root.configure(bg="black")

label = tk.Label(root, text="Text to Speech", bg="black", fg="white", font=("Helvetica", 30))
label.pack(pady=30)

entry = tk.Entry(root, width=50, font=("Arial", 23))

entry.pack(padx=20)


button = tk.Button(root, text="Save&Play!", font=("Arial", 25), command=lambda: save_and_play(entry.get()))
button.pack(pady=30)


def play_file(entry_text):
    for root, dirs, files in os.walk("./output/"):
        for file in files:
            if file == entry_text:
                os.system("afplay ./output/" + str(file))
                return


var = tk.IntVar()
checkbox = tk.Checkbutton(root, text="Play file", font=("Arial", 20), variable = var)
checkbox.pack()


def save_and_play(entry_text):
    if var.get() == 1:
        play_file(entry_text)
    else:
        language = detect_language(entry_text)
        speech = gTTS(text=entry_text, lang=language, slow=False)
        counter = 1
        for root, dirs, files in os.walk("./output/"):
            for file in files:
                counter += 1
        speech.save("./output/" + str(counter) + ".mp3")
        os.system("afplay ./output/" + str(counter) + ".mp3")
        print("Saved and played!")


root.mainloop()
