"""A NLP based Diary. Two"""
# Capturing settings.
import datetime
import pandas as pd
import numpy as np
from textblob import TextBlob
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk import pos_tag
from textblob import Word
from get_txt import fetch
import string
import nltk
nltk.download('averaged_perceptron_tagger')


def filter_insignificant(chunk, tag_suffixes=['DT', 'CC']):
  good = []

  for word, tag in chunk:
    ok = True

    for suffix in tag_suffixes:
      if tag.endswith(suffix):
        ok = False
        break

    if ok:
      good.append((word, tag))

  return good


def word_frequencies(cloud_cleaned_entry: list[str]) -> dict[str, int]:
    freq_dict = dict()
    for word in cloud_cleaned_entry:
        if word not in freq_dict:
            freq_dict[word] = 1
        else:
            freq_dict[word] += 1
    # print("\n".join([f"{word} : {freq}" for word, freq in freq_dict.items()]))
    return freq_dict


def word_cloud_clean(entry: str) -> str:
    """Clean every paragraph, stems all the words, puts into one list."""
    stemmer = PorterStemmer()
    eng_stops: list[str] = stopwords.words("english")
    entry = [i for i in word_tokenize(entry) if i not in eng_stops]
    entry = list(filter(lambda word: word not in string.punctuation+"’“”", entry))
    print(entry)
    entry = [word for word, pos in filter_insignificant(pos_tag(entry))]
    # print(entry)
    # entry = [stemmer.stem(w) for w in entry]
    print(entry)
    return entry



class MelanJournal():
    reminder_time: datetime
    new_user: bool = True
    data: pd.DataFrame


    def __init__(self):
        """Runs upon restarting the program."""
        if self.new_user == True:
            self.settings()
            self.new_user = False
            self.data = pd.DataFrame(columns = ["Date", "Text"])


    def settings(self) -> None:
        """Sets or changes the settings."""
        # reminder_time = input("In the format HH:MM: ")
        reminder_time = "03:35"
        self.reminder_time = datetime.time(*map(int, reminder_time.split(':')))


    def turn_into_data_frame(self, data = dict[datetime.datetime, str]) -> None:
        """Convert into a dataframe."""
        self.data = pd.concat([pd.DataFrame(data), self.data], sort = False)
        # generate the stemmed version of all entries.
        self.data["Word Cloud Text"] = self.data["Text"].apply(word_cloud_clean)
        self.data["Word Cloud Frequency"] = self.data["Word Cloud Text"].apply(word_frequencies)
        print(self.data)

    
    def wordcloud(self) -> None:
        for i, row in self.data.iterrows():
            frequencies = row["Word Cloud Frequency"]


    def sentiment_by_time(self) -> pd.DataFrame:
        """Make a new column where a new column is added to the dataframe."""


def main() -> None:
    journal = MelanJournal()
    journal.turn_into_data_frame([fetch("sample_3.txt")])
    pass

main()