from docx import Document

def text_extractor(file_path):
    docx_file = Document(file_path)
    docx_file=' '.join([p.text for p in docx_file.paragraphs])
    return docx_file