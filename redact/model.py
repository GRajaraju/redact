from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


class EntityDetection:
  def __init__(self, model_name="dslim/bert-base-ner"):
    super().__init__()

    self.tokenizer = AutoTokenizer.from_pretrained(
      model_name
      )
    self.model = AutoModelForTokenClassification.from_pretrained(
      model_name
      )

    self.entity_detection = pipeline("ner", 
                                     model=self.model,
                                     tokenizer=self.tokenizer
                                     )
    
  def detect_entities(self, text):
    results = self.entity_detection(text)
    return results
    
if __name__ == "__main__":
    model_name = "dslim/bert-base-ner"
    entity_detection = EntityDetection()

    text = "Delhi is the capital of India"

    results = entity_detection.detect_entities(text)
    print(results)

    
        
