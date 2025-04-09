from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# إضافة التوكن والإيدي مباشرة هنا
API_TOKEN = '7710703665:AAHP7QUj-UsWKYDEpnOEgViPZp6BHC4Vd4o'
ADMIN_ID = 928585571  # الإيدي الخاص بك

# إعداد البوت
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# قائمة الألعاب
games = []

# قائمة لحفظ المستخدمين الذين تفاعلوا مع البوت
users = set()

# أمر /start
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    users.add(message.from_user.id)
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton("ألعاب PS4"))
    await message.answer("مرحباً بك في 4GAMER بوت!", reply_markup=keyboard)

# أمر /broadcast لإرسال رسالة جماعية
@dp.message_handler(commands=['broadcast'])
async def broadcast(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("أنت غير مصرح لك باستخدام هذا الأمر.")
    
    await message.answer("أرسل الآن الرسالة التي تريد إرسالها للمستخدمين.")

    @dp.message_handler()
    async def get_broadcast(msg: types.Message):
        for user_id in users:
            try:
                await bot.send_message(user_id, msg.text)
            except:
                continue
        await msg.answer("تم إرسال الرسالة بنجاح.")

# أمر /addgame لإضافة لعبة جديدة
@dp.message_handler(commands=['addgame'])
async def add_game(message: types.Message):
    if message.from_user.id != ADMIN_ID:
        return await message.answer("أمر غير مسموح لك.")
    
    await message.answer("أرسل اسم اللعبة مع الرابط بالشكل التالي:\n\nاسم اللعبة - الرابط")

    @dp.message_handler()
    async def save_game(msg: types.Message):
        games.append(msg.text)
        await msg.answer("تمت إضافة اللعبة!")

# زر "ألعاب PS4"
@dp.message_handler(lambda message: message.text == "ألعاب PS4")
async def show_games(message: types.Message):
    if not games:
        await message.answer("لا توجد ألعاب مضافة بعد.")
    else:
        reply = "\n\n".join(games)
        await message.answer(f"قائمة الألعاب:\n\n{reply}")

# تشغيل البوت
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
