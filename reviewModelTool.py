import joblib
import re
import spacy

class ReviewModelTool:
    def __init__(self, modelPath: str, vectorizerPath: str):
        self.text = ''
        self.model = joblib.load(modelPath)
        self.vectorizer = joblib.load(vectorizerPath)
        self.nlp = spacy.load("en_core_web_sm")
        
    def loadText(self, newText: str):
        self.text = newText
        
    def predictReviewRating(self, text: str):
        self.loadText(text)
        
        text = re.sub(r'<[^>]+>|\\n|\.|,|:|&|;|-|"', '', self.text)
        
        tokens = self.nlp(text)
        processedText = ' '.join([token.text for token in tokens if not token.is_stop])
        
        X = self.vectorizer.transform([processedText])
        
        print(self.model.predict(X))