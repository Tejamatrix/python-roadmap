students = [
    ("Teja",95),
    ("Rahul",80),
    ("Anjali",90)
]

students.sort(key = lambda x: x[1],reverse = True)

print(students)

#map

mapping = [1,2,3,4,5,6,7,8,9]
even = list(map(lambda x:x%2==0,mapping))
print(even)

#filter

filter11 = [2,3,1,4,5,3,56,7,8,9,0]

greater = list(filter(lambda x:x%10==0,filter11))
print(greater)

#reduce

reducer = [1,2,3,4,5,6,7,8,9]

additionall = reduce(lambda x,y:x+y,reducer)

print(additionall)