import os
from datetime import datetime


def current_timestamp():
    return f'{datetime.now().strftime("%d/%m/%Y %H:%M:%S")}'


ROOT_DIR=os.getcwd() # current working directory
CONFIG_DIR='config'
CONFIG_FILE_NAME='config.yaml'
CONFIG_FILE_PATH=os.path.join(ROOT_DIR,CONFIG_DIR,CONFIG_FILE_NAME)



# Training Pipelien Constants Declarations

TRAINING_PIPELINE_CONFIG_KEY='training_pipeline_config'
TRAINING_PIPELINE_ARTIFACT_DIR_KEY='artifact_dir'
TRAINING_PIPELINE_NAME_KEY='pipeline_name'


