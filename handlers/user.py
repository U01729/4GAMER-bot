from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import ADMIN_ID
from bot import dp

# تعريف لوحة المفاتيح الخاصة بـ "start"
def start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("ألعاب PS4")
    button2 = KeyboardButton("انضم إلى القناة")
    keyboard.add(button1, button2)
    return keyboard

# أمر /start
@dp.message_handler(commands=["start"])
async def start_cmd(message: types.Message):
    await message.answer(
        "مرحباً بك في 4GAMER بوت!", reply_markup=start_keyboard()
    )

# أمر للبحث عن الألعاب
@dp.message_handler(lambda message: message.text == "ألعاب PS4")
async def search_game(message: types.Message):
    # هنا تضع الكود لعرض الألعاب
    await message.answer("قائمة الألعاب...")

# أمر للانضمام للقناة
@dp.message_handler(lambda message: message.text == "انضم إلى القناة")
async def join_channel(message: types.Message):
    await message.answer("يمكنك الانضمام إلى قناتنا على Telegram هنا: https://t.me/4GAMER_Channel")
