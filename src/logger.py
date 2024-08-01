import logging

class MyLogger:
    def __init__(self):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(logging.DEBUG)

        # Create a file handler
        #file_handler = logging.FileHandler('my_app.log')
        #file_handler.setLevel(logging.INFO)

        # Create a console handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.DEBUG)

        # Create a formatter
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        #file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)

        # Add handlers to the logger
        #self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)

    def logDebug(self, message):
        self.logger.debug(message)

    def logInfo(self, message):
        self.logger.info(message)

    def logWarning(self, message):
        self.logger.warn(message)
