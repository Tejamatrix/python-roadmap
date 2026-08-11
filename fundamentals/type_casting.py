age = "21"

integerconversion = int(age)

print(type(integerconversion))
print(type(age))

# ====================================

age = 21

stringconversion = str(age)

print(type(stringconversion))
print(type(age))

#========================================

age = input("Enter your age: ")
name = int(input("Enter your name: "))

new_name = str(name)
new_age = int(age)

print(f"{new_name}, you are {new_age} years old.")
