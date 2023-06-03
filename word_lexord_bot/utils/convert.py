import word_lexord as wl
from .responses import Response


ALPHABETS = set(["enu", "enl", "руу", "рул"])

def only_numbers_in(s: str) -> bool:
    """
    Returns True if s is made of digits and spaces only.
    """
    s = s.replace(" ", "")
    return s.isnumeric()


async def try_convert(msg: str) -> str:
    """
    Handles a message. If it is like "[alphabet] [text]" then it is converted.
    """
    msg_split = msg.split()
    first_word = msg_split[0].lower()
    if len(first_word) != 3:
        return Response.UNKNOWN_COMMAND

    if first_word not in ALPHABETS:
        return Response.NO_ALPHABET

    if len(msg_split) < 2:
        return Response.NO_TEXT_GIVEN

    if len(msg_split) > 100:
        return Response.TOO_MANY_WORDS

    for word in msg_split:
        if len(word) > 2000:
            if word.isnumeric() and len(word) < 3001:
                continue
            return Response.WORD_TOO_LONG

    match first_word:
        case "enu":
            lang = wl.lang.ALPHABETS["EN"]["upper"]
        case "enl":
            lang = wl.lang.ALPHABETS["EN"]["lower"]
        case "руу":
            lang = wl.lang.ALPHABETS["RU"]["upper"]
        case "рул":
            lang = wl.lang.ALPHABETS["RU"]["lower"]
        case _:
            return Response.IMPOSSIBLE
    
    the_text = msg[4:]
    msg_converted = ""

    if not only_numbers_in(the_text):
        nums = wl.get_words_numbers_in_sentence(the_text, lang)
        if not nums:
            return Response.LETTERS_MISSING
        msg_converted = " ".join(map(str, nums))
    else:
        words = wl.nums_to_words(map(int, msg_split[1:]), lang)
        msg_converted = " ".join(words)

    return Response.append_msg(Response.wrap_md_mono(msg_converted))
