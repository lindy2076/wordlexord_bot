import hashlib
import logging
from aiogram.types import (
    InlineQuery, InlineQueryResultArticle, InputTextMessageContent
)
from word_lexord_bot.utils import convert_inline_mode


ALPHABETS = ["enu", "enl", "руу", "рул"]


async def inline_echo(inline_query: InlineQuery):
    text = inline_query.query
    if not text:
        await inline_query.answer(results=[])
        return None
    logging.info(text)

    options = []
    for alphabet in ALPHABETS:
        request = f"{alphabet} {text}"

        for i in range(2):
            msg = convert_inline_mode(request, silent=i)
            response = InputTextMessageContent(msg, parse_mode="Markdown")

            code = f"{request}{i}"
            result_id = hashlib.md5(code.encode()).hexdigest()
            title = f'{alphabet} {text}'
            if i:
                title += " (silent mode)"

            item = InlineQueryResultArticle(
                id=result_id,
                title=title,
                input_message_content=response,
                description=msg[:25] + "...",
            )
            options.append(item)
    await inline_query.answer(results=options, cache_time=200)
