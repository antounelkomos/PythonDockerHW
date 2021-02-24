def addition(a, b):
    return a + b
def subtraction(a, b):
    return a - b
def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b
def square(a, b):
    return a ** b
def root(a, b):
    return b**(1/float(a))

class Calculator:
    result = 0

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
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
    def root(self, a, b):
        self.result = root(a, b)
        return self.result

