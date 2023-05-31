from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
)


def create_reply_kb() -> ReplyKeyboardMarkup:
    btn_cmds = KeyboardButton("команды")
    btn_info = KeyboardButton("инфо")

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(btn_cmds)
    kb.row(btn_info)
    return kb


startup_kb = create_reply_kb()
nothing = ReplyKeyboardRemove()
