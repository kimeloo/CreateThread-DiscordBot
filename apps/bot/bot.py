import discord
from discord.ext import commands as discord_commands
import logging
logger = logging.getLogger(__name__)

class Bot():
    def __init__(self):
        self.__create_bot()
    
    def __create_bot(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.reactions = True
        
        bot = discord_commands.Bot(command_prefix='!', intents=intents)
        self.bot = bot
    
    def get_bot(self):
        return self.bot

if __name__ == '__main__':
    logger.warning("Do not run this file directly.")