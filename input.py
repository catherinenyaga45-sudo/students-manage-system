#学生姓名，年龄，年级输入函数
def input_student_info():
    while True:
        name = input('请输入学生姓名：')
        if not name:
            print('姓名不能为空，请重新输入')
            continue
        break
    while True:
        age = input('请输入学生年龄：')
        if not age.isdigit() or int(age) <= 0:
            print('年龄必须为正整数，请重新输入')
            continue
        break
    while True:
        grade = input('请输入学生年级：')
        if not grade:
            print('年级不能为空，请重新输入')
            continue
        break
    return name, age, grade


#科目成绩输入函数
def input_subject_scores(students, student_id):
    while True:
        in_subject = input('请输入要修改的科目(语文/数学/英语)  (输入q退出)：')
        if in_subject == 'q':
            break
        for subject in students[student_id]['subjects_scores']:
            if subject == in_subject:
                while True:
                    try:
                        in_score = input('请输入新的成绩：')
                        students[student_id]['subjects_scores'][subject] = int(in_score)
                        print('成绩修改成功')
                        break
                    except ValueError:
                        print('请输入有效的成绩')
                break
        else:
            print('未找到该科目')

    return students