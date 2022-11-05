"""A NLP based Diary. Two"""
# Capturing settings.
import datetime
import pandas as pd

class MelanJournal():
    reminder_time: datetime
    new_user: True
    data: pd.DataFrame
    def __init__(self):
        """Runs upon restarting the program."""
        if self.new_user == True:
            self.settings()
            self.new_user = False
            self.data = pd.DataFrame(columns = ["datetimes", "entry"])


    def settings(self) -> None:
        """Sets or changes the settings."""
        self.reminder_time = "placeholder, replace with datetime object"

    
    def turn_into_data_frame(self) -> None:
        pass


def main() -> None:
    journal = MelanJournal()
    pass