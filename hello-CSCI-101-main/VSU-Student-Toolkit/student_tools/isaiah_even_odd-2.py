TOOL_NAME = "Even or Odd Checker"

def run():
    print("Welcome to the Even or Odd Checker!")
    number = int(input("Enter a whole number: "))
    if number % 2 == 0:
        print("Your number is even.")
    else:
        print("Your number is odd.")

if __name__ == "__main__":
    run()
