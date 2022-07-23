def grade(score):
    if score >= 95:
        grade = "학점:A+"
    elif score >= 90:
        grade = "학점:A"
    elif score >= 85:
        grade = "학점:B+"
    elif score >= 80:
        grade = "학점:B"
    elif score >= 75:
        grade = "학점:C+"
    elif score >= 70:
        grade = "학점:C"
    elif score >= 65:
        grade = "학점:D+"
    elif score >= 60:
        grade = "학점:D"
    else:
        grade = "학점:F"
    return grade

name = input("이름:")
score = int(input("점수:"))
print(grade(score))