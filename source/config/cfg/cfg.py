import nextcord


class Config:
    dotenv_path = '.env'
    """Путь до .env файла относителя корня проекта."""

    bot_extensions = [

    ]
    """Расширения бота (коги), которые будут загружены при запуске."""

    bot_intents = nextcord.Intents.default()
    """Интенты для бота. По умолчанию установлено `nextcord.Intents.default()`"""
