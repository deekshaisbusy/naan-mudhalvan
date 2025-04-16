
# @title Mood-Based Song Selector
mood = "Happy"  # @param ["Happy", "Sad", "Relaxed", "Energetic", "Romantic"]
# Dictionary of moods and song recommendations
song_recommendations = {
    "Happy": ["Happy - Pharrell Williams", "Can't Stop the Feeling - Justin Timberlake", "Uptown Funk - Mark Ronson"],
    "Sad": ["Someone Like You - Adele", "Fix You - Coldplay", "Hurt - Johnny Cash"],
    "Relaxed": ["Weightless - Marconi Union", "Sunflower - Post Malone", "Perfect - Ed Sheeran"],
    "Energetic": ["Eye of the Tiger - Survivor", "Stronger - Kanye West", "Don't Stop Me Now - Queen"],
    "Romantic": ["Thinking Out Loud - Ed Sheeran", "All of Me - John Legend", "Unchained Melody - The Righteous Brothers"]
}
# Display recommended songs
print(f"🎶 Based on your mood '{mood}', here are some song recommendations:")
for song in song_recommendations[mood]:
    print(f"- {song}")