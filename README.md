# Melancholy
## A Smart Mental Health Diary
### Authors: Minjae Kung, Hanqi Xiao, Graham Troy, Achyuta Kannan
### HackNC 2022-2023

### Project: MelanJournal - A NLP-based Diary Analytics Tool

#### Overview

MelanJournal is a Python-based project that aims to provide a comprehensive analysis of your diary entries. It uses Natural Language Processing (NLP) techniques to track your emotions, sentiments, and frequently used words over time. The project is designed to offer insights into your emotional state, allowing you to better understand yourself.

#### Features

- **Automated Sentiment Analysis**: Uses VADER (Valence Aware Dictionary and sEntiment Reasoner) to analyze the sentiment of each diary entry.
  
- **Emotion Classification**: Utilizes the DistilBERT model to classify the emotions expressed in the text.

- **Word Cloud Generation**: Creates a word cloud based on the frequency of words in your entries, after stemming and removing stopwords.

- **Time-based Analysis**: Plots your sentiment and emotions over time to track changes.

- **Reminder Settings**: Allows you to set a reminder time for making diary entries.

#### Requirements

- Python 3.x
- Pandas
- NumPy
- TextBlob
- NLTK
- Matplotlib
- Transformers

#### Installation

1. Clone the repository.
2. Install the required packages.

    ```bash
    pip install -r requirements.txt
    ```
    
#### Code Structure
(Excludes flask web app)
- `MelanJournal`: The main class that handles the diary analytics.
  - `__init__`: Initializes the object and sets default settings.
  - `settings`: Allows you to change settings like reminder time.
  - `turn_into_data_frame`: Converts a diary entry into a DataFrame row and performs NLP analysis.
  - `wordcloud`: Generates a word cloud based on word frequencies.
  - `sentiment_by_time`: Plots sentiment over time.

- Utility Functions:
  - `filter_insignificant`: Filters out insignificant words based on their POS tags.
  - `word_frequencies`: Returns a frequency dictionary of words.
  - `word_cloud_clean`: Cleans and stems the diary entry.
  - `sentiment_polarity`: Analyzes the sentiment of the text.
  - `emotion_polarity`: Classifies the emotion of the text.

#### Future Work

- Add more visualization options.
- Optimize for scalability and performance.
