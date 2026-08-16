from pypdf import PdfReader

reader = PdfReader("new.pdf")

content = ""

for file in reader.pages:
    content+=file.extract_text()

print(content)