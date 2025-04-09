# handlers/user.py
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

async def start_cmd(message: types.Message):
    # عند إرسال أمر /start
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("ألعاب PS4"))
    await message.answer("مرحبًا بك في 4GAMER بوت!", reply_markup=keyboard)

def setup(dp):
    dp.register_message_handler(start_cmd, commands=['start'])
