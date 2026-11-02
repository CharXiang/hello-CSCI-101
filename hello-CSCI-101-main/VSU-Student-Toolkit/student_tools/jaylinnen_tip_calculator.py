# Tip Calculator

bill = float(input("Enter the total bill: $"))
tip_percent = float(input("Enter the tip percentage: "))

tip = bill * (tip_percent / 100)
total = bill + tip

print("\n--- Tip Calculator ---")
print(f"Bill Amount: ${bill:.2f}")
print(f"Tip Amount: ${tip:.2f}")
print(f"Total Amount: ${total:.2f}")
