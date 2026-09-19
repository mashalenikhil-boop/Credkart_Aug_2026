import logging

class log_generator_class:

    @staticmethod
    def loggen_method():
        #logger = logging.getLogger("Test_User_Profile.py")
        log_file =  logging.FileHandler(".\\Logs\\Credkart_automation_testing.log")
        log_format = logging.Formatter('%(asctime)s - %(levelname)s -%(funcName)s -%(lineno)d -%(message)s')
        log_file.setFormatter(log_format)
        logger = logging.getLogger()
        logger.addHandler(log_file)
        logger.setLevel(logging.INFO)
        #logger.setLevel(logging.WARNING)
        #logger.setLevel(logging.ERROR)
        #logger.setLevel(logging.CRITICAL)
        return logger


"""
info
warning
error
critical
"""
