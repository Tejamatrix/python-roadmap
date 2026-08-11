def outer():

    x = 10

    def inner():
        nonlocal x
        x = 11
    inner()

    print(x)

outer()
