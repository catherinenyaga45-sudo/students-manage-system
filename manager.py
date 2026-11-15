import json
from student import Student
from log import logger
from input import input_student_info, input_subject_scores

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
        name, age, grade = input_student_info()
        if self.students:
            count = max(int(number[1:]) for number in self.students)
        else:
            count = 0
        self.students[f'P{count+1:03d}'] = Student(name, age, grade).__dict__
        for subject in self.students[f'P{count+1:03d}']['subjects_scores']:
            score = input(f'请输入{subject}成绩：')
            self.students[f'P{count+1:03d}']['subjects_scores'][subject] = int(score)
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

    #修改学生成绩
    def update_student_score(self):
        stu_id = input('请输入学生学号(例：P001)：')
        for number in self.students:
            if number == stu_id:
                self.students = input_subject_scores(self.students, number)
                logger.log('修改学生成绩', self.students[number]['name'])
                self.save_students()

    #删除学生
    def delete_student(self):
        stu_id = input('请输入学生学号(例：P001)：')
        target = None
        for number in self.students:
            if number == stu_id:
                target = number
                break
        if target:
            del self.students[target]
            logger.log('删除学生', self.students[target]['name'])
            self.save_students()
        else:
            print('未找到该学生')

    #查看所有学生
    def show_all_students(self):
        for number in self.students:
            print(number, self.students[number])
        logger.log('查看所有学生')

    #运行程序
    def run(self):
        while True:
            print('1. 添加学生')
            print('2. 查找学生')
            print('3. 修改学生成绩')
            print('4. 删除学生')
            print('5. 查看所有学生')
            print('6. 退出程序')
            choice = input('请输入操作编号：')
            if choice == '1':
                self.add_student()
            elif choice == '2':
                self.find_student()
            elif choice == '3':
                self.update_student_score()
            elif choice == '4':
                self.delete_student()
            elif choice == '5':
                self.show_all_students()
            elif choice == '6':
                break
            else:
                print('无效的操作编号，请重新输入')

manager = Manager()