"""
Question:
Write a program, which will find all such numbers between 1000 and 3000 (both included)
 such that each digit of the number is an even number.
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.

"""

def find_even_in_sequence(a,b):
    list_even_numbers = []
    for n in range(a,b+1):
        s = str(n)
        if int(s[0]) % 2 == 0 and int(s[1]) % 2 == 0 and int(s[2]) % 2 == 0 and int(s[3]) % 2 == 0:
            list_even_numbers.append(s)
    return list_even_numbers

print ','.join(find_even_in_sequence(1000,3000))




            
        
