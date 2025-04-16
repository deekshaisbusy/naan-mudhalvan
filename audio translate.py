
# Install required libraries
!pip install deep-translator gtts
from deep_translator import GoogleTranslator
from gtts import gTTS
import IPython.display as display
# Function to translate and convert text to speech
def translate_and_speak(text, src_lang="en", dest_lang="de"):
    translated_text = GoogleTranslator(source=src_lang, target=dest_lang).translate(text)
    
    print(f"🔹 English: {text}")
    print(f"🔹 German: {translated_text}")
    
    # Convert translated text to speech
    tts = gTTS(translated_text, lang=dest_lang)
    tts.save("translated_audio.mp3")
    
    # Play the translated speech
    display.display(display.Audio("translated_audio.mp3", autoplay=True))
# Example usage
text_to_translate = "Good morning! Have a nice day."
translate_and_speak(text_to_translate)