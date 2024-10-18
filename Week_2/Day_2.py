import math


# Mean of a List of Numbers

def calculate_mean(numbers):
    return sum(numbers) / len(numbers)



# Standard Deviation of a List of Numbers

def calculate_std_dev(numbers):
    mean = sum(numbers) / len(numbers)
    variance = sum((x - mean) ** 2 for x in numbers) / len(numbers)
    return math.sqrt(variance)


# Example usage:
numbers = [float(x) for x in input("Enter numbers separated by spaces: ")]
print(f"The standard deviation of the list is: {calculate_std_dev(numbers)}")



# Example usage:
numbers = [float(x) for x in input("Enter numbers separated by spaces: ")]
print(f"The mean of the list is: {calculate_mean(numbers)}")