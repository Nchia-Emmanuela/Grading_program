Student_Scores = {
    "Harry": 81,
    "Peter": 99,
    "Serge": 71,
    "Ron" : 78,
    "Boris": 64,
    "George": 87,
}

Student_Grade = {}

for Student in Student_Scores:
    score = Student_Scores[Student]
    if score > 90:
        Student_Grade[Student] = 'Outstanding'
    elif score > 80:
        Student_Grade[Student] = 'Exceeds Expectations'
    elif score > 70:
        Student_Grade[Student] = 'Acceptable'
    else:
        Student_Grade[Student] ='Fail'

print(Student_Grade)