from PIL import Image
import pytesseract
from io import StringIO
import pandas as pd

image_path = "C:\\Users\\RAJARAJU\\Downloads\\housing.png"
text_info = pytesseract.image_to_data(Image.open(image_path))

text_bounding_boxes = {}
for single_line in text_info.split('\n'):
    print(f"line split: {single_line}")
    ents = single_line.split('\t')
    print(f"ENTS: {ents}")
    text_bounding_boxes.update({ents[-1] :
                                {
                                    'x' : ents[6],
                                    'y' : ents[7],
                                    'width' : ents[8],
                                    'height' : ents[9]
                                }})
    
print(text_bounding_boxes)


