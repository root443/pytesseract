import re
from tesseract.settings import *

def writing(filename, text):
    if re.search(r"\.docx", filename):
        writingdocx(filename=filename, content=text)
    else:
        writingtxt(filename=filename, content=text)

def writingdocx(filename, content):
    from docx import Document
    from docx.oxml.ns import qn

    document = Document()
    document.add_paragraph(content)
    section = document.sections[0]

    sectPr = section._sectPr
    cols = sectPr.xpath('./w:cols')[0]
    cols.set(qn('w:num'), '2')
    document.save('{d}{f}'.format(d=FOLDER_OUT, f=filename))

def writingtxt(filename, content):
    with open('{d}{f}.txt'.format(d=FOLDER_OUT, f=filename), 'wb') as f:
        f.write(content.encode())
