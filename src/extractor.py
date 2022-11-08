from PIL import Image
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'


def extract(file_path):
    # step 1: extracting text from image
    img = Image.open(file_path)
    document_text = pytesseract.image_to_string(img, lang='eng')
    return document_text

if __name__ == '__main__':
    data = extract(r'src\data\new.jpg')
    print(data)