import transformers
import os
import json
from datasets import Dataset

def load_data_from_folder(folder_path):
    data_files = os.listdir(folder_path)
    data = []
    for file_name in data_files:
        file_path = os.path.join(folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            item = json.load(file)
            data.append(item)
    return data

def load_syllabus_dataset():
    folder_path = os.path.join("..", "syllabuses")
    data = load_data_from_folder(folder_path)

    dataset = Dataset.from_dict({"json": item for item in data})
    return dataset

