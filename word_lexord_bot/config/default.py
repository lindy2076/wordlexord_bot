from os import environ, path
from dotenv import load_dotenv

from pydantic import BaseSettings


dotenv_path = path.join(path.dirname(__file__), '../..', '.env')
load_dotenv(dotenv_path)


class DefaultSettings(BaseSettings):
    """
    default app config
    """
    BOT_TOKEN: str = environ.get("BOT_TOKEN", "")
    HOST_ADDR: str = environ.get("HOST_ADDR", "localhost")
    HOST_PORT: str = environ.get("HOST_PORT", "8080")
    HOST_PATH: str = environ.get("HOST_PATH", "")
    ADMIN_ID: str = environ.get("ADMIN_ID", "")
    WEBHOOK_URL: str = f"{HOST_ADDR}:{HOST_PORT}{HOST_PATH}"
    DEBUG: str = environ.get("DEBUG", True)
