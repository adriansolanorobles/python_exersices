"""
Question:
Write a program that accepts a sentence and calculate the number of letters and digits.
Suppose the following input is supplied to the program:
hello world! 123
Then, the output should be:
LETTERS 10
DIGITS 3

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

sentence = raw_input("Enter a sencente: ")

count_digits = 0
count_char = 0

for s in sentence:
    if s.isdigit():
        count_digits += 1
    elif s.isalpha():
        count_char += 1

print 'LETTERS: %d' % (count_char)
print 'DIGITS: %d' % (count_digits)


