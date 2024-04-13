from setuptools import setup, find_packages
from typing import List


# Declare variables for the setup tools
PROJECT_NAME='HOUSING-PREDICTION'
VERSION='0.0.1'
AUTHOR='PRANJAL MALPANI'
DESCRIPTION='HOUSING PRICE PREDICTION'


# variable help to build the packages HYPEN_MINUS_E declared in requirements.txt file need to be removed 
# from get_requirements_list function
DOT_HYPHEN_E='-e .' 


def get_requirements_list(file:str)->List[str]:
    """
    Description: This function is going to return lis of requirement 
    mention in requirements.txt

    return this function is going to return a lis which contain name of libraries 
    mentioned in requirements.txt file
    """
    try:
        with open(file,'r') as file:
            
            contents=file.readlines()
            requirements=[content.replace('\n',"") for content in contents]
            if DOT_HYPHEN_E in requirements:
                requirements.remove(DOT_HYPHEN_E)
        return requirements
    except Exception as e:
        return e
            



setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(), #find all the packages that are there in the project
    install_requires=get_requirements_list('requirements.txt')

)