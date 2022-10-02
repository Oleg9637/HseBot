from aiogram import types
from loader import dp


@dp.message_handler(text='Видеоматериалы')
async def buttons_test(message: types.Message):
    await message.answer(f'https://www.youtube.com/watch?v=34Rp6KVGIEM&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa')


@dp.message_handler(text='Дополнительные материалы')
async def buttons_test(message: types.Message):
    await message.answer(f'https://pythonworld.ru/samouchitel-python')
