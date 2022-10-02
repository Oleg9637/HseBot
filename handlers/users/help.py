from aiogram import types
from loader import dp


@dp.message_handler(text='/help')
async def command_start(message: types.Message):
    await message.answer(f'/start \n'
                         f'/menu \n'
                         f'/help')
