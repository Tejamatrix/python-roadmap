from pathlib import Path

folder = Path("body.txt")

folder.touch()
folder.write_text("python\nis a machine learning\nlanguage")