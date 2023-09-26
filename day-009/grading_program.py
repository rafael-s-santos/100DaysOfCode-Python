student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
# 🚨 Don't change the code above 👆

# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇


def create_grade_dictionary_by_student(dictionary):
    for key in dictionary:
        if dictionary[key] >= 91:
            student_grades[key] = "Outstanding"
        elif dictionary[key] >= 81:
            student_grades[key] = "Exceeds Expectations"
        elif dictionary[key] >= 71:
            student_grades[key] = "Acceptable"
        else:
            student_grades[key] = "Fail"


create_grade_dictionary_by_student(student_scores)

# 🚨 Don't change the code below 👇
print(student_grades)
