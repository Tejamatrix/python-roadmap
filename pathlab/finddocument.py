from pathlib import Path

folder = Path("pathlab")


for file in folder.glob("*.txt"):
    print(file)