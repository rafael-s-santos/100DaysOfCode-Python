import random
names = ["Alex", "Beth", "Caronline", "Dave", "Elanor", "Freddie"]


# students_score = [new_key:new_value for item in list]
students_score = {student:random.randint(1, 100) for student in names}
passed_students = {student:score for (student, score) in students_score.items() if score >= 60}

print(passed_students)