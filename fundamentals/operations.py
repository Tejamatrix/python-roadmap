def add_numbers(a, b):
    return a + b

def subtract_numbers(a, b):
    return a - b

def multiply_numbers(a, b):
    return a * b    

def divide_numbers(a,b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return a ** 0.5


add = add_numbers(1, 2)
subtract = subtract_numbers(1, 7)
multiply = multiply_numbers(2, 5)
divide = divide_numbers(3, 8)
square_root_result = square_root(91)

print("Addition:", add)
print("Subtraction:", subtract)
print("Multiplication:", multiply)
print("Division:", divide)
print("Square Root:", square_root_result)