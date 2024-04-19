# from housing.entity import DataIngetionConfig, DataValidationConfig, DataTransformationConfig,\
# ModelTrainingConfig, ModelEvaluationConfig, ModelPusherConfig, TrainingPipelineConfig

from housing.entity.config_entity import *
from housing.exception import CustomException
from housing.utils import read_yaml_file
from housing import constants
import os,sys
from housing.constants.constants import *

class Configuration():

    def __init__(self,config_file_path:str,current_time_stamp:current_timestamp):
        try:
            self.config_info=read_yaml_file(config_file_path)
            self.training_pipeline_config=self.get_training_pipeline_config
            self.time_stamp=current_time_stamp
        except Exception as e:
            raise CustomException(e,sys) from e

    def get_data_ingetion_config(self)->DataIngetionConfig:
        
        try:
            data_ingetion_config_dict=self.config_info['data_ingetion_config']
            data_ingetion_dir=os.path.join(self.get_training_pipeline_config().artifacts_dir,'data_ingetion',self.time_stamp)
            raw_data_dir=os.path.join(data_ingetion_dir,data_ingetion_config_dict['raw_data_dir'])
            tgz_data_dir=os.path.join(data_ingetion_dir,data_ingetion_config_dict['tgz_download_url'])
            ingested_data_dir=os.path.join(data_ingetion_dir,data_ingetion_config_dict['ingested_data_dir'])
            ingested_train_dir=os.path.join(ingested_data_dir,data_ingetion_config_dict['ingested_train_dir'])
            ingested_test_dir=os.path.join(ingested_data_dir,data_ingetion_config_dict['ingested_test_dir'])
            
            # print(data_ingetion_config_dict)
            # print(data_ingetion_dir)
            # print(raw_data_dir)
            # print(tgz_data_dir)
            # print(ingested_data_dir)
            # print(ingested_train_dir)
            # print(ingested_test_dir)
            return DataIngetionConfig(dataset_url=data_ingetion_config_dict['dataset_download_url'],
                                    tgz_download_url=tgz_data_dir, raw_data_dir=raw_data_dir,
                                    ingested_train_dir=ingested_train_dir,
                                    ingested_test_dir=ingested_test_dir)
        except Exception as e:
            raise CustomException(e,sys) from e

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
            training_pipeline_config=TrainingPipelineConfig(artifact_dir)
            return training_pipeline_config
        except Exception as e:
            raise CustomException(e,sys) from e