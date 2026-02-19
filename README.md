# Mental Health Keyword Intensity Analyzer

This project performs an exploratory analysis of mental-health-related text
by measuring keyword intensity for anxiety, depression, and positive coping.

## Disclaimer
This is **not a diagnostic tool**. It is an exploratory NLP project intended
for educational purposes only.

## How It Works
- Text is preprocessed and tokenized
- Keyword frequency is used to estimate intensity levels
- Scores are normalized by text length for fairness


## Live Demo
```
Enter text: "Feeling anxious and stressed, but trying to stay calm"
Anxiety Intensity: 0.125
Depression Intensity: 0.0  
Positive Coping Intensity: 0.062
```

## Key Features
- 3 Keyword Categories: Anxiety (7 words), Depression (7 words), Positive (7 words)
- Smart Preprocessing: Lowercase conversion, punctuation removal, token splitting
- Intensity Calculation: `keyword_matches / total_words` (0-1 scale)
- Instant Results: Enter text → Get formatted report
- Privacy First: 100% local, no data collection

## How to Use
```bash
1. Save as mental_health_analyzer.py
2. Run: python mental_health_analyzer.py
3. Enter any text
4. View scores instantly
```

## Tech Stack
- Python 3.x
- `re` module (regex preprocessing)
- Custom dictionaries (21 keywords total)

## Easy Extensions
- Add new keyword lists
- Analyze files instead of CLI input
- Export results to CSV

