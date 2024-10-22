from textSummarizer.pipeline.stage_01_data_ingestion import DAtaIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DAtaValidationTrainingPipeline
from textSummarizer.logging import logger

STAGE_NAME = 'Data Ingestion Stage'

try :
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<< ")
    data_ingestion = DAtaIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n>>>>>> stage {STAGE_NAME} over <<<<<<\n\nx==================x")

except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = 'Data Validation Stage'

try :
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<< ")
    data_ingestion = DAtaValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f"\n>>>>>> stage {STAGE_NAME} over <<<<<<\n\nx==================x")

except Exception as e:
    logger.exception(e)
    raise e

