from setuptools import find_packages, setup 
from typing import List

setup(
    name = 'mlproject',
    version='0.0.1',
    author='Maroof',
    author_email='warsimaroof1@gmail.com',
    packages=find_packages(),
    install_requires = ['pandas', 'numpy', 'seaborn']
)

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:                                 #function will return a list
    '''
    This function will return the list of requirements.
    '''

    requirements= []                                                            #empty list
    with open(file_path) as file_obj:                                           #create temp file obj
        requirements = file_obj.readlines()                                     #once we read first line, when we go to next line, there \n also gets read due to readlines().                                                                         
        requirements = [req.replace("\n","") for req in requirements]           #use list comprehension.

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements        