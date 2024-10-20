from textSummarizer.pipeline.stage_01_data_ingestion import DAtaIngestionTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = 'Data Ingestion Stage'

try :
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<< ")
    data_ingestion = DAtaIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n>>>>>> stage {STAGE_NAME} started <<<<<<\n\nx==================x")

except Exception as e:
    logger.exception(e)
    raise e