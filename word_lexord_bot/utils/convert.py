from typing import List
import word_lexord as wl
from .responses import Response


def word_too_long(word: str) -> bool:
    """
    Returns True if word is too long.
    """
    if len(word) <= 2000:
        return False
    if len(word) <= 3000 and word.isnumeric():
        return False
    return True


def only_numbers_in(s: str) -> bool:
    """
    Returns True if s is made of digits and spaces only.
    """
    s = s.replace(" ", "")
    return s.isnumeric()


def detect_alphabet(code_word: str) -> str | None:
    """
    Returns word_lexord alphabet if code_word is an alphabet code, or
      None otherwise.
    """
    lang = None
    match code_word:
        case "enu":
            lang = wl.lang.ALPHABETS["EN"]["upper"]
        case "enl":
            lang = wl.lang.ALPHABETS["EN"]["lower"]
        case "руу":
            lang = wl.lang.ALPHABETS["RU"]["upper"]
        case "рул":
            lang = wl.lang.ALPHABETS["RU"]["lower"]
    return lang


def convert(msg: str, words: List[str], lang: str) -> str:
    """
    Converts text from msg. Words should be msg.split()[1:].
    """
    converted = ""
    text = msg[4:]

    if only_numbers_in(text):
        numbers = [int(word) for word in words]
        words = wl.nums_to_words(numbers, lang)
        converted = " ".join(words)
    else:
        nums = wl.get_words_numbers_in_sentence(text, lang)
        converted = " ".join(map(str, nums))
    return converted


def try_convert(msg: str) -> str:
    """
    Handles a message. If it is like "[alphabet] [text]" then it is converted.
    """
    msg_split = msg.split()
    first_word = msg_split[0].lower()
    if len(first_word) != 3:
        return Response.UNKNOWN_COMMAND

    lang = detect_alphabet(first_word)
    if not lang:
        return Response.NO_ALPHABET

    if len(msg_split) < 2:
        return Response.NO_TEXT_GIVEN

    if len(msg_split) > 100:
        return Response.TOO_MANY_WORDS

    for word in msg_split:
        if word_too_long(word):
            return Response.WORD_TOO_LONG

    msg_converted = convert(msg, msg_split[1:], lang)
    if not msg_converted:
        return Response.LETTERS_MISSING

    return Response.wrap_converted(msg_converted)
