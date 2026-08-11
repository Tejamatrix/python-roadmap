p = 32

square = lambda x: x**2 

print(square(5)) 

addition = lambda x:x+x

print(addition(5))

addition = lambda x,y:x+y**2

print(addition(5,6))

subtract = lambda x:x-p
if subtract(5)<0:
    print("negative")