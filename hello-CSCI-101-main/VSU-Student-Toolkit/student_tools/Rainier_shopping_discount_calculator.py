TOOL_NAME = "Shopping Discount Calculator"


def run():
      print("Enter price")
price = float(input("Enter your price: "))
if price <= 50:
      print(price)
else:
      print("Discount")
      total = price - 5
      print("total cost", total)