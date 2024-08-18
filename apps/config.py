import os
from dotenv import load_dotenv, find_dotenv
import logging
logger = logging.getLogger("config")

class Config():
    def __init__(self, name):
        self.token_name = name
        self.__load_env()
        logger.info(".env loaded.")
    
    def __check_env(self):
        dotenv_file = find_dotenv()
        logger.debug(".env found.")
        return dotenv_file

    def __load_env(self):
        dotenv_file = self.__check_env()
        if dotenv_file:
            load_dotenv(dotenv_file)
            try:
                os.environ[self.token_name]
                return
            except KeyError:
                logger.debug(".env - {} not found.".format(self.token_name))
        logger.debug("generating .env file.")
        self.__gen_dotenv()
    
    def __gen_dotenv(self):
        logger.warning("Cannot find your token or .env file !")
        logger.info("Making your .env file...")
        TOKEN = input("Paste your {} (If you don't have any, just press enter) >> ".format(self.token_name))
        if not TOKEN:
            pass
        with open('./.env', 'a') as envFile:
            envFile.write(f'\n{self.token_name} = {TOKEN}')
        logger.info("Token saved in .env file !")
        logger.info("Be careful when you share this project.")

if __name__ == '__main__':
    logger.warning("Do not run this file directly.")