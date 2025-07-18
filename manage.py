from src.exception.exception_base import ProjectException
from src.components.preprocess import ExtractData
from src.components.model import ATS_Score
import sys


class TestScore:
    
    def __init__(self):
        pass
    
    def FindScore(self , resume_path,jd):

        try:
            
            extract_resume = ExtractData(resume_path)
            preprocess_data = extract_resume.preprocess_text()
            preprocess_data = " ".join(preprocess_data)
            
            experience_resume = extract_resume.extract_experience(preprocess_data)
            
            jd_data =extract_resume.preprocess_text(jd)
            job_description = " ".join(jd_data)
            
            skill_set =  extract_resume.extract_skills_from_jd(job_description )
            experience = extract_resume.extract_experience(job_description)
            
            
            
            ats_score =  ATS_Score(skill_set)
            final_score =  ats_score.calculate_ats_score(preprocess_data , job_description)
            
            return final_score


        except ZeroDivisionError as e:
            ProjectException(e,sys)