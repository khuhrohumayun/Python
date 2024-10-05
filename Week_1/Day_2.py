
    # Problem: Write a Python program to check if a number is even or odd.

def check_Even_Odd(number):

    if number % 2 == 0:

        return 'even'

    else:

        return 'odd'




    # Problem: Write a Python program to print Alphabait traingle

def alphabait_triangle(n):

    num = 0

    for i in range(1, n + 1):

        for j in range(1, i + 1):

            print(chr(65 + num), end=' ')

            num += 1
        print()




   # Problem: Write a Python program to convert Celsius to Fahrenheit.

def Celsius_To_Fahrenheit(celsius):
    return (celsius * 9/5) + 32






    # Printing alphabait using loop

num = (int(input("Enter number to print alphabetical triangle: ")))

alphabait_triangle(num)





        # Check number even or odd

number = int(input("Enter number: "))

print(f"The number is {check_Even_Odd(number)}")



    # Example: Usage:

celsius = int(input("Enter tempreture in Celcius: "))

print(f"Tempreture in fahrenheit {Celsius_To_Fahrenheit(celsius)}")