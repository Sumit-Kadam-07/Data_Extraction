import os
import pdfplumber
import re
from nltk.tokenize import word_tokenize
import pandas as pd
from datetime import datetime

###### IMPORT Specific Extracing Functions ######
from coursera import extract_coursera
from internshala import extract_internshala
from techedu import extract_techedu
from coretechtive import extract_coretechtive
from udemy import extract_udemy

def get_files():
    dir_name = os.getcwd()
    dir_name += "\certificates\\"

    files = os.listdir(dir_name)
    files = [(dir_name + file) for file in files if file.endswith('.pdf')]
    return files

def get_ocr(file):
    ocr_result = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            ocr_result = page.extract_text()
    return ocr_result

def store_excel(filename, rows, columns):
    df = pd.DataFrame(rows, columns=columns)
    df.to_excel(filename, index=False)

files = get_files()
data = []

for file in files:
    ocr_result = get_ocr(file)

    txt = ocr_result
    name1='all the best for future endeavours'
    name2='Training Completion Certificate'
    name3='IS PROUDLY PRESENTED'
    name4='online non'

    p = re.search(f"{name1}",txt)
    q = re.search(f"{name2}",txt)
    r = re.search(f"{name3}",txt)
    s = re.search(f"{name4}",txt)

    if p:
        print("Internshala")
        row = extract_internshala(ocr_result)
        data.append(row)

    if q:
        print("Coretechtive")
        row = extract_coretechtive(ocr_result)
        data.append(row)

    if r:
        print("Techedu")
        attributes = extract_techedu(ocr_result)
        data.append(row)

    if s:
        print("coursera")
        row = extract_coursera(ocr_result)
        data.append(row)
        
    


filename = "certificates.xlsx"
column_names = ['Name of the Student', 'Date of Certification', 'Course Name']
store_excel(filename=filename, rows=data, columns=column_names)
    
    # here we have to return three fields(name,course,etc.) from specific functions eg.extract_internshala()

