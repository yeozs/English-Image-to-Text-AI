# English-Image-to-Text-AI
Quick Fix to Converting Images to Text Document

Reason for Creation: Wanted a fast method to convert pdf and whatsapp/telegram screenshots into text. It was possible to google it but what a better way than to code out the quick fix!

Managed to find some help from Replit Community to use pytesseract. https://replit.com/talk/ask/Pytesseract-Auto-Shell-Install-Package-Issue/140049
Problem was the code didn't write the converted text into a docx file. 
My code helps to alleviate that problem. 
Do note to save a copy of test.docx separately before converting another image as code purposefully wipes clean test.docx during each run of main.py!


How to Use:
1. Download all the documents.
2. Open terminal and "cd" to the local folder "English-Image-to-Text-AI-main"
3. Install the necessary python packages. (pip install PIL, pip install pytesseract)
4. Install Brew if using mac. run: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
5. run: brew install tesseract
6. run: sudo mv -v eng.traineddata /usr/local/share/tessdata/

How to convert image to word doc:
1. Place image in local folder "English-Image-to-Text-AI-main". Rename the file as "test4.png"
2. Open terminal and "cd" to the local folder "English-Image-to-Text-AI-main"
3. run: python main.py
4. Open test.docx to find your converted image in word document.


Hope it works for you! Upload your images now and see if the text is shown in test.docx.

