from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

btnProfile = KeyboardButton('👥 ПУСТО')
btnSub = KeyboardButton('❤ ЛУЧШИЙ')
btnList = KeyboardButton('👥 ЧЕРНЫЙ СПИСОК')

mainMenu = ReplyKeyboardMarkup(resize_keyboard = True)
mainMenu.add(btnProfile, btnSub, btnList)


sub_inline_markup = InlineKeyboardMarkup(row_width=1)
btnSubMonth = InlineKeyboardButton(text="точно нужно нажать", url="https://t.me/azathd")
sub_inline_markup.insert(btnSubMonth)