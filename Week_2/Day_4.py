
"""
import pyttsx3,PyPDF2

#insert name of your pdf 
pdfreader = PyPDF2.PdfFileReader(open('book.pdf', 'rb'))
speaker = pyttsx3.init()

for page_num in range(pdfreader.numPages):
    text = pdfreader.getPage(page_num).extractText()
    clean_text = text.strip().replace('\n', ' ')
    print(clean_text)
#name mp3 file whatever you would like
speaker.save_to_file(clean_text, 'story.mp3')
speaker.runAndWait()

speaker.stop()
"""

        # Find the Second largest number in a list

def second_largest(numbers):
    numbers = list(set(numbers)) # Removing deplicates
    numbers.sort() # Sorting the list
    return numbers[-2] # Returning the second largest element


# Example usage:
numbers = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"The second largest number is: {second_largest(numbers)}")



    # Remove duplicates from a list

def remove_duplicates(lst):
    return list(set(lst))



# Example usage:
lst = [int(x) for x in input("Enter numbers separated by spaces: ").split()]
print(f"List after removing duplicates: {remove_duplicates(lst)}")




        # Check Armstrong Number

def is_armstrong(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digits) ** num_digits for digits in num_str)
    return sum_of_powers == number


# Example usage:
number = int(input("Enter a number: "))
if is_armstrong(number):
    print(f"{number} is a Armstrong number")
else:
    print(f"{number} is not a Armstrong number")
