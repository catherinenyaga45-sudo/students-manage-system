import json

class Manager:
    def __init__(self):
        pass

    def load_students(self):
        try:
            with open('students.json', 'r', encoding='utf-8') as f:
                return json.load(f)

        except FileNotFoundError:
            return {}

    
