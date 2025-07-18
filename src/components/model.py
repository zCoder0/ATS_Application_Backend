import spacy
from src.exception.exception_base import ProjectException 
from src.components.preprocess  import ExtractData
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


class ATS_Score:
    
    def __init__(self,skillset):
        self.nlp = spacy.load('en_core_web_sm')
        self.skillset = [skill.lower() for skill in skillset ]
        
    def match_skills(self,text):
        
       tokens = [token.text.lower() for token in self.nlp(text) if token.is_alpha]
       matched_skills = [skill for skill in self.skillset if skill in tokens]
       return matched_skills
   
    def calculate_similarity(self, resume_text , jd_text):
        vectorizer = TfidfVectorizer()
        resume_vector = vectorizer.fit_transform([resume_text ,jd_text])
        similarity = cosine_similarity(resume_vector[0:1], resume_vector[1:2])[0][0]
        return similarity*100
        
   
    def calculate_ats_score(self,resume_text ,jd_text):
        
        matched_skills = self.match_skills(resume_text)
        
        skill_socre =( len(matched_skills) / len(self.skillset))* 100 
        similarity_score  = self.calculate_similarity(resume_text ,jd_text)
        final_score = round(0.55* skill_socre + 0.45*similarity_score,2)        
    
        return {
            "final_score":final_score,
            "skill_score":round(skill_socre,2),
            "similarity_score":round(similarity_score,2),
            "matched_skills":matched_skills,
            "missing_skills":list(set(self.skillset) - set(matched_skills))
        }
