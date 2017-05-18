"""
Question:
Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
Suppose the following input is supplied to the program:
Hello world!
Then, the output should be:
UPPER CASE 1
LOWER CASE 9

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

def calculate_number_upper_lower(sentence):
    d = {'UPPER_CASE': 0, 'LOWER_CASE': 0}
    for s in sentence:
        if s.isupper():
            d['UPPER_CASE'] += 1
        elif s.islower():
            d['LOWER_CASE'] += 1
    return d

sentence = raw_input('Enter a sentence')

print calculate_number_upper_lower(sentence)

