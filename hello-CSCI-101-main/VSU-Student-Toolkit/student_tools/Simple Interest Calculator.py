tool_kit = Simple Interest Calculator
def run():
    def calculate_simple_interest(principal, rate, time):
    
    return (principal * rate * time) / 100
 
# User input
P = float(input('Enter principal amount: '))
R = float(input('Enter rate of interest: '))
T = float(input('Enter time in years: '))
 
# Calculate interest
interest = calculate_simple_interest(P, R, T)
print(f'Simple Interest: {interest}')
