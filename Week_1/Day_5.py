# Problem: Write a Python program to print the Fibonacci sequence up to n terms.

def fibonacci(n):
    sequence = [0,1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]




# Problem: Write a Python program to reverse a number.

def reverse_number(num):
    reverse_num = 0
    while num > 0:
        digit = num % 10
        reverse_num = reverse_num * 10 + digit
        num //= 10
    return reverse_num




# Problem: Write a Python program to find the least common multiple (LCM) of two numbers.

def gcd(a,b):
    while b:
        a, b = b, a % b
    return a

def lcm(a,b):
    return (a*b) // gcd(a,b)





# Example usage:
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(f"LCM of {a} and {b}: {lcm(a,b)}")


# Example usage:
num = int(input("Enter a number: "))
print(f"Reversed number: {reverse_number(num)}")





# Example usage:
n = int(input("Enter the number of terms in the fibonacci sequance: "))
print(f"Fibonacci sequence up to {n} terms: {fibonacci(n)}")