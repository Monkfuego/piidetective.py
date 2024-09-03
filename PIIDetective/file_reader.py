import os
from docx import Document
import PyPDF2
from pdfminer.high_level import extract_text as pdfminer_extract_text
from bs4 import BeautifulSoup
from PIL import Image
import pytesseract

def read_text_from_file(file_path):
    ext = os.path.splitext(file_path)[1].lower()
    
    if ext == '.txt':
        return read_text_from_txt(file_path)
    elif ext == '.docx':
        return read_text_from_docx(file_path)
    elif ext == '.pdf':
        return read_text_from_pdf(file_path)
    elif ext == '.html' or ext == '.htm':
        return read_text_from_html(file_path)
    elif ext in ['.jpg', '.jpeg', '.png', '.bmp', '.tiff', '.gif']:
        return read_text_from_image(file_path)
    else:
        raise ValueError(f"Unsupported file extension: {ext}")

def read_text_from_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def read_text_from_docx(file_path):
    doc = Document(file_path)
    text = '\n'.join([para.text for para in doc.paragraphs])
    return text

def read_text_from_pdf(file_path):
    text = ""
    try:
        with open(file_path, 'rb') as file:
            reader = PyPDF2.PdfFileReader(file)
            for page_num in range(reader.getNumPages()):
                text += reader.getPage(page_num).extractText()
        if not text.strip():  # If PyPDF2 fails, use pdfminer
            text = pdfminer_extract_text(file_path)
    except Exception as e:
        text = pdfminer_extract_text(file_path)
    return text

def read_text_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')
        return soup.get_text()

def read_text_from_image(file_path):
    image = Image.open(file_path)
    text = pytesseract.image_to_string(image)
    return text
