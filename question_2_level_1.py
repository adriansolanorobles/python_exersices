"""
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program:
"""

def factorial(n):
    if n == 1:
        return 1
    total = n * factorial(n-1)
    return total


if __name__ == "__main__":
    print(factorial(6))
