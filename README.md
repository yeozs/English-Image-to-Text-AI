# English-Image-to-Text-AI
Quick Fix to Converting Images to Text Document

Reason for Creation: Wanted a fast method to convert pdf and whatsapp/telegram screenshots into text. It was possible to google it but what a better way than to code out the quick fix!

Managed to find some help from Replit Community to use pytesseract. https://replit.com/talk/ask/Pytesseract-Auto-Shell-Install-Package-Issue/140049
Problem was the code didn't write the converted text into a docx file. 
My code helps to alleviate that problem.


How to Use:
1. Download all the documents.
2. Install the necessary python packages. (pip install PIL, pip install pytesseract)
3. Install Brew. /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
4. brew install tesseract
5. sudo mv -v eng.traineddata /usr/local/share/tessdata/


Hope it works for you! Upload your images now and see if the text is shown in test.docx.

