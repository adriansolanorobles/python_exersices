"""
Write a program that calculates and prints the value according to the given formula:
Q = Square root of [(2 * C * D)/H]
Following are the fixed values of C and H:
C is 50. H is 30.
D is the variable whose values should be input to your program in a comma-separated sequence.
"""
from math import sqrt
list_string = raw_input('Enter a comma-separated list of numbers')
list_d = list_string.split(',')
list_q = []
for d in list_d:
    list_q.append ( str(int(round(sqrt((2 * 50.0 * int(d)) / 30.0)))) )

print ','.join(list_q)