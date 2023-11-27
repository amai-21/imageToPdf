# Python3 program to convert iage to pdf
# using img2pdf library

import os
from PIL import Image # pip install pillow
import img2pdf

#storing image path
img_path = r"C:\Users\andre\Pictures\Screenshots\codingRelatedImages\violinPicture2.jpg"

# storing pdf path
pdf_path = r"C:\Users\andre\Pictures\Screenshots\codingRelatedImages\violinPicture2.pdf"

# opening image
image = Image.open(img_path)

# converting into chunks using img2pdf
pdf_bytes = img2pdf.convert(image.filename)

# opening or creating pdf file
file = open(pdf_path, "wb")

# writing pdf files with chunks
file.write(pdf_bytes)

# closing image file
image.close()

# closing pdf file
file.close()

# output
print("Successfully made pdf file")


