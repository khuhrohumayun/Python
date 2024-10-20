
        # Multiplication Table

def multiplication_table(num):
    for i in range(1,11):
        print(f"{num} x {i} = {num*i}")




    # Count Words in a Sentence

def count_words(sentence):
    words = sentence.split()
    return len(words)



    # Reverse a String 

def reverse_string(string):
    return string[::-1]





# Example usage:
string = input("Enter a string: ")
print(f"Reversed string: {reverse_string(string)}")



# Example usage: 
sentence = input("Enter a sentence: ")
print(f"Number of words: {count_words(sentence)}")


# Example usage:
num = int(input("Enter a number: "))
multiplication_table(num)