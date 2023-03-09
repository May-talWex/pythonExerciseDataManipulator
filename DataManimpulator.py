import json
from pathlib import Path
from datetime import datetime


def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y/%m/%d %H:%M:%S").strftime('%Y/%m/%d %H:%M:%S'):
            raise ValueError
        return True
    except ValueError:
        return False


class DataManipulator:
    def __init__(self, file_path):
        self.file_path = file_path
        try:
            with file_path.open() as file:
                json_data = json.load(file)
            self.data = json_data
        except ValueError:
            print("Bad input")

    def process_data(self):
        for key, value in self.data.items():
            if isinstance(value, list):
                self.data[key] = list(set(value))
            elif validate(value):
                self.data[key] = value.replace(value[0: 4], "2021", 1)
            elif isinstance(value, str):
                self.data[key] = value[::-1].replace(" ", "")

    def save_data(self):
        with self.file_path.open("w") as file:
            json.dump(self.data, file, indent=4)
