import PyPDF2

pdf_path = r'C:\Users\MSI\OneDrive\文件\Downloads\賴聖元.pdf'

with open(pdf_path, 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    text = ''
    for page in reader.pages:
        text += page.extract_text() + '\n'

print(text)