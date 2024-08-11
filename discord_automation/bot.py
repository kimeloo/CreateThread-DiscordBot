import discord
from discord.ext import commands as discord_commands
import os
from .commands import Commands as mycommands
from .events import Events as myevents
import logging
logger = logging.getLogger("bot")

class ThreadBot():
    def __init__(self):
        self.__TOKEN = os.getenv('DISCORD_BOT_TOKEN')
        # self.__CHANNEL_ID_discussion = os.getenv('CHANNEL_DISCUSSION')
        self.__create_bot()
    
    def __create_bot(self):
        intents = discord.Intents.default()
        intents.message_content = True
        intents.guilds = True
        intents.reactions = True
        
        bot = discord_commands.Bot(command_prefix='!', intents=intents)
        bot = myevents(bot).add()
        bot = mycommands(bot).add()
        self.bot = bot
    
    # def __add_events(self, bot):
    #     @bot.event
    #     async def on_ready():
    #         logger.info(f'Logged in as {bot.user.name}')
        
    #     @bot.event
    #     async def on_raw_reaction_add(reaction):
    #         logger.debug("EVENT")
    #         logger.debug(reaction.message)
    #         logger.debug(reaction.message.content)
    #         logger.debug(reaction.message.channel.parent)
    #         if (reaction.message.channel.name == 'idea') or (reaction.message.channel.parent.name == 'idea'):
    #             discussion_channel = bot.get_channel(int(self.__CHANNEL_ID_discussion))
    #             logger.debug(f'Get Channel by ID {self.__CHANNEL_ID_discussion}')
    #             new_message = await discussion_channel.send(reaction.message.content)
    #             await new_message.create_thread(name=reaction.message.content)

    #     @bot.event
    #     async def on_raw_reaction_add(payload):
    #         channel = await self.bot.fetch_channel(payload.channel_id)
    #         message = await channel.fetch_message(payload.message_id)
    #         emoji = payload.emoji
    #         logger.info(emoji.name)
    #         if (channel.name == 'idea') or (channel.parent.name == 'idea'):
    #             if emoji.name == "✅":
    #                 discussion_channel = bot.get_channel(int(self.__CHANNEL_ID_discussion))
    #                 new_message = await discussion_channel.send(message.content)
    #                 thread = await new_message.create_thread(name=message.content, auto_archive_duration=10080)

    #                 seoul_tz = ZoneInfo('Asia/Seoul')
    #                 creation_time = datetime.now(seoul_tz)
    #                 archive_time = creation_time + timedelta(days=7)
    #                 creation_time = creation_time.strftime("%Y-%m-%d %H:%M:%S")
    #                 archive_time = archive_time.strftime("%Y-%m-%d %H:%M:%S")
    #                 await thread.send(f"@everyone\n Created : {creation_time} (UTC+9)\nArchived : {archive_time} (UTC+9).")
    #     return bot

    # def __add_commands(self, bot):
    #     @bot.command()
    #     async def ping(ctx):
    #         send_message = 'pong'
    #         logger.info("[{:>8}] : {}".format("Recieved", ctx.message.content))
    #         await ctx.channel.send(send_message)
    #         logger.info("[{:>8}] : {}".format("Sent", send_message))
    #     return bot
    
    def run(self):
        if self.__TOKEN:
            self.bot.run(self.__TOKEN)
        else:
            logger.error("Token not found.")

if __name__ == '__main__':
    logger.warning("Do not run this file directly.")