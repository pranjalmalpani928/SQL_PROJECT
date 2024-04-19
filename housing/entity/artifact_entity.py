from collections import namedtuple

DataIngetionArtifact=namedtuple('DataIngetionArtifact',
                                ['train_file_path','test_file_path','is_ingested','message'])