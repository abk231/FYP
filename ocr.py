try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import re

def ocr_core(filename):
    """
    This function will handle the core OCR processing of images.
    """
    text = pytesseract.image_to_string(Image.open(filename))  
    return text

resulttext = ocr_core('test3.png')
count = 0
if("FIGURE" in resulttext):
    splitted_text = resulttext.split(" ")
    a = re.findall(r'[\w\.-]+ \d+\.\d+', resulttext)
    a = [x.upper() for x in a]
    unique_figno = list(set(a))
    print(unique_figno)
    # for text in splitted_text:
    #     x = re.findall("Figure", text)
        # try:
        #     figno = float(text)
        #     print(figno)
        # except:
        #     pass
else:
    print("No Figure Number in Image")