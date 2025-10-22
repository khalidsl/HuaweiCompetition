import logging
from logging.handlers import RotatingFileHandler
import os

# Configure the logger
def setup_logger():
    log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
    log_format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    
    logging.basicConfig(level=log_level, format=log_format)
    
    # Create a rotating file handler
    handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=10)
    handler.setFormatter(logging.Formatter(log_format))
    
    # Add the handler to the root logger
    logging.getLogger().addHandler(handler)

# Call the setup_logger function to initialize logging
setup_logger()