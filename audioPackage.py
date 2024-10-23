import os
from gtts import gTTS

def createAudioBook(text_file, output_file):
    with open(text_file, 'r', encoding='utf-8') as file:
        
        text = file.read()
        
    tts = gTTS(text=text, lang='en')
    tts.save(output_file)
    print(f"AudioBook saved as { output_file}")
    
text_file = "clcodingtxt.txt"
output_file = "audiobookconvert.mp3"

createAudioBook(text_file, output_file)
os.system(f"start {output_file}")