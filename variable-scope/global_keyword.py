x = 120

def global_variable():
    global x
    x = 321
    print(x)

print(x)
global_variable()