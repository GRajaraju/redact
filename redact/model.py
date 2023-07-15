from transformers import AutoTokenizer, AutoModelForTokenClassification
from transformers import pipeline


class EntityDetection:
  def __init__(self, model_name="dslim/bert-base-ner"):
    super().__init__()

    print(f"Loading model: {model_name}")
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

  def merge_subwords(self, results):
     words_list = []
     for idx, row in enumerate(results):
        word = row['word']
        if not idx == 0:
           if '##' in word:
              if len(words_list) < idx:
                 merged_word = words_list[len(words_list) - 1] + word.replace('##', '')
                 words_list[len(words_list) - 1] = merged_word
              else:
                 merged_word = words_list[idx - 1] + word.replace('##', '')
                 words_list[idx - 1] = merged_word
           else:
              words_list.append(word)
        else:
           words_list.append(word)

     return words_list
            

  def detect_entities(self, text):
    results = self.entity_detection(text)
    words_list = self.merge_subwords(results)
    return words_list
    
if __name__ == "__main__":
    model_name = "dslim/bert-base-ner"
    entity_detection = EntityDetection()

    text = "Delhi is the capital of India"

    results = entity_detection.detect_entities(text)
    print(results)

    
        
