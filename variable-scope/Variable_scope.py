a = 29

def sum(a,b):
    return a+b

result = sum(a,32)

print(result)

def calculation():
    c = 10
    print(c)

def outer_function():
    return c+21

print(outer_function())
print(calculation())
print(result)


# gloal variable declared outside functions and can be accessed inside functions
# local variable declared inside functions and can be accessed only inside that function