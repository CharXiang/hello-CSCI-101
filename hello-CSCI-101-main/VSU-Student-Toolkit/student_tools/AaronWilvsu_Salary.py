TOOL_NAME = "Salary Checker" 

def run():
    hours = float(input("How many hours?"))
    rates = int(input("What is your rate?"))

    salary = hours * rates

    print(f"If you work {hours} hours and your rate is {rates} an hour, your salary will be {salary} dollars.")