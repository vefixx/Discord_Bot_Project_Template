import nextcord
from nextcord.ext import commands

from source.config.cfg.cfg import Config
from source.config.log.log import log
from source.utils.dotenv_utils import get_dotenv_data

bot = commands.Bot(intents=Config.bot_intents)

if __name__ == '__main__':
    for ext in Config.bot_extensions:
        log.info(f"Загрузка расширения {ext}")
        bot.load_extension(ext)

    env_data = get_dotenv_data()

    log.info("Запуск бота")

    bot.run(env_data.bot_token)