import os
from dotenv import load_dotenv, find_dotenv
import logging
logger = logging.getLogger("config")

class Config():
    def __init__(self):
        self.__TOKEN = self.__load_token()
    
    @property
    def token(self):
        return self.__TOKEN
    
    @token.setter
    def token(self, token):
        logger.warning("Do not override TOKEN")
    
    def __check_token(self):
        dotenv_file = find_dotenv()
        return dotenv_file

    def __load_token(self):
        dotenv_file = self.__check_token()
        if dotenv_file:
            load_dotenv(dotenv_file)
            try:
                return os.environ['discordBotToken']
            except KeyError:
                pass
        return self.__gen_dotenv()
    
    def __gen_dotenv(self):
        print("Cannot find your token or .env file !")
        print("Making your .env file...")
        TOKEN = input("Paste your Discord Bot TOKEN >> ")
        with open('./.env', 'a') as envFile:
            envFile.write(f'\n# This file contains your secret!!\n# Be careful when you share this project.\n\ndiscordBotToken = {TOKEN}')
        print("Token saved in .env file !")
        print("Be careful when you share this project.")
        return TOKEN

if __name__ == '__main__':
    print("Do not run this file directly!")
    print("Please go to Project Directory and run main.py")