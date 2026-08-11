try:
    x = 10
    print(x/0)

except ZeroDivisionError:
    print("cant div by 0")
finally:
    print("always executes")