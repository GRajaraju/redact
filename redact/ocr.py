from PIL import Image
import pytesseract
from io import StringIO
import pandas as pd

"""
Generate a dictionary that contains text and its corresponding bounding boxes.
This dictionary will be used to map the words with its bounding boxes.
"""
class OCR:
    def __init__(self, image_path):
        super().__init__()

        self.image_path = image_path

    def extract_text(self):
        text_info = pytesseract.image_to_data(Image.open(self.image_path))
        text = pytesseract.image_to_string(Image.open(self.image_path))
        # print(f"Extracted text: {text}")
        return text, text_info

    """
    TODO:
    1. Handle duplicate entries
    
    """
    def word_bounding_box_map(self):
        text, text_info = self.extract_text()
        text_bounding_boxes = {}
        for single_line in text_info.split('\n'):
            ents = single_line.split('\t')
            if len(ents)>1:
                text_bounding_boxes.update({ents[-1] :
                                            {
                                                'x' : ents[6],
                                                'y' : ents[7],
                                                'width' : ents[8],
                                                'height' : ents[9]
                                            }})
        return text, text_bounding_boxes


if __name__ == "__main__":
    image_path = "sample_letter.png"

    ocr = OCR(image_path)
    text, word2bb = ocr.word_bounding_box_map()
    print(word2bb)


