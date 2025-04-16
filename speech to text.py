
import speech_recognition as sr
r = sr.Recognizer()
audio_file = "audio.wav"  # Upload your file
with sr.AudioFile(audio_file) as source:
    audio = r.record(source)
text = r.recognize_google(audio)
print("Transcribed Text:\n", text)