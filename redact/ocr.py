from PIL import Image
import pytesseract
from io import StringIO
import pandas as pd

image_path = "C:\\Users\\RAJARAJU\\Downloads\\housing.png"
text_info = pytesseract.image_to_data(Image.open(image_path))

print(type(text_info))
all_data = StringIO(text_info)

df = pd.read_csv(all_data)
print(df)

df.to_csv("ocr_data.csv")
