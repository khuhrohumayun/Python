

    # Problem: Write a Python program to calculate the perimeter of a square.

def square_perimeter(side):
    return 4 * side



# Problem: Write a Python program to calculate simple interest.

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100



# Example usage: 

side = float(input("Enter the side length of the square: "))
print(f"Perimeter of the square: {square_perimeter(side)}")




# Example usage: 

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time in years: "))

print(f"Simple Interest: {simple_interest(principal,rate,time)}")

# After add interest 
remianing = principal + simple_interest(principal,rate,time)
print()
print(f"Your end balance is: {remianing}")