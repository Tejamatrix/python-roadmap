def counter():
    count = 1

    def increment():
        nonlocal count
        count += 1
        print(count)

    return increment


c = counter()

c()
c()
c()
c()