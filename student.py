class student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = grade
        self.subjects_scores = {}