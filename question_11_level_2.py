"""
Question:
Write a program which accepts a sequence of comma separated 4 digit binary 
numbers as its input and then check whether they are divisible by 5 or not. T
he numbers that are divisible by 5 are to be printed in a comma separated sequence.
Example:
0100,0011,1010,1001
Then the output should be:
1010
Notes: Assume the data is input by console.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
digit_binary = raw_input("Enter a sequence of comma separated 4 digit binary: ")
list_digit_binary = digit_binary.split(',')
list_divisible_by_5 = []
for l in list_digit_binary:
    if int(l,2) % 5 == 0:
        list_divisible_by_5.append(l)

print ','.join(list_divisible_by_5)
