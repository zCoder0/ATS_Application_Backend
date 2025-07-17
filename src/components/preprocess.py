import spacy
from src.exception.exception_base import ProjectException 
from pdfminer.high_level import extract_text
import sys
import nltk
import string

from nltk.corpus import stopwords

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

punc = set(string.punctuation)

punc.add("•")
punc.add("–")

class ExtractData:
    
    def __init__(self ,path ,txt = False):
        try:
            if not txt:
                self.text = extract_text(path).lower()
            
            else:
                with open(path , 'r') as f:
                    self.text = f.read().lower()
            
            
        except Exception as e:
            ProjectException(e, sys)
    
    def preprocess_text(self,text=None):
        
        if text ==None:
            text = self.text
        
        splited_text = text.split("\n")
        
        pre_sentence =[]
        
        for sentence in splited_text:
            if sentence.strip():  # removes empty lines
                sentence = sentence.replace(",", " ")
                sentence = "".join(char for char in sentence if char not in punc)
                clean_sentence = " ".join(
                    word for word in sentence.split() if word not in stop_words
                )
                pre_sentence.append(clean_sentence)
        return pre_sentence
    
