
a = lambda x: x + 10

z = [1,2,3,4,5,6,7,8,9]

students = [
    ("Teja", 95,2),
    ("Rahul", 80,3),
    ("Anjali", 90,1)
]

print(a(32))

sortd = sorted(students, key = lambda x:x[2])

b = lambda x,*args: x * sum(args)
c = lambda x,y,z: x + y + z
d = lambda x:x**x
e = lambda x:x%2
z = list(map(lambda x:x**2,z))
x = list(filter(lambda x:x>2,z))


print(b(2,3,4))
print(c(1,2,3))
print(d(2))
print(e(5))
print(z)
print(x)
print(sortd)