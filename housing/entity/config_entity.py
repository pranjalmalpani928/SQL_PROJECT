from collections import namedtuple


# custom datatypes 
DataIngetionConfig=namedtuple('DataIngetionConfig',['dataset_url','tgz_download_url',
                                                    'ingested_train_dir','ingested_test_dir'])

DataValidationConfig=namedtuple('DataValidationConfig',['schema_file_path'])

DataTransformationConfig=namedtuple('DataTransformationConfig',['add_bedroom_per_room','transformed_train_dir'
                                                                'transformed_test_dir','preprocessed_object_file_path'])

ModelTrainingConfig=namedtuple('ModelTrainingConfig',['train_model_file_path','base_accuracy'])

ModelEvaluationConfig=namedtuple('ModelEvaluationConfig',['model_evaluation_file_path','timestamp'])

ModelPusherConfig=namedtuple('ModelPusherConfig',['export_dir_path'])

TrainingPipelineConfig=namedtuple('TrainingPipelineConfig',['artifacts_dir'])