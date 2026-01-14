class Student:
    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score


number_of_students = int(input("Enter the number of students: "))
students = []
scores_male = []
scores_female = []

for i in range(number_of_students):

    student = Student(
        input(f"Enter the name of student {i + 1}: "),
        input(f"Enter the gender of student {i + 1}: "),
        float(input(f"Enter the score of student {i + 1}: "))
    )
    if student.score < 0 or student.score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        student.score = float(input(f"Re-enter the score of student {i + 1}: "))
    students.append(student)

    if students[i].gender == "male":
        scores_male.append(students[i].score)
    elif students[i].gender == "female":
        scores_female.append(students[i].score)

avr_male = round(sum(scores_male) / len(scores_male), 2)
avr_female = round(sum(scores_female) / len(scores_female), 2)

print(f"Average score for male students: {avr_male}")
print(f"Average score for female students: {avr_female}")
print(f"Average score for all students: {round((sum(scores_male) + sum(scores_female)) / number_of_students, 2)}")