# Keyword dictionaries
ANXIETY_WORDS = [
    "anxious", "panic", "fear", "worried", "nervous", "stress", "overthinking"
]

DEPRESSION_WORDS = [
    "sad", "hopeless", "tired", "empty", "worthless", "depressed", "lonely"
]

POSITIVE_WORDS = [
    "hope", "calm", "relaxed", "grateful", "happy", "improving", "healing"
]

#Text Preprocessing
import re

def preprocess(text):
    text = text.lower()
    text = re.sub(r"[^a-z\s]", "", text)
    return text.split()

#Intensity Scoring Function
def keyword_intensity(tokens, keyword_list):
    if len(tokens) == 0:
        return 0
    count = sum(1 for word in tokens if word in keyword_list)
    return round(count / len(tokens), 3)

#Analyzer Function
def analyze_text(text):
    tokens = preprocess(text)

    anxiety_score = keyword_intensity(tokens, ANXIETY_WORDS)
    depression_score = keyword_intensity(tokens, DEPRESSION_WORDS)
    positive_score = keyword_intensity(tokens, POSITIVE_WORDS)

    return {
        "Anxiety Intensity": anxiety_score,
        "Depression Intensity": depression_score,
        "Positive Coping Intensity": positive_score
    }


if __name__ == "__main__":
    text = input("Enter mental health related text:\n\n")
    results = analyze_text(text)

    print("\n--- Mental Health Keyword Intensity Report ---")
    for k, v in results.items():
        print(f"{k}: {v}")
