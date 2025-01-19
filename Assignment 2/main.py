# ================================== Grading System Using If-Else Statements ==================================


totalMarks = 500
obtMarks = 349

percentage = (obtMarks / totalMarks) * 100
print(f"{percentage}%")

if percentage >= 80:
    print("Grade A+")
elif percentage >= 70:
    print("Grade A")
elif percentage >= 60:
    print("Grade B")
elif percentage >= 50:
    print("Grade C")
elif percentage >= 40:
    print("Grade D")
else:
    print("Fail")