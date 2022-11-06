"""Save text to a txt file"""
import os
import datetime

def save_text(text):
    filename = os.path.join("./Diary_inputs/", str(datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S")) + ".txt")
    print(filename)
    with open(filename, 'w') as file:
        file.write(text)