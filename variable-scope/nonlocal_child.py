def outer():
    count = 0

    def inner():
        nonlocal count
        count += 2
        return count

    return inner


o = outer()

for i in range(10):
    print(o())