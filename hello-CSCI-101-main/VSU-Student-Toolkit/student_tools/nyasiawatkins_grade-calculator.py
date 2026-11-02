TOOL_NAME = "Grade Calculator"

def run():
    print("The Greatest Grade Calculator")
    score = float(input("Enter score: "))
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"Thy grade is: {grade}")