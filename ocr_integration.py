import pytesseract
from PIL import Image
import fitz  # PyMuPDF
import io

def extract_text_from_images(pdf_bytes):
    document = fitz.open(stream=pdf_bytes, filetype="pdf")
    text = ""
    for page_num in range(len(document)):
        page = document.load_page(page_num)
        image_list = page.get_images(full=True)
        for img_index, img in enumerate(image_list):
            xref = img[0]
            base_image = document.extract_image(xref)
            image_bytes = base_image["image"]
            image = Image.open(io.BytesIO(image_bytes))
            text += pytesseract.image_to_string(image)
    return text
