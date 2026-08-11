user_name = "teja"
user_age = 18

try:
    print(f"{user_age}+{user_name}this is details")
except:
    if user_age < 20:
        print("under age")
finally:
    print("everything is done")