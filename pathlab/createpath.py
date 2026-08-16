from pathlib import Path

folder = Path("teja.txt")

if folder.exists:
    print("yes")
else:
    folder.mkdir()

folder.mkdir()