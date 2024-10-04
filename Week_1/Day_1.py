import math


    # Calculate area and circumference of circle


radius = float(input("Enter the radius of Circle: "))


area = math.pi * radius **2

circumference = 2 * math.pi * radius


# print(f"The area of circle is: {area}")
# print(f"The Circumference of circle is: {circumference}")


        # Table of math

table = int(input("Enter number to print table: "))

for i in range(1,11):
    print(table, "x", i, "=", i*table)