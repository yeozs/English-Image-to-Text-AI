#Why do this: Can be used to convert pdf, whatsapp/telegram screenshots into text. AI converter.

#Line 10: This part above will have error. Need to install tesseract everytime you open this document. Delete line 10-12. Then reinput line 10-12

from PIL import Image
import os
import pytesseract



path = "/usr/local/share/tessdata/osd.traineddata"
if os.path.exists(path):
  print("Already installed!")
else:
  os.system("install-pkg tesseract-ocr") #install tesseract locally

#This part above will have error. Need to install tesseract

pytesseract.pytesseract.tesseract_cmd = "tesseract" #put tesseract executable in your path

os.environ["TESSDATA_PREFIX"] = "/usr/local/share/tessdata/" #go to environment of tesseract called TESSDATA_PREFIX. Get tessdata as environment

# List of available languages
print(pytesseract.get_languages(config=''))

text = pytesseract.image_to_string(Image.open('test4.png'))

g = open('test.docx','w+') #wipe previous csv file data
g.close()

with open('test.docx', mode = 'w') as f:
    f.write(text)
    
print(text)


#https://tesseract-ocr.github.io/tessdoc/Data-Files.html => other language trained data

# French text image to string
#print(pytesseract.image_to_string(Image.open('test-european.jpg'), lang='fra'))

#in case of corruption: https://replit.com/talk/ask/Pytesseract-Auto-Shell-Install-Package-Issue/140049

#Install Brew
#/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"

