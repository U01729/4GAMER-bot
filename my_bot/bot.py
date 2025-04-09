from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor

API_TOKEN = '7710703665:AAHP7QUj-UsWKYDEpnOEgViPZp6BHC4Vd4o'  # استبدل هذا بالتوكن الخاص بك

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# فئات وهمية للتجربة
categories = ["PS4 Games", "PS5 Games", "Tools", "Tutorials", "Join Channel"]

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    buttons = [KeyboardButton(cat) for cat in categories]
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True).add(*buttons)
    await message.answer("Welcome to 4GAMER Bot! Choose a category or send a keyword to search:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text in categories)
async def category_selected(message: types.Message):
    category = message.text
    if category == "PS4 Games":
        await message.answer("Here are some PS4 games:\n- Game 1\n- Game 2\n- Game 3")
    elif category == "PS5 Games":
        await message.answer("Here are some PS5 games:\n- Game A\n- Game B\n- Game C")
    elif category == "Tools":
        await message.answer("Here are some tools:\n- Tool 1\n- Tool 2\n- Tool 3")
    elif category == "Tutorials":
        await message.answer("Here are some tutorials:\n- Tutorial 1\n- Tutorial 2\n- Tutorial 3")
    elif category == "Join Channel":
        await message.answer("Join our channel here: [Channel Link]")

@dp.message_handler()
async def search(message: types.Message):
    keyword = message.text.lower()
    results = f"Results for '{keyword}':\n- Game 1\n- Game 2\n- Game 3"
    await message.answer(results)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
