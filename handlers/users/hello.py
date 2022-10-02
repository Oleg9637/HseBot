from aiogram import types
from loader import dp


@dp.message_handler(text='/hello')
async def command_start(message: types.Message):
    await message.answer(f'hello {message.from_user.full_name}!')
