# wordlexord_bot

Этот бот показывает функционал питоновского пакета [wordlexord](https://github.com/lindy2076/words-serial-number).

[Ссылка](https://t.me/wordlexord_bot) на бота в телеграм.

Перевод осуществляется так:

`[alphabet] [text]`, где *alphabet* - один из доступных алфавитов, а *text* - либо предложение, для слов которого необходимо получить порядковые номера, либо порядковые номера, которые надо перевести в слова.

### алфавиты:
пока доступны:
- **enl** - **en**glish **l**ower case (`abcdefghijkl`)
- **enu** - **en**glish **u**pper case
- **руу** - **русский** **у**ппер кейс
- **рул** - **русский** **л**овер кейс


### примеры:

1. req: `enl hello there i am using github`

    res: `msg: 3752127 9283981 9 39 9936895 87639892`

2. req: `enl 9 221629 5877569419735112053`

    res: `msg: i love bioinformatics`

3. req: `рул привет`

    res: `msg: 687011114`

