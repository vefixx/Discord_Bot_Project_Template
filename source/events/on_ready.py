import nextcord
from nextcord.ext import commands

from source.config.log.log import log


class OnReadyEvent(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

        @bot.event
        async def on_ready():
            log.info(f"Бот запущен: {bot.user}")


def setup(bot: commands.Bot):
    bot.add_cog(OnReadyEvent(bot))
