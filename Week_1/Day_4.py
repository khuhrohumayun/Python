# Problem: Write a Python program to find the sum of the first N natural numbers.


def sum_natural_numbers(n):
    return n * (n+1) // 2



# Problem: Write a Python program to find the factorial of a number.

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)


# Problem: Write a Python program to check whether a number is prime or not.

def is_Prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True



# Example usage:
num = int(input("Enter a number: "))
if is_Prime(num):
    print(f"{num} is a prime number")
else:
    print(f"{num} is not prime number")




# Example usage:
n = int(input("Enter a number: "))
print(f"Factorail of {n} is {factorial(n)}")




# Example usage:
n = int(input("Enter a positive integer: "))
print(f"Sum of the first {n} natural numbers: {sum_natural_numbers(n)}")