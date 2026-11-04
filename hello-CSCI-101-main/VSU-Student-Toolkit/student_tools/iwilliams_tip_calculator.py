
TOOL_NAME = "Tip Calculator"

def run():
    print("Welcome to the Tip Calculator!")

    bill = float(input("Enter the total bill amount ($): "))
    tip_percentage = float(input("Enter the tip percentage (e.g., 15, 18, 20): "))

    tip_amount = bill * (tip_percentage / 100)
    total_amount = bill + tip_amount

    print(f"Tip: ${tip_amount:.2f}")
    print(f"Total to pay: ${total_amount:.2f}")


run()
