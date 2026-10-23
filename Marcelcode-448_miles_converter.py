# Miles to Kilometers Converter
# Student contribution for CSCI 101

TOOL_NAME = "Miles to Kilometers Converter"

def run():
    print("Welcome to the Miles to Kilometers Converter!")

    miles = float(input("Enter the number of miles: "))

    kilometers = miles * 1.60934

    print(miles, "miles is equal to", round(kilometers, 2), "kilometers.")