import random
import os


def load_txt(file_path: str) -> list:
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = [line.rstrip('\n') for line in file]
            return content
    except FileNotFoundError:
        print("File not found or path is incorrect.")
    except IOError:
        print("Error reading.")
        
        
def seed_everything(seed_value: int) -> None:
    random.seed(seed_value)
    os.environ["PYTHONHASHSEED"] = str(seed_value)