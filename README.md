# Document redaction

This project is to develop an open source redaction application that redacts the critical or sensitive information in the documents.

The approach is simple, run OCR against the document and generate a word to bounding box mapping which will be used later
to draw bounding boxes on the documents. 

Pass the text to a language model for NER and make a list of identified entities. Given these entities, retrieve the bounding boxes
of each word in the list and draw the bounding boxes in the document.

<h1>Installation</h1>

To extract text from a document (image), we need an OCR engine. In this project, we are using an open source model tesseract.
Prior to using tesseract, it needs to be installed and update its bin path in the Environment variables.

In addition to tesseract binary, its wrapper pytesseract should be installed.


