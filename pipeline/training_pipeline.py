from src.data_ingestion import DataIngestion
from src.data_preprocessing import DataProcessor
from src.model_training import ModelTraining
from utils.common_fuctions import read_yaml
from config.path_config import *



if __name__ == "__main__":
    ###  1. Data Ingestion
    data_ingestion = DataIngestion(read_yaml(CONFIG_PATH))
    data_ingestion.run()

    ###  2. Data Processing
    processor = DataProcessor(TRAIN_FILE_PATH,TEST_FILE_PATH,PROCESSED_DIR,CONFIG_PATH)
    processor.process()    

    ###  3. Model Training
    trainer = ModelTraining(PROCESSED_TRIAN_DATA_PATH,PROCESSED_TEST_DATA_PATH,MODEL_OUTPUT_PATH)
    trainer.run() 


# set GOOGLE_APPLICATION_CREDENTIALS=C:\Users\hp\Downloads\mkaad-464810-c7e3d76b14c6.json
