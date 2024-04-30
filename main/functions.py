import easyocr

def ocr_function(image):
    # image is a NumPy array
    reader = easyocr.Reader(['en'], gpu=False) # this needs to run only once to load the model into memory
    result = reader.readtext(image, detail = 0)
    result = " ".join(result)
    return result