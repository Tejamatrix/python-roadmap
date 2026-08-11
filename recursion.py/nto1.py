def infinite(n):
    if n == 0:
        return

    print(n)
    infinite(n-1)

infinite(100)