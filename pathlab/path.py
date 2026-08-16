from pathlib import path

file = path("data.txt")

with open("file","r") as lib:
    new = lib.read()

for a in new:
    print(a)