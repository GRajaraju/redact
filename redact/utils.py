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
    img = cv2.imread(image_path)

    for word in words_list:
        i = 0
        j = 1

        if word in word2bb.keys():
            for _ in range(0, len(word2bb[word]), 2):
                (x1, y1) = word2bb[word][i]
                (x2, y2) = word2bb[word][j]
                cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), -1)
                i+=2
                j+=2

    cv2.imwrite(f"Redacted image saved at: {target_path}\Redacted_{file_name}")
    
