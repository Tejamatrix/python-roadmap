from pathlib import Path

file = Path("data.txt")

if file.exists():
    print("yes")
else:
    print("no")