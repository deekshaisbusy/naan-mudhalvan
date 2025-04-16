
# Step 1: Install dependencies
!pip install moviepy gtts whisper googletrans==4.0.0-rc1
import moviepy.editor as mp
from gtts import gTTS
import whisper
from googletrans import Translator
import os
# Step 2: Upload your video
from google.colab import files
uploaded = files.upload()
video_path = list(uploaded.keys())[0]
# Step 3: Extract audio from video
video = mp.VideoFileClip(video_path)
audio_path = "extracted_audio.wav"
video.audio.write_audiofile(audio_path)
# Step 4: Transcribe using Whisper
model = whisper.load_model("base")
result = model.transcribe(audio_path)
original_text = result["text"]
print("Original Transcription:\n", original_text)
# Step 5: Translate text
translator = Translator()
translated = translator.translate(original_text, dest='ta')  # Change 'ta' to your target language code
translated_text = translated.text
print("\nTranslated Text:\n", translated_text)
# Step 6: Convert translated text to audio
tts = gTTS(text=translated_text, lang='ta')  # 'ta' for Tamil, 'hi' for Hindi, etc.
tts_path = "translated_audio.mp3"
tts.save(tts_path)
# Step 7: Merge audio back with video
final_video = video.set_audio(mp.AudioFileClip(tts_path))
output_path = "translated_video.mp4"
final_video.write_videofile(output_path)
# Step 8: Download
files.download(output_path)