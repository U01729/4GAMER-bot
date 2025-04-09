from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

# زر البحث عن لعبة
def start_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("🔍 البحث عن لعبة")
    button2 = KeyboardButton("📩 انضم للقناة")
    keyboard.add(button1, button2)
    return keyboard

# زر خاص بالمشرف لإضافة ألعاب
def admin_keyboard():
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = KeyboardButton("📥 إضافة لعبة")
    button2 = KeyboardButton("📢 إرسال رسالة جماعية")
    keyboard.add(button1, button2)
    return keyboard
