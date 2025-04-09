from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

# تكوين تسجيل الدخول
logging.basicConfig(level=logging.INFO)

# استيراد التوكن من ملف config.py
from config import BOT_TOKEN

# تعريف البوت والموزع (dispatcher)
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# الآن، بعد تعريف dp، يمكننا استيراد handler.
# استيراد أوامر المستخدم والمشرف بعد تعريف dp لتجنب الاستيراد الدائري
from handlers import user, admin

# تشغيل الأوامر
user.setup(dp)
admin.setup(dp)

# تشغيل البوت باستخدام polling
if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
