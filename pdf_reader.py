from pypdf import PdfReader
import re 

def read_extract(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for pages in reader.pages:

        page_text = pages.extract_text()
        
        if page_text:
            text += page_text

    text = text.replace("\n" , " ")

    text = re.sub(r"\s+", " ", text)

    return text