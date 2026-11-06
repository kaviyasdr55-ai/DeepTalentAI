import PyPDF2
from docx import Document

def extract_resume_text(file_path):
    text = ""

    if file_path.lower().endswith(".pdf"):
        with open(file_path, "rb") as file:
            reader = PyPDF2.PdfReader(file)

            for page in reader.pages:
                text += page.extract_text() or ""

    elif file_path.lower().endswith(".docx"):
        doc = Document(file_path)

        for paragraph in doc.paragraphs:
            text += paragraph.text + "\n"

    elif file_path.lower().endswith(".txt"):
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()

    return text
