from config.configuration import Configuration
from housing.exception import CustomException

from housing.entity.config_entity import DataIngetionConfig
from housing.entity.artifact_entity import DataIngetionArtifact

from housing.components.data_ingetion import DataIngetion

from datetime import datetime
import os,sys

class Pipeline():

    def __init__(self, config:Configuration=Configuration(os.path.join(os.getcwd(),'config','config.yaml'),datetime.now().strftime("%d_%m_%Y_%H_%M_%S")))->None:
        try:
            self.config = config

            
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def start_data_ingetion(self)->None:
        try:
            data_ingetion_config=self.config.get_data_ingetion_config()
            data_ingetion=DataIngetion(data_ingetion_config=data_ingetion_config)
            return data_ingetion.initiate_data_ingetion()

        except Exception as e:
            raise CustomException(e,sys) from e
        
    
    def start_data_validation(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys) from e
        
    
    def start_data_transformation(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys) from e
        

    def start_model_trainer(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys) from e
        
    
    def start_model_evaluation(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def start_model_pusher(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys) from e
        
    
    def run_pipeline(self):
        try:
            data_ingestion_artifact=self.start_data_ingetion()
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    