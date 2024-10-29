from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup 

tillar = InlineKeyboardMarkup(
    inline_keyboard=[
        [
          InlineKeyboardButton(text="🇺🇿 O'zbek",callback_data="O'zbek"),
          InlineKeyboardButton(text="🇷🇺 Русский",callback_data="русский"),
        ],
    ], row_width=True
)