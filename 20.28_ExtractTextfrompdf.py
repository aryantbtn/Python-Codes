# You must have to collect text from pdf as a Python developer. This skill is useful when woring with resumes. Extracting text from a pdf file is not a difficult task at all. For this task, you need to install a Python library known as PyPDF2.
# Updated Code:
import PyPDF2
pdf = open("Questionbank.pdf", "rb")
reader = PyPDF2.PdfReader(pdf)
page_reading = reader.pages[0]
text = page_reading.extract_text()
print(text)
pdf.close()