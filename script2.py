import tkinter as tk
import main
from gtts import gTTS
import os

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


def save_and_play(entry_text):
    language = main.detect_language(entry_text)
    speech = gTTS(text=entry_text, lang=language, slow=False)
    counter = 1
    for root, dirs, files in os.walk("./output/"):
        for file in files:
            counter += 1
    speech.save("./output/" + str(counter) + ".mp3")
    os.system("afplay ./output/" + str(counter) + ".mp3")
    print("Saved and played!")


root.mainloop()
