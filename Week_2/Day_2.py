
    # Count Vowels in a String 

"""
# Create function to count vowels in a String
def count_vowels(string):
    vowel = 'aeiouAEIOU'
    count = sum(1 for char in string if char in vowel)
    return count



# Example usage: 
string = input("Enter a string: ")
print(f"Number of vowels: {count_vowels(string)}")
"""


    # Find the largrest Number in a list 

"""
# Create funciton for find largest
def find_largest(numbers):
    return max(numbers)


# Example Usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"The largest number is: {find_largest(numbers)}")
"""



    # Check if a String is a Palindrome

"""
# create function to check palindrome
def is_palindrome(string):
    return string == string[::-1]


# Example usage:
string = input("Enter a string: ")
if is_palindrome(string):
    print(f"{string} is a palindrome")
else:
    print(f"{string} is not a palindrome")
"""


def is_palindrome(value):
    value_str = str(value)
    return value_str == value_str[::-1]


value = int(input("Enter number: "))

if is_palindrome(value):
    print(f"{value} is a palindrome")
else:
    print(f"{value} is not palindrome")