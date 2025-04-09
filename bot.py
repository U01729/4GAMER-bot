# bot.py
from aiogram import Bot, Dispatcher
from aiogram.types import ParseMode
from aiogram.utils import executor
import logging
from config import BOT_TOKEN

# تكوين تسجيل الدخول
logging.basicConfig(level=logging.INFO)

# تعريف البوت والموزع (dispatcher)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# استيراد ملفات المعالجات بعد تعريف dp لتجنب الاستيراد الدائري
from handlers import user, admin

# إعداد الأوامر باستخدام setup
user.setup(dp)
admin.setup(dp)

# تشغيل البوت باستخدام polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
