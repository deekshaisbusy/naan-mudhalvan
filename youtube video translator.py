
!pip install youtube-transcript-api googletrans==4.0.0-rc1
from youtube_transcript_api import YouTubeTranscriptApi
from googletrans import Translator
video_id = "YOUR_VIDEO_ID"  # e.g. 'dQw4w9WgXcQ'
lang_target = "ta"  # Target language (e.g. 'ta' for Tamil)
# Get transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)
text = " ".join([i['text'] for i in transcript])
# Translate
translator = Translator()
translated = translator.translate(text, dest=lang_target)
print("Translated Transcript:\n", translated.text)