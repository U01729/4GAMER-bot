from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import ADMIN_ID

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

def setup(dp):
    dp.register_message_handler(broadcast, commands=["broadcast"])
    dp.register_message_handler(add_game, commands=["addgame"])
