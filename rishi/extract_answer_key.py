# import PyPDF2

# # creating a pdf file object
# pdfFileObj = open('misc/resized2.pdf', 'rb')

# # creating a pdf reader object
# pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# # printing number of pages in pdf file
# print('# ', pdfReader.numPages)

# # print(pdfReader)

# # creating a page object
# pageObj = pdfReader.getPage(0)

# # extracting text from page
# print('Text ', pageObj.extractText())

# # closing the pdf file object
# pdfFileObj.close()

######

# import pdfminer

# local_pdf_filename = "misc/resized2.pdf"
# pages = [0]  # just the first page

# extracted_text = pdfminer.high_level.extract_text(
#     local_pdf_filename, "", pages)
# print(extracted_text)


import slate3k as slate
import re

with open('misc/resized2.pdf', 'rb') as f:
    extracted_text = slate.PDF(f)

txt = ''.join(extracted_text)

print(txt)

matches = re.findall("Q [0-9]+.[A-D]", txt)

print(matches)
