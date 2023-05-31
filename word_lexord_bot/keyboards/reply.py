from aiogram.types import (
    ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
)


def create_reply_kb() -> ReplyKeyboardMarkup:
    btn_cmds = KeyboardButton("команды")
    btn_info = KeyboardButton("инфо")
    btn_gh1 = KeyboardButton("gh пакет")
    btn_gh2 = KeyboardButton("gh бот")

    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    kb.row(btn_cmds)
    kb.row(btn_info)
    kb.row(btn_gh1, btn_gh2)
    return kb


startup_kb = create_reply_kb()
nothing = ReplyKeyboardRemove()
