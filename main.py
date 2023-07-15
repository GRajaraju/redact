import json
import argparse
from redact.ocr import OCR
from redact.model import EntityDetection
from redact.utils import draw_redaction

config_filepath = "./redact/config.json"
with open(config_filepath, "r+") as fr:
    config = json.load(fr)

def main(image_path, target_path):
    # Extract text from the document
    ocr = OCR(image_path)
    text, word2bb = ocr.word_bounding_box_map()

    #Loading NER model
    model_name = config['model_name']
    print(f"Model in use: {model_name}")

    entity_detection = EntityDetection()
    words_list = entity_detection.detect_entities(text)

    # Draw redaction on the image copy and save
    draw_redaction(image_path, target_path, words_list, word2bb)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--filepath", help="path of the file to be redacted.")
    parser.add_argument("--target_path", help="path of the redacted file to be saved.")
    args = parser.parse_args()
    
    image_path = args.filepath
    target_path = args.target_path

    main(image_path, target_path)




