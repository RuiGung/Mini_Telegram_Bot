from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove

kb = ReplyKeyboardMarkup(resize_keyboard=True)

b1 = KeyboardButton(text='/help')
b2 = KeyboardButton(text='/description')
b3 = KeyboardButton(text='Random photo')

kb.add(b1, b2).insert(b3)

#Клава для фото
kb_photo = ReplyKeyboardMarkup(resize_keyboard=True)
bp1 = KeyboardButton(text='Random')
bp2 = KeyboardButton(text='Главное меню')


# Кнокпи для интерфейса кнопок
kb_photo.add(bp1, bp2)

ikb = InlineKeyboardMarkup(row_width=3)

ib1 = InlineKeyboardButton(text='❤️ ',
                           callback_data="like")
ib2 = InlineKeyboardButton(text='🖤 ',
                           callback_data="dislike")
ib3 = InlineKeyboardButton(text='next random images',
                           callback_data="NextImages")

ikb.add(ib1, ib2).add(ib3)