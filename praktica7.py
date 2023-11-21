from aiogram import Bot, executor, Dispatcher, types
from keyboards7 import kb, ikb, kb_photo #импортим Файл с клавой keyboard7.py
from aiogram.dispatcher.filters import Text
import random

TOKEN_API = '6620538528:AAEsP7-wisplnKMP--pa7Kuh3LIdqlB6e14'

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

HELP_COMMAND = """
<b>/start</b> - <em>Начало нашей работы!</em>
<b>/help</b> - <em>Список комманд</em>
<b>/description</b> - <em>Описание бота</em>
<b>/GangBang</b> - <em>Отправляет Gang Bang</em>
<b>/random</b> - <em>Отправляет Рандомное местоположение</em>
"""

arr_photos = ['https://i.pinimg.com/originals/3e/7e/8d/3e7e8d107967abfb4678641b52538e54.jpg',
              'https://i.pinimg.com/originals/26/10/8c/26108cb3dcceeb508ba2c331f1dd5631.jpg',
              'https://i.pinimg.com/736x/15/c2/5e/15c25e576859d427d5ca72bbc9109e56.jpg',
              'https://i.pinimg.com/originals/38/94/f2/3894f2fc78683d4fa3ccb1d35a29a267.jpg']

photos = dict(zip(arr_photos, ['Gang', 'Duo_Gang', 'solo_gang', 'kakashi_gang']))
random_photo = random.choice(list(photos.keys()))

async def on_startup(_): #Коммент в Terminale, при запуске бота
    print('Я был запущен!')

async def send_random(message: types.Message): #Вынесем функционал фото в отдельную функцию
    global random_photo
    random_photo = random.choice(list(photos.keys()))
    await bot.send_photo(chat_id=message.chat.id,
                         photo=random_photo,
                         caption=photos[random_photo],
                         reply_markup=ikb)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer(text='Привет я бот, воспользуйся мной!',
                           reply_markup=kb)
    await message.delete()

@dp.message_handler(commands=['help'])
async def help_command(message: types.Message):
    await message.answer(text=HELP_COMMAND,
                           parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=['description'])
async def description_command(message: types.Message):
    await message.answer(text='Данный бот умеет отправлять рандомные фото')
    await bot.send_sticker(chat_id=message.chat.id,
                           sticker="CAACAgIAAxkBAAEKss1lSMfgP76x_BXeOklfdsfX_lNIJwACGBQAAk5zYEqYQmDeamJ9tDME")
    await message.delete()


#Функционал Кнопки Random photo в галвном меню
@dp.message_handler(Text(equals="Random photo"))
async def open_kb_photo(message: types.Message):
    await send_random(message)
    await message.delete()

@dp.message_handler(Text(equals="Random"))    
async def send_random_photo(message: types.Message):
    await send_random(message)

@dp.message_handler(Text(equals="Главное меню"))    
async def open_kb(message: types.Message):
    await message.answer(text='Добро пожаловать в главное меню!',
                         reply_markup=kb)
    await message.delete()

@dp.callback_query_handler()
async def callback_check(callback: types.CallbackQuery):
    global random_photo
    if callback.data == 'like':
        await callback.answer('Лайк поставлен')
        # await callback.message.answer('Лайк поставлен')
    elif callback.data == 'dislike':
        await callback.answer('Дизлайк поставлен')
        # await callback.message.answer('Дизлайк поставлен')
    else:
        random_photo = random.choice(list(filter(lambda x: x != random_photo, list(photos.keys()))))
        await callback.message.edit_media(types.InputMedia(media=random_photo,
                                                           type='photo',
                                                           caption= photos[random_photo]),
                                                           reply_markup=ikb)
        await callback.answer()


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp, skip_updates=True, on_startup=on_startup)