## Parsing tesaminan News
### ТЗ:
```
Сайт: https://www.tesmanian.com/

Що треба реалізувати:

1. Скрипт, який скрапить сайт 24/7 з інтервалом у 15 секунд.
2. Логін має бути один раз (або коли отримуємо unauthirized error), 
	щоб нас не запідозрили у спамі
3. На виході мають бути тільки нові результати (у порівняня з попередньою перевіркою 15 сек тому)
	у телеграм канал. Відсилати потрібно title статті і посилання на неї.

```

---
## Description

Get the latest news from 'https://www.tesmanian.com/blogs/tesmanian-blog', send them to a Telegram channel, and save the news in a JSON file `'./data/news.json'`.

Request every 15 sec.

Logfile: log_scraping.log

---
## Dependencies:

    - Linux
    - Python (v3.10)

---
## Instruction for run 

1. download script: 
2. Open directory 'scrap_tesmanian': cd spa_comments/

3. Initialize environment:
```
python3.10 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
4. Create config file named: 'config.cfg'

Content 'config.cfg':
```
[user]
LOGIN = [login for https://www.tesmanian.com/account/login]
PASSWORD = [password for https://www.tesmanian.com/account/login]

[bot]
BOT_TOKEN = [telegram bot_token]
CHAT_ID = [telegram chat id]
```

5. run script: `python3 main.py`
