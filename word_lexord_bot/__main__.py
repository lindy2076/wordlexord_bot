import logging

from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


from word_lexord_bot.handlers import (
    list_of_commands, inline_echo
)
from word_lexord_bot.config import DefaultSettings
from .bot import bot


logging.basicConfig(
    format='%(levelname)s:%(asctime)s %(message)s',
    datefmt='%m/%d/%Y %I:%M:%S %p',
    filename='wordlexordinfo.log',
    level=logging.INFO
)

settings = DefaultSettings()
dp = Dispatcher(bot)


def register_commands() -> None:
    for handler, handler_commands in list_of_commands:
        dp.register_message_handler(handler, commands=handler_commands)
    dp.register_inline_handler(inline_echo)


async def on_startup_polling(_):
    logging.info("bot started with longpolling!")


async def on_startup_webhook(_):
    logging.info("bot started with webhook!")
    await bot.set_webhook(
        settings.WEBHOOK_URL,
        certificate=open(settings.CERT_PATH, 'rb')
    )


async def on_shutdown():
    logging.warning('shutting down...')
    await bot.delete_webhook()
    logging.warning('bye.')


if __name__ == "__main__":
    register_commands()
    if settings.DEBUG in ["TRUE", "True", "1", True]:
        executor.start_polling(
            dp,
            skip_updates=True,
            on_startup=on_startup_polling
        )
    else:
        executor.start_webhook(
            dispatcher=dp,
            webhook_path=settings.HOST_PATH,
            on_startup=on_startup_webhook,
            on_shutdown=on_shutdown,
            skip_updates=True,
            host=settings.WEBAPP_HOST,
            port=settings.WEBAPP_PORT
        )
