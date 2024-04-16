import yaml
from housing.exception import CustomException
from housing.constants.constants import *
import sys

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise CustomException(e,sys) from e
