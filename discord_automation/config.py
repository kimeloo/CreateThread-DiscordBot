import os
from dotenv import load_dotenv, find_dotenv
import logging
logger = logging.getLogger("config")

class Config():
    def __init__(self):
        self.__TOKEN = self.__load_token()
        logger.info("token loaded.")
    
    @property
    def token(self):
        return self.__TOKEN
    
    @token.setter
    def token(self, token):
        logger.warning("Do not override TOKEN")
    
    def __check_token(self):
        dotenv_file = find_dotenv()
        logger.debug(".env found.")
        return dotenv_file

    def __load_token(self):
        dotenv_file = self.__check_token()
        if dotenv_file:
            load_dotenv(dotenv_file)
            try:
                return os.environ['DISCORD_BOT_TOKEN']
            except KeyError:
                logger.debug(".env - DISCORD_BOT_TOKEN not found.")
        logger.debug("generating .env file.")
        return self.__gen_dotenv()
    
    def __gen_dotenv(self):
        logger.warning("Cannot find your token or .env file !")
        logger.info("Making your .env file...")
        TOKEN = input("Paste your Discord Bot Token >> ")
        with open('./.env', 'a') as envFile:
            envFile.write(f'\n# This file contains your secret!!\n# Be careful when you share this project.\n\nDISCORD_BOT_TOKEN = {TOKEN}')
        logger.info("Token saved in .env file !")
        logger.info("Be careful when you share this project.")
        return TOKEN

if __name__ == '__main__':
    logger.warning("Do not run this file directly.")