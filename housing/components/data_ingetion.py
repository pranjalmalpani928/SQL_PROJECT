from housing.entity.config_entity import DataIngetionConfig
from housing.entity.artifact_entity import DataIngetionArtifact
from housing.exception import CustomException
from config.configuration import Configuration
import sys
import tarfile
import requests
import os
from six.moves import urllib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import StratifiedShuffleSplit
import numpy as np



class DataIngetion:
    def __init__(self,data_ingetion_config:DataIngetionConfig):
        try:
            self.data_ingetion_config=data_ingetion_config
        except Exception as e:
            raise CustomException(e,sys) from e
    
    def download_tgz_file(self)->str:
        try:
            '''MY SOLUTION TO DOWNLAOD THE FILE code is working fine
             the problem i faced was that i have not created the raw_data_dir 
             before hand and was trying to insert in the dir'''
            # # url to download tar file
            # dataset_url=self.data_ingetion_config.dataset_url

            # # path of the tar file to be downloaded after the download
            # tgz_file_dir = self.data_ingetion_config.tgz_download_url

            # # make dir for the tar file
            # os.makedirs(tgz_file_dir,exist_ok=True)
            # #print(tgz_file_dir)

            # # open the file and write the file in the directory
            # tar_file_loc=os.path.join(tgz_file_dir,'tgz_file.tgz')
            # with open(tar_file_loc,'wb') as file:
            #     file.write(requests.get(dataset_url).content)

            # # extract the tarfile in csv format in raw data folder
            # raw_data_dir_file=self.data_ingetion_config.raw_data_dir
            # #print(raw_data_dir_file)
            # # make directory for the raw data
            # os.makedirs(raw_data_dir_file,exist_ok=True)
            # with tarfile.open(tar_file_loc,'r')  as tar_file:
            #     tar_file.extractall(raw_data_dir_file)
            # Download and extract the tar file simultaneously
            # return raw_data_dir_file

            # extraction remote url to download dataset
            download_url=self.data_ingetion_config.dataset_url

            # folder location to download tgz file
            tgz_download_dir=self.data_ingetion_config.tgz_download_url

            # check if the path exists
            if os.path.exists(tgz_download_dir):
                pass
            else:
                os.makedirs(tgz_download_dir,exist_ok=True)
            
            # find the file name from the url
            # file_name=download_url.split('/')[-1] -- my solution will not work if we change the os as 
            # naming convention changes with the os system.
            
            file_name=os.path.basename(download_url)

            # complete path of the downloaded file
            tgz_file_path=os.path.join(tgz_download_dir, file_name)

            urllib.request.urlretrieve(download_url, tgz_file_path)

            return tgz_file_path
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def extract_tgz_file(self,tgz_file_path:str):
        try:
            # tar file path which needs to be extracted
            tgz_file_path=tgz_file_path

            # file path of raw_data_dir from data_ingetion_config
            raw_data_dir=self.data_ingetion_config.raw_data_dir
            
            # make the directory to extract the file in raw_data_dir
            if os.path.exists(raw_data_dir):
                pass
            else:
                os.makedirs(raw_data_dir,exist_ok=True)

            with tarfile.open(tgz_file_path) as tgz_file:
                tgz_file.extractall(raw_data_dir)

            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def split_data_as_train_test(self)->DataIngetionArtifact:
        try:
            raw_data_dir=self.data_ingetion_config.raw_data_dir
            file_name=os.listdir(raw_data_dir)[0]

            housing_file_path=os.path.join(raw_data_dir,file_name)

            housing_dataframe=pd.read_csv(housing_file_path)

            # funtion to generate categorisation of median income
            def categorise_median_income(x):
                try:
                    if x>0 and x<=1.5:
                        return 1
                    elif x>1.5 and x<=3:
                        return 2
                    elif x>3 and x<4.5:
                        return 3
                    elif x>4.5 and x<6:
                        return 4
                    else:
                        return 5
                except Exception as e:
                    raise CustomException(e,sys) from e
                
            # new feature categorisation of median income    
            housing_dataframe['cat_median_income']=housing_dataframe['median_income'].map(lambda x: categorise_median_income(x) )

            strat_train_set=None
            strat_test_set=None

            split= StratifiedShuffleSplit(n_splits=1, test_size=0.2,random_state=42)

            for train_index,test_index in split.split(housing_dataframe,housing_dataframe['cat_median_income']):
                strat_train_set=housing_dataframe.loc[train_index].drop(columns=['cat_median_income'],axis=1)
                strat_test_set=housing_dataframe.loc[test_index].drop(columns=['cat_median_income'],axis=1)
            
            # path of the test dataset and tain dataset
            train_path=os.path.join(self.data_ingetion_config.ingested_train_dir,'train.csv')
            test_path=os.path.join(self.data_ingetion_config.ingested_test_dir,'test.csv')

    
            if strat_train_set is not None:
                os.makedirs(self.data_ingetion_config.ingested_train_dir,exist_ok=True)
                strat_train_set.to_csv(train_path,index=False)
            
            if strat_test_set is not None:
                os.makedirs(self.data_ingetion_config.ingested_test_dir,exist_ok=True)
                strat_test_set.to_csv(test_path,index=False)            
            # print('here are the test and train folders')
            return DataIngetionArtifact(train_file_path=train_path,test_file_path=test_path,is_ingested=True,message='Data Ingested')
        except Exception as e:
            raise CustomException(e,sys) from e

    def initiate_data_ingetion(self)->DataIngetionArtifact:
        try:
            tgz_file_path= self.download_tgz_file()
            self.extract_tgz_file(tgz_file_path=tgz_file_path)
            # print('where is the test and train folder')
            return self.split_data_as_train_test()
            
        except Exception as e:
            raise CustomException(e,sys) from e
        
    def __del__(self):
        print('data ingestion completed successfully')