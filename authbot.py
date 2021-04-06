from pyrogram import Client
from pyrogram import filters
from pyrogram import types
import sqlite3
import time
import random
import asyncio
app = Client('my_accounts')

my_id = 44520977
id_chat= '-1001389712083'

@app.on_message(filters.command('b'))
async def echo (client,message):
    print(message.chat.id)
    if message.from_user.id == my_id:
        id_user = message.chat.id
        try:
            await app.add_chat_members(chat_id=id_chat,user_ids=id_user)
            await app.send_message(chat_id=message.chat.id, text='Добавил тебя в чат')
        except:
            await app.send_message(chat_id=message.chat.id, text="""Не могу тебя добавить в чат так как тебя запрещено добавлять в беседы
Что бы это исправить переходи в настройки, нажимай

- Конфидециальность
- Группы и каналы
И добавь меня в список тех, кто тебя может приглашать в группы

После этого напиши мне  и мы повторим попытку""")



@app.on_message(filters.text)
async def payments (client,message):
    print(message)
    if message.from_user.id == my_id and message.text == 'Рр':
        await app.edit_message_text(message_id=message.message_id,chat_id=message.chat.id,text="""🇷🇺Если ты с РФ
4048 4150 0303 3277


🇰🇬Если с Кыргызстана
Mbank online : 996552152071
Можно через банкомат


🇺🇿Если ты с Узбекистана:
uzcard - 8600 1204 2026 7414
AKSENOVA ANGELINA


🇰🇿Казахстан КАСПИ - +77088338356


🥝Так же ты можешь оплатить на киви:
+79183561047

💰Юмани(ЯндексДеньги):
410019301888334


Сумма для оплаты :
Для РФ - 354р
Для Кыргызстана - 407 сом
Для Узбекистана - 50 150 сум
Для Казахстана - 2005 тенге

Чек сюда, после проверки добавлю в чат!""",parse_mode='html')

app.run()