import PyPDF2
import pandas as pd
import os
from docx import Document
import csv
import xlrd

def pdf_to_text(pdf_file):
    text = ""
    with open(pdf_file, 'rb') as f:
        pdf_reader = PyPDF2.PdfFileReader(f)
        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            text += page.extractText()
    return text

def docx_to_text(docx_file):
    doc = Document(docx_file)
    text = ""
    for para in doc.paragraphs:
        text += para.text + '\n'
    return text

def excel_to_csv(excel_file, csv_file):
    wb = xlrd.open_workbook(excel_file)
    sheet = wb.sheet_by_index(0)
    with open(csv_file, 'w', newline='') as f:
        writer = csv.writer(f)
        for row_num in range(sheet.nrows):
            writer.writerow(sheet.row_values(row_num))

def convert_document(input_file, output_file):
    file_ext = os.path.splitext(input_file)[1].lower()
    if file_ext == '.pdf':
        text = pdf_to_text(input_file)
        with open(output_file, 'w') as f:
            f.write(text)
    elif file_ext == '.docx':
        text = docx_to_text(input_file)
        with open(output_file, 'w') as f:
            f.write(text)
    elif file_ext == '.xlsx':
        excel_to_csv(input_file, output_file)
    else:
        print("Unsupported file format")

if __name__ == "__main__":
    input_file = input("Enter the path of the input file: ")
    output_file = input("Enter the path of the output file: ")
    convert_document(input_file, output_file)
