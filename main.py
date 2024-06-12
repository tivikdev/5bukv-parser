import requests
import codecs
from bs4 import BeautifulSoup


url = 'https://littlewords.ru/'
class_ = 'entry-content'
page_directory = 'index.html'
fullpage = '''<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="content-type" content="text/html; charset=UTF-8">
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="icon" type="image/png" href="/favicon.png">
        <meta name="description" content="Ответы на игру в Тинькофф (Т-Банк). Только сегодняшнее слово из 5 Букв. Пять букв - Ничего больше.">
        <title>5 Букв. Только слово.</title>
    <style>
        :root {
            --button-color: #ffdd2d;
            --button-color-pressed: #fab619;
        }
        @media (hover:hover) {
            .button:hover {
                background-color: var(--button-color-pressed);
            }
        }
        @media (hover:none) {
            .button:active {
                background-color: var(--button-color-pressed);
            }
        }
        body {
            margin: 0;
            font-family: Verdana;
        }
        main {
            height: 95vh;
            display: flex;
            flex-direction: column;
            justify-content: center;
            align-items: center;
        }
        #dword {
            text-transform:uppercase;
        }
        .button {
            border-radius: 8px;
            background-color: var(--button-color);
            color: black;
            border: none;
            padding: 20px 34px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 20px;
            margin: 4px 2px;
            cursor: pointer;
            text-transform: uppercase;
            transition: 0.2s;
        }
        header {
            display: flex;
            justify-content: flex-start;
            background-color: black;
            text-align: center;
            line-height: 60px;
            font-size: 18px;
            border: none;
            position:fixed;
            width:100vw;
        }
            header > a {
                min-width: 10vw;
                text-decoration: none;
                font-weight: bold;
                color: var(--button-color);
                margin-inline: 25px;
            }
    </style>
</head>
<body>
    <header>
        <a class="logo" href="/">tivik.dev</a>
    </header>
    <main>
        <h1 id="dword">dailyWord</h1>
        <a class="button" href="https://l.tinkoff.ru/5bukv_web" target="_blank" rel="noopener noreferrer">В игру</a>
    </main>
</body>
</html>'''


def get_last_word(string):
    last_string = list(string.split(" "))
    return last_string[len(last_string)-1]


r = requests.get(url)
html = BeautifulSoup(r.text, 'html.parser').find(class_ = class_)
collection = []
for word in html.find_all('li'):
    text = BeautifulSoup.get_text(word)
    if text[0].isdigit():
        collection.append(text)

fullpage = fullpage.replace("dailyWord", get_last_word(collection[-1]))
file = codecs.open(page_directory, 'w', "utf-8")
file.write(fullpage)
file.close()
