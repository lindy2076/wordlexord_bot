class Response:
    UNKNOWN_COMMAND = "пока такой команды нет. напиши *инфо*"
    NO_ALPHABET = "такого алфавита пока нет... напиши *инфо*, " + \
                  "там есть необходимая информация"
    NO_TEXT_GIVEN = "после алфавита нужно ввести сообщение для перевода"
    IMPOSSIBLE = "этого сообщения не должно быть"
    UNKNOWN_ERROR = "произошла какая-то ошибка"
    LETTERS_MISSING = "в запросе должна быть хотя бы одна буква алфавита."
    WORD_TOO_LONG = "в запросе присутствует очень длинное слово/число. " + \
                    "ограничение - не более 2000 символов/3000 цифр"
    TOO_MANY_WORDS = "в запросе очень много слов/чисел. " + \
                     "Ограничение - не более 100 слов"

    @staticmethod
    def wrap_md_mono(s: str) -> str:
        """
        Wraps s with '`' symbols.
        """
        return "`" + s + "`"

    @staticmethod
    def append_msg(s: str) -> str:
        """
        Adds 'msg: ' before s.
        """
        return "msg: " + s

    @classmethod
    def wrap_converted(cls, s: str) -> str:
        """
        Adds 'msg: ' before s wrapped with '`' symbols.
        """
        return cls.append_msg(cls.wrap_md_mono(s))


class InlineResponse(Response):
    LETTERS_MISSING = "в запросе отсутствуют буквы выбранного алфавита."

    @classmethod
    def wrap_inline_response(cls, s: str, lang_code: str, query: str) -> str:
        """
        Adds additional information about the alphabet and query.
        """
        return f"Запрос: {cls.wrap_md_mono(query)}\n" + \
               f"Результат: {cls.wrap_md_mono(s)}"

    @classmethod
    def wrap_inline_response_silent(cls, s: str):
        """
        Wraps s with '`'.
        """
        return cls.wrap_md_mono(s)
