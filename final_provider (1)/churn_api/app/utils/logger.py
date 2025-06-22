import logging
from pathlib import Path
import sys
import pandas as pd
from datetime import datetime
import os

def setup_logger():
    """Configure and return a logger instance"""
    logger = logging.getLogger("churn_api")
    logger.setLevel(logging.INFO)

    # Create handlers
    c_handler = logging.StreamHandler(sys.stdout)
    f_handler = logging.FileHandler("churn_api.log")
    c_handler.setLevel(logging.INFO)
    f_handler.setLevel(logging.INFO)

    # Create formatters and add it to handlers
    log_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    c_handler.setFormatter(log_format)
    f_handler.setFormatter(log_format)

    # Add handlers to the logger
    logger.addHandler(c_handler)
    logger.addHandler(f_handler)

    return logger

def log_prediction(data, prediction):
    """Log prediction data to a CSV file"""
    log_data = data.dict()
    log_data["prediction"] = prediction
    log_data["timestamp"] = datetime.now().isoformat()

    log_df = pd.DataFrame([log_data])
    log_file = "predictions.csv"

    if os.path.exists(log_file):
        log_df.to_csv(log_file, mode='a', header=False, index=False)
    else:
        log_df.to_csv(log_file, index=False)
