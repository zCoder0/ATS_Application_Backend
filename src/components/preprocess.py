import spacy
from src.exception.exception_base import ProjectException 
from pdfminer.high_level import extract_text
import sys
import nltk
import string
import re
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
            
            
            self.nlp = spacy.load('en_core_web_sm')
       
            
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
    
    
    def extract_experience(self,jd_text):
        
        experience_format = r'(\d{1,2})\s*(?:\+-)?\s*(?:years|yrs)'
        
        matches = re.findall(experience_format , jd_text.lower())
        print(matches)
        if matches:
            return max([int(number) for number in matches])
        return 0
    
    def extract_skills_from_jd(self, jd_text, skillset=None):
        skill_text = ""
        doc = self.nlp(jd_text)
        
        for chunk in doc.noun_chunks:
            if len(chunk.text.split()) <= 3:
                skill_text += chunk.text.lower() + " "
        
        candidate_skills = {token.text for token in self.nlp(skill_text) if token.is_alpha}
        
        if skillset:
            # Filter with known skillset (if provided)
            matched_skills = [skill for skill in skillset if skill.lower() in candidate_skills]
            return matched_skills
        return list(candidate_skills)
        
        
