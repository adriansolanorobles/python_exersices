"""
Define a class which has at least two methods:
getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
"""

class InputString():
    def __init__(self):
        self.s = ""
    
    def getString(self):
        self.s = raw_input("Introduce tu nombre")
    
    def printString(self):
        print self.s.upper()

if __name__ == "__main__":
    i = InputString()
    i.getString()
    i.printString()