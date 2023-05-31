import logging
from aiogram import Bot

from word_lexord_bot.config import DefaultSettings


def get_app() -> Bot:
    settings = DefaultSettings()
    token = settings.BOT_TOKEN
    if not token:
        logging.info("no token provided")
        exit(1)
    bot = Bot(token=settings.BOT_TOKEN)
    return bot


bot = get_app()
