import emoji  #importing emoji package
from textblob import TextBlob #imports textblob package
from dataclasses import dataclass #imports dataclass package

@dataclass
class Mood:
    emoji: str # emoji is presented in string format
    sentiment: float # the sentiments are presented in decimal format


def get_mood(input_text: str, *, threshold: float) -> Mood:
    sentiment: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = threshold
    hostile_threshold: float = -threshold

    if sentiment >= friendly_threshold:
        return  Mood(print(emoji.emojize("\U0001F601")), sentiment)
    elif sentiment <= hostile_threshold :
        return  Mood(print(emoji.emojize("\U0001F61E")), sentiment)
    else:
        return Mood(print(emoji.emojize(":neutral_face:")), sentiment)

if __name__ == '__main__':
    while True:
        text: str = input('Tell me your thoughts: ')

        mood: Mood = get_mood(text, threshold= 0.5)
        
        print(f'{mood.emoji} ({mood.sentiment})')
