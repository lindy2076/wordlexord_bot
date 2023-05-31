import word_lexord as wl

alphabets = set(["enu ", "enl ", "руу ", "рул "])

async def try_convert(msg: str) -> int | str:
    if len(msg) < 4 or msg[:4] not in alphabets:
        return -1
    
    msg_split = msg.split()
    if len(msg_split) < 2:
        return "что-то то должно быть!!!"

    lang = "abcde"
    match msg[:3]:
        case "enu":
            lang = wl.lang.ALPHABETS["EN"]["upper"]
        case "enl":
            lang = wl.lang.ALPHABETS["EN"]["lower"]
        case "руу":
            lang = wl.lang.ALPHABETS["RU"]["upper"]
        case "рул":
            lang = wl.lang.ALPHABETS["RU"]["lower"]


    try:
        words = wl.nums_to_words(map(int, msg_split[1:]), lang)
    except:
        words = None
    
    try:
        nums = wl.get_words_numbers_in_sentence(msg[4:], lang)
    except:
        nums = None
    
    if words is None and nums == []:
        return "some crazy shit happened..."
    elif words is None:
        return "msg: `" + " ".join(map(str, nums)) + "`"
    
    return "msg: `" + " ".join(words) + "`"
