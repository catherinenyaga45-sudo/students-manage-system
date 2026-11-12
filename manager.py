import json
from student import Student
from log import logger

class Manager:
    def __init__(self):
        self.students = self.load_students()

    #加载学生数据
    def load_students(self):
        try:
            with open('data/students.json', 'r', encoding='utf-8') as f:
                return json.load(f)

        except FileNotFoundError:
            return {}

    #保存学生数据
    def save_students(self):
        with open('data/students.json', 'w', encoding='utf-8') as f:
            json.dump(self.students, f, ensure_ascii=False, indent=4)

    #添加学生
    def add_student(self):
        name = input('请输入学生姓名：')
        age = input('请输入学生年龄：')
        grade = input('请输入学生年级：')
        if self.students:
            count = max(int(number[1:]) for number in self.students)
        else:
            count = 1
        self.students[f'P{count:03d}'] = Student(name, age, grade).__dict__
        for subject in self.studnents[f'P{count:03d}']['subjects_scores']:
            score = input(f'请输入{subject}成绩：')
            self.students[f'P{count:03d}']['subjects_scores'][subject] = int(score)
        logger.log('添加学生', name)
        self.save_students()

    #查找学生
    def find_student(self):
        stu_id = input('请输入学生学号(例：P001)：')
        for number in self.students:
            if number == stu_id:
                print(number, self.students[number])
                logger.log('查找学生', self.students[number]['name'])
                break
        else:
            print('未找到该学生')    
