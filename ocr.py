from PIL import Image
from pytesseract import pytesseract
import glob

#path to tesseract executable
path_tess = r'D:\1softwares\ocr\tesseract.exe'
#path to image folder, change with your own path
imgs_path = r"C:\Users\91953\Desktop\testbot\*"

img_list = glob.glob(imgs_path)

text_list = []

for ipath in img_list:
    img = Image.open(ipath)
    pytesseract.tesseract_cmd = path_tess
    text_list += [pytesseract.image_to_string(img)]

def stringcheck(textarr,text):
    match = text.split()
    i = 0
    for a_string in textarr:
        if all(x in a_string for x in match):
            return i
        i = i + 1

#keywords to search the image file
istring = input("\nEnter the string:\n")
i = stringcheck(text_list,istring)

im = Image.open(img_list[i])
im.show()















