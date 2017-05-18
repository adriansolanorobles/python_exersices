"""
Question:
Write a program that computes the value of a+aa+aaa+aaaa with a given digit as the value of a.
Suppose the following input is supplied to the program:
9
Then, the output should be:
11106

9+99+999+9999


Hints:
In case of input data being supplied to the question, it should be assumed to be a console input.
"""
def computes_aaa(v,r):
    list_aaa = []
    s = ''
    for i in range(4):
        s = str(v) + s
        list_aaa.append(int(s))
    return sum(list_aaa)

print computes_aaa(9,4)
