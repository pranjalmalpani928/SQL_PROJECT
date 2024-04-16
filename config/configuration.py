from housing.entity import DataIngetionConfig, DataValidationConfig, DataTransformationConfig,\
ModelTrainingConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig
from housing.exception import CustomException
from housing.utils import read_yaml_file
from housing import constants
import os,sys
from housing.constants.constants import *

class Configuration():

    def __init__(self,config_file_path:str,current_time_stamp:current_timestamp):
        self.config_info=read_yaml_file(config_file_path)
        self.training_pipeline_config=self.get_training_pipeline_config
        self.time_stamp=current_time_stamp

    def get_data_ingetion_config(self)->DataIngetionConfig:
        pass

    def get_data_validation_config(self)->DataValidationConfig:
        pass

    def get_data_transformation_config(self)->DataTransformationConfig:
        pass

    def get_model_trainer_config(self)->ModelTrainingConfig:
        pass

    def get_model_evaluation_config(self)->ModelEvaluationConfig:
        pass

    def get_model_pusher_config(self)->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self):
        pass

    def get_training_pipeline_config(self)->TrainingPipelineConfig:
        try:
            training_pipeline_config=self.config_info[TRAINING_PIPELINE_CONFIG_KEY]
            artifact_dir=os.path.join(ROOT_DIR,
                                      training_pipeline_config[TRAINING_PIPELINE_NAME_KEY],
                                      training_pipeline_config[TRAINING_PIPELINE_ARTIFACT_DIR_KEY])
        except Exception as e:
            raise CustomException(e,sys) from e