# Problem: Write a Python program to find the greatest of three numbers.

def greatest_of_three(a,b,c):
    return max(a,b,c)



# Problem: Write a Python program to check if a number or string is a palindrome.

def is_palindrome(value):
    value_str = str(value)
    return value_str == value_str[::-1]



# Example usage:
value = input("Enter a number or string: ")
if is_palindrome(value):
    print(f"{value} is a palindrome")
else:
    print(f"{value} is not a palindrome")

    

# Example usage: 
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))
c = float(input("Enter the third number: "))
print(f"The greatest number is: {greatest_of_three(a,b,c)}")
