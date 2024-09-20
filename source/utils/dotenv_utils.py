from dotenv import dotenv_values

from source.config.cfg.cfg import Config
from source.models.models import DotenvDefaultData


def get_dotenv_data() -> DotenvDefaultData:
    """Возвращает модель **DotenvDefaultData** из файла .env (`Config.dotenv_path`)"""

    env_values = dotenv_values(Config.dotenv_path)

    values = [value for key, value in env_values.items()]

    return DotenvDefaultData(*values)

