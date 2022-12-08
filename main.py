import sys
from gtts import gTTS
import os
from langdetect import detect



def detect_language(line):
    try:
        return detect(line)
    except:
        return 'en'


def text_to_speech(source_dir_path, output_path):
    # read all files in a directory
    counter = 1
    for root, dirs, files in os.walk(source_dir_path):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.txt'):
                with open(file_path, 'r') as f:
                    text = f.readlines()
                    for line in text:
                        # convert text to speech
                        language = detect_language(line)
                        try:
                            speech = gTTS(text=line, lang=language, slow=False)
                            speech.save(output_path + str(counter) + '.mp3')
                            counter += 1
                            print('Saved: ' + output_path + str(counter) + '.mp3')
                        except:
                            print('Error in converting text to speech or saving file')


text_to_speech(str(sys.argv[1]), str(sys.argv[2]))
