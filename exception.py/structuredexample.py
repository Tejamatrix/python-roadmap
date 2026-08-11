def process_user(user):
    try:
          name = user["name"]
          age = int(user["age"])
          score = int(user["score"])
          print(f"name is {name} and age is {age} acquired score is {score}")
    except KeyError:
         print(f"the key isnt available right now")
    except ValueError:
         print("value didnt match")
    finally:
         print("done execution")

process_user(user = {
    "name": "Teja",
    "age": 20,
    "score": "95"
})

try:
     process_user(user = {
    "name": "eeja",
    "age": 50,
    "score": "95"
})
     print("a")
except:
     print("b")
finally:
     print("c")
