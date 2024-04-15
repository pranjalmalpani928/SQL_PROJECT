from housing.entity import DataIngetionConfig, DataValidationConfig, DataTransformationConfig,\
ModelTrainingConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig

from housing.utils import read_yaml_file
from housing import constants
import os

ROOT_DIR=os.getcwd()
CONFIG_DIR='config.yaml'
CONFIG_FILE_NAME=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)
class Configuration():

    def __init__(self):
        pass

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
        pass