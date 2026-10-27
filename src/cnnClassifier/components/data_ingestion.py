import os
import zipfile
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig, KaggleToken
from pathlib import Path
import kaggle

class DataIngestion:
    def __init__(self, config: DataIngestionConfig, token: KaggleToken):
        self.config = config
        self.secrets = token
    
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            os.environ['KAGGLE_USERNAME'] = self.secrets.username
            os.environ['KAGGLE_KEY'] = self.secrets.key
            url = self.config.source_URL            
            kaggle.api.authenticate()
            kaggle.api.dataset_download_files(url,
                                             path=self.config.unzip_dir,
                                             unzip=False)
            
            logger.info(f" Casting dataset is downloaded!")
        else:
            logger.info(f"File already exist and has a size of: {get_size(Path(self.config.local_data_file))}")


    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Downloaded zipfile has been extracted")