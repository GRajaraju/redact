import cv2

def draw_redaction(image_path, target_path, words_list, word2bb):
    """Draws filled rectangular boxes around key entities for redaction.
    
    Args:
        image_path: path of the image which needs to be redacted.
        target_path: path of the redacted image to be saved.
        words_list: list of all entities found in the document.
        word2bb: list that contains mapping between words and
                their corresponding bounding boxes.

    """
    file_name = image_path.split('\\')[-1]
    print(f"File in process: {file_name}")
    img = cv2.imread(image_path)
    for word in words_list:
        if word in word2bb.keys():
            x1 = int(word2bb[word]['x'])
            y1 = int(word2bb[word]['y'])
            x2 = int(word2bb[word]['width'])
            y2 = int(word2bb[word]['height'])
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 1)
    print(f"Saving redacted image at {target_path}\\Redacted_{file_name}")
    cv2.imwrite(f"{target_path}\Redacted_{file_name}", img)
    