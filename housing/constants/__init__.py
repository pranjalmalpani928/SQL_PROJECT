import os
from datetime import datetime


def current_timestamp():
    return f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'


ROOT_DIR=os.getcwd() # current working directory
CONFIG_DIR='config'
CONFIG_FILE_NAME='config.yaml'
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)



# Training Pipeline Constants Declarations

TRAINING_PIPELINE_CONFIG_KEY='training_pipeline_config'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY='artifact_dir'
TRAINING_PIPELINE_NAME_KEY='pipeline_name'


# Constants for Data Ingetion configuration

DATA_INGETION_CONFIG_KEY='data_ingetion_config'
DATA_INGETION_ARTIFACT_DIR='data_ingetion'
DATA_INGETION_DOWNLOAD_URL_KEY='dataset_download_url'
DATA_INGETION_RAW_DATA_DIR_KEY='raw_data_dir'
DATA_INGETION_TGZ_DOWNLOAD_URL_KEY='tgz_download_url'
DATA_INGETION_DATA_DIR_NAME_KEY='ingested_data_dir'
DATA_INGETION_TRAIN_DIR_NAME_KEY='ingetsted_train_dir'
DATA_INGETION_TEST_DIR_NAME_KEY='ingested_test_dir'


# Constants for Data Validation Configurations

DATA_VALIDATION_CONFIG_KEY= 'data_validation_config'
DATA_VALIDATION_SCHEMA_FILE_NAME_KEY= 'schema_file_name'