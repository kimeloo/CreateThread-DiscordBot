import os
import importlib
import logging
logger = logging.getLogger("app_mgr")

class RunBot():
    def __init__(self):
        self.bot = self.create_bot()
    
    def run(self):
        app_mgr = ManageApps(self.bot)
        app_mgr.run()
        self.bot = app_mgr.get_bot()

        # run bot or try 3 times
        for _ in range(3):
            complete = self.run_bot(self.bot)
            if complete:
                break
        else:
            logger.critical("DISCORD BOT FAILED!!!")

    def create_bot(self):
        from .bot.bot import Bot
        bot = Bot().get_bot()
        return bot

    def run_bot(self, bot):
        BOT_TOKEN_NAME = 'DISCORD_BOT_TOKEN'
        from .config import Config
        Config(BOT_TOKEN_NAME)
        bot_token = os.getenv(BOT_TOKEN_NAME)
        if bot_token:
            bot.run(bot_token)
            return True
        else:
            logger.error("Bot Token not found.")
            return False

class ManageApps():
    def __init__(self, bot):
        self.bot = bot
        self.apps = ['Thread',]
    
    def run(self):
        loaded = self.load_apps(self.apps)
        self.append_apps(loaded)

    def load_apps(self, apps):
        loaded = {}
        for app in apps:
            try:
                module = importlib.import_module('.main', package='apps.'+app)
            except ImportError as e:
                logger.warning('Module Not Found : {}'.format(e.args[0]))
            locals()[app] = module
            loaded[app] = module
        return loaded

    def append_apps(self, apps):
        for app in list(apps.keys()):
            self.bot = apps[app].run(self.bot)
    
    def get_bot(self):
        return self.bot

if __name__ == '__main__':
    print("Do not run this file directly.")