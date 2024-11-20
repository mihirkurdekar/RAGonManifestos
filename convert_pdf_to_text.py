from PyPDF2 import PdfReader

reader = PdfReader("manifestos/MVA-Manifesto-English.pdf")
text = ""
for page in reader.pages:
    text += page.extract_text()
with open("manifestos/mva-manifesto.txt", "w") as f:
    f.write(text)
