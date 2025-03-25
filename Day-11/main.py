import re

emoji_mood_dict = {
    "😊": "Happy Mood!",
    "😃": "Happy Mood!",
    "😍": "Happy Mood!",
    "😢": "Sad Mood!",
    "😭": "Sad Mood!",
    "☹": "Sad Mood!",
    "😡": "Angry Mood!",
    "🤬": "Angry Mood!",
    "😠": "Angry Mood!",
    "😐": "Neutral Mood!",
    "😶": "Neutral Mood!",
    "🤔": "Neutral Mood!"
}

def analyze_mood(message):
    emojis = re.findall(r'[\U0001F600-\U0001F64F]', message)
    if emojis:
        for emoji in emojis:
            if emoji in emoji_mood_dict:
                return f"Detected Mood: {emoji_mood_dict[emoji]}"
        return "Emoji found, but mood not recognized!"
    else:
        return "No emoji found, can't detect mood!"
user_message = input("Enter your message: ")
result = analyze_mood(user_message)
print(result)