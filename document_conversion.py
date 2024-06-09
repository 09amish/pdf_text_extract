import fitz  # PyMuPDF

def convert_pdf_to_text(pdf_bytes):
    document = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        text += page.get_text()
    return text
