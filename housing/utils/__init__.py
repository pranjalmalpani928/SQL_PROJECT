import yaml
import sys
from housing.exception import CustomException

def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path,'r') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise CustomException(e,sys) from e