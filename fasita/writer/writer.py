import re
from fasita.settings import *


def writing(filename, text):
    if re.search(r"\.docx", filename):
        writingdocx(filename=filename, content=text)
    else:
        writingtxt(filename=filename, content=text)

def writingdocx(filename, content, column=0):
    from docx import Document
    from docx.oxml.ns import qn

    document = Document()
    paragraph = document.add_paragraph(text=content)

    if column > 0:
        section = document.sections[0]
        cols = section._sectPr.xpath('./w:cols')[0]
        cols.set(qn('w:num'), column)
    document.save('{d}/{f}'.format(d=FOLDER_OUT, f=filename))

def writingtxt(filename, content):
    with open('{d}/{f}.txt'.format(d=FOLDER_OUT, f=filename), 'wb') as f:
        f.write(content.encode())
