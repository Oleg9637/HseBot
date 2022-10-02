from aiogram import types
from loader import dp


@dp.message_handler(text='/timer')
async def command_timer(message: types.Message):
    await message.answer(f'hello, How often do I kick you')
