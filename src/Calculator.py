import math

def addition(a, b):
    return a + b
#You see whathadhabbenwaz
def deco_func(func,*args):
    try:
        return func(*args)
    except:
        print("Error occured")
        return None


def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def square(a, b):
    return a ** b
def root(a):
    return math.sqrt(a)

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = deco_func(addition,a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result
    def multiplication(self, a, b):
        self.result = multiplication(a, b)
        return self.result
    def division(self, a, b):
        self.result = division(a, b)
        return self.result
    def square(self, a, b):
        self.result = square(a, b)
        return self.result
    def root(self, a):
        self.result = root(a)
        return self.result

