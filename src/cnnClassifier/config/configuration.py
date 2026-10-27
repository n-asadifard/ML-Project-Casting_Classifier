from cnnClassifier.constants import *
from cnnClassifier.utils.common import read_yaml, create_directories
from cnnClassifier.entity.config_entity import DataIngestionConfig, KaggleToken


class ConfigurationManager:
    def __init__(
        self,
        secrets_filepath = TOKEN_KEY_PATH,
        config_filepath = CONFIG_FILE_PATH,
        params_filepath = PARAMS_FILE_PATH):

        self.secrets = read_yaml(secrets_filepath)
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)

        create_directories([self.config.artifacts_root])


    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir 
        )

        return data_ingestion_config

    def get_data_ingestion_secrets(self) -> KaggleToken:
        secrets = self.secrets.kaggle_secrets

        get_data_ingestion_secrets = KaggleToken(
            username=secrets.username,
            key=secrets.key
        )

        return get_data_ingestion_secrets