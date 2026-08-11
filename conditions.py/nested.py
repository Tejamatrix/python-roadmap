age = 18
name = "teja"

has_id = True

if age >= 18:
    if has_id:
        print(f"{name}, you are eligible to vote.")
    else:
        print(f"{name}, you need an ID to vote.")
else:
    print("you are underage to vote.")