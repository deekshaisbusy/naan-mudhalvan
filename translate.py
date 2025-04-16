
import googletrans
from googletrans import Translator
from gtts import gTTS
import IPython.display as display
# Function to translate text and convert to speech
def translate_and_speak(text, src_lang="en", dest_lang="de"):
    translator = Translator()
    translated_text = translator.translate(text, src=src_lang, dest=dest_lang).text
    
    print(f"🔹 English: {text}")
    print(f"🔹 German: {translated_text}")
    
    # Convert text to speech
    tts = gTTS(translated_text, lang=dest_lang)
    tts.save("translated_audio.mp3")
    
    # Play the audio
    display.display(display.Audio("translated_audio.mp3", autoplay=True))
# Example usage
text_to_translate = "Hello, how are you?"
translate_and_speak(text_to_translate)