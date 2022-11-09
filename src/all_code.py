import pytesseract
from PIL import Image
import re
import pandas as pd
import os

pytesseract.pytesseract.tesseract_cmd=r'C:\Program Files\Tesseract-OCR\tesseract.exe'

name = []
date = []
qty = []
fat = []
snf = []
rate = []
amount = []
images = []

dirname = r'src\data'

# get file path for all the images
def get_file_paths(dirname):
    for root, directories, files in os.walk(dirname):
            for filename in files:
                filepath1 = os.path.join(root, filename)
                images.append(filepath1)
    return images

# extract text from image
def get_text(img):
    img = Image.open(img)
    text = pytesseract.image_to_string(img, lang='eng')
    return text


# get name
def get_name(text):
    pattern = 'Name:(.*)'

    matches = re.findall(pattern, text)
    name = re.findall('\d',matches[0].strip())
    name = ''.join(name)
    return(name[-2:])

def get_date(text):
    pattern = '\d{2}-\d{2}-\d{4}'
    matches = re.findall( pattern, text)
    return(matches[0].strip())

def get_qty(text):
    pattern = 'Total Qty\(Lt\) : (.*)'

    matches = re.findall(pattern, text)
    return matches[0].strip()

def get_fat(text):
    pattern = 'Aug. Fat : (.*)'

    matches = re.findall(pattern, text)
    return matches


def get_snf(text):
    pattern = 'Avg. SNF : (.*)'

    matches = re.findall(pattern, text)
    return matches

def get_rate(text):
    pattern = 'Avg Rate : (.*)'

    matches = re.findall(pattern, text)
    return matches

def get_amount(text):
    pattern = 'Total Parount : (.*)'

    matches = re.findall(pattern, text)
    return matches

# get all information in list
def get_all(text):
    name.append(get_name(text))
    date.append(get_date(text))
    qty.append(get_qty(text))
    fat.append(get_fat(text))
    snf.append(get_snf(text))
    rate.append(get_rate(text))
    amount.append(get_amount(text))
    return name, date, qty, fat, snf, rate, amount

def conv_to_dict(name, date, qty, fat, snf, rate, amount):
    return {
        'Name': name,
        'Date': date,
        'Total Quantity' : qty,
        'Fat' : fat,
        'SNF' : snf,
        'Average Rate' : rate,
        'Total Amount' : amount
        
    }

def get_all_info(dirname):
    images = get_file_paths(dirname)
    for img in images:
        text = get_text(img)
        name, date, qty, fat, snf, rate, amount = get_all(text)
    data = conv_to_dict(name, date, qty, fat, snf, rate, amount)
    df = pd.DataFrame(data)
    return df

all_info = get_all_info(dirname)
print(all_info)