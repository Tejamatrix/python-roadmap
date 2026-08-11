def combined(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)

    combined(1,2,3,4,5,6,7,8,9,name = "teja",age = 20,city = "hyderabad")