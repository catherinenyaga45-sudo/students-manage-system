class Student:
    #初始化
    def __init__(self, name, age, grade):
        self.name = name
        self.age = int(age)
        self.grade = grade
        self.subjects_scores = {'语文': 0, '数学': 0, '英语': 0}