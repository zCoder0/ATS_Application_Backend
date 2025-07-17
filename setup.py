import os

from setuptools import setup ,find_packages

from typing import List 


def get_requirements() -> List[str]:
    
    requirements_list :List[str] =[]
    
    with("requirements.txt",'r') as f:
        
        lines = f.readlines()
        
    
        for line in lines:
            
            line = line.strip()
            
            if line and line !="-e.":
                requirements_list.append(line)
                
        
    return requirements_list


setup(
    
    name="ATS Application",
    version="1.0",
    author="PremRaj",
    author_email="rajp37590@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements()
    
)
        