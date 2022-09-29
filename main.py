import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.message import ContentType
import markups as nav
from db import Database

import time
import datetime

TOKEN = "1206033024:AAEcEtMiuQ-EcQgRWfzsK6nMTFVsNJL85JU"

logging.basicConfig(level=logging.INFO)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

db = Database('database.db')

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_message(message.from_user.id, "Привет, дружище! Нажимай на кнопочки.", reply_markup=nav.mainMenu)


@dp.message_handler()
async def bot_message(message: types.Message):
    if message.chat.type == 'private':
        if message.text == '👥 ПУСТО':
            await bot.send_message(message.from_user.id, "ты че не понял меня?", reply_markup=nav.mainMenu)
        elif message.text == '❤ ЛУЧШИЙ':
            await bot.send_message(message.from_user.id, "Этот чел точно красава", reply_markup=nav.sub_inline_markup)
        elif message.text == '👥 ЧЕРНЫЙ СПИСОК':
            await bot.send_message(message.from_user.id, "@aza_kad <-- сам ищи, даже ссылку на него давать - грех.", reply_markup=nav.mainMenu)


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates = True)
