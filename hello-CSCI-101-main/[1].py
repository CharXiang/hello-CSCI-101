TOOL_NAME = "Grade Calculator" 

def  run():
    print("Welcome to the grade calculator!")
    score = float(input("Enter your score (0-100): "))
    if score >= 90:
        print("Your grade is A") 
    elif score >= 80:
        print("Your grade is B")
    elif score >= 70:
        print("Your grade is C") 
    elif score >= 60: 
        print("Your grade is D") 
    else: 
        print("Your grade is F")