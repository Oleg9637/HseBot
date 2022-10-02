from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Видеоматериалы '),
            KeyboardButton(text='Дополнительные материалы '),
        ],
    ],
    resize_keyboard=True
)
