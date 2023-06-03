import logging
from aiogram import types

import word_lexord_bot.keyboards as kb
import word_lexord_bot.utils as wl_utils
from .texts import MESSAGES


async def send_hello(message: types.Message):
    logging.info(f"/start from {message.from_user.id}, {message.from_user.first_name}")
    await message.reply(MESSAGES["START_MESSAGE"], reply_markup=kb.startup_kb, parse_mode="Markdown")


async def send_info(message: types.Message):
    await message.reply(MESSAGES["INFO"], parse_mode="Markdown", reply_markup=kb.startup_kb)


async def send_commands(message: types.Message):
    await message.reply(MESSAGES["COMMANDS"], parse_mode="Markdown", reply_markup=kb.startup_kb)


async def send_echo(message: types.Message):
    match message.text.lower():
        case "инфо":
            await message.reply(MESSAGES["INFO"], parse_mode="Markdown")

        case "info":
            await message.reply(MESSAGES["INFO"], parse_mode="Markdown")

        case "команды":
            await message.reply(MESSAGES["COMMANDS"], parse_mode="Markdown")

        case _:
            converted = await wl_utils.try_convert(message.text)
            await message.reply(converted, parse_mode="Markdown")
