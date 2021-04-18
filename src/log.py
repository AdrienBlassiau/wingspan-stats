import logging

from src.path import Path


class Log:

    @staticmethod
    def setup():
        """
        This function setups the logger.
        :return: nothing
        """
        logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
        rootLogger = logging.getLogger()

        fileHandler = logging.FileHandler(Path.get_log_path())
        fileHandler.setFormatter(logFormatter)
        rootLogger.addHandler(fileHandler)

        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(logFormatter)
        rootLogger.addHandler(consoleHandler)

        rootLogger.setLevel(logging.DEBUG)
        logging.getLogger('matplotlib.font_manager').disabled = True
