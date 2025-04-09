from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils import executor

API_TOKEN = '7710703665:AAHP7QUj-UsWKYDEpnOEgViPZp6BHC4Vd4o'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# قاعدة بيانات وهمية
fake_database = {
    "ps4": ["God of War", "Spider-Man", "Horizon Zero Dawn"],
    "ps5": ["Demon's Souls", "Ratchet & Clank", "Returnal"],
    "tools": ["PSX Downloader", "Game Splitter", "Save Mounter"],
    "tutorials": ["Unzip Game", "Transfer Game", "Launch Game"]
}

# ترجمة المحتوى
translations = {
    "ar": {
        "welcome": "مرحباً بك في بوت 4GAMER!\nاختر أحد التصنيفات:",
        "ps4": "ألعاب PS4",
        "ps5": "ألعاب PS5",
        "tools": "أدوات مساعدة",
        "tutorials": "شروحات",
        "back": "العودة",
        "language": "تغيير اللغة",
        "select_lang": "اختر لغتك:",
        "content": "المحتوى المتوفر في"
    },
    "en": {
        "welcome": "Welcome to 4GAMER Bot!\nChoose a category:",
        "ps4": "PS4 Games",
        "ps5": "PS5 Games",
        "tools": "Tools",
        "tutorials": "Tutorials",
        "back": "Back",
        "language": "Change Language",
        "select_lang": "Select your language:",
        "content": "Available content in"
    }
}

# --- لوحة اختيار اللغة ---
def language_menu():
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton("العربية", callback_data="lang_ar"),
        InlineKeyboardButton("English", callback_data="lang_en")
    )

# --- القائمة الرئيسية ---
def main_menu(lang="en"):
    t = translations[lang]
    return InlineKeyboardMarkup(row_width=2).add(
        InlineKeyboardButton(t["ps4"], callback_data=f"category_ps4_{lang}"),
        InlineKeyboardButton(t["ps5"], callback_data=f"category_ps5_{lang}"),
        InlineKeyboardButton(t["tools"], callback_data=f"category_tools_{lang}"),
        InlineKeyboardButton(t["tutorials"], callback_data=f"category_tutorials_{lang}"),
        InlineKeyboardButton(t["language"], callback_data="change_lang")
    )

# --- زر الرجوع فقط ---
def back_menu(lang="en"):
    t = translations[lang]
    return InlineKeyboardMarkup().add(
        InlineKeyboardButton(t["back"], callback_data=f"back_{lang}")
    )

# --- /start: اختيار اللغة أولاً ---
@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message):
    await message.answer(translations['ar']['select_lang'], reply_markup=language_menu())

# --- عند اختيار اللغة ---
@dp.callback_query_handler(lambda c: c.data.startswith("lang_"))
async def set_language(callback_query: types.CallbackQuery):
    lang = callback_query.data.split("_")[1]
    t = translations[lang]
    await callback_query.message.edit_text(t["welcome"], reply_markup=main_menu(lang))
    await callback_query.answer()

# --- تغيير اللغة من القائمة ---
@dp.callback_query_handler(lambda c: c.data == "change_lang")
async def change_lang(callback_query: types.CallbackQuery):
    await callback_query.message.edit_text("Select your language:", reply_markup=language_menu())
    await callback_query.answer()

# --- عرض المحتوى حسب التصنيف واللغة ---
@dp.callback_query_handler(lambda c: c.data.startswith("category_"))
async def show_category(callback_query: types.CallbackQuery):
    _, cat_key, lang = callback_query.data.split("_")
    content = fake_database.get(cat_key, [])
    t = translations[lang]
    text = f"**{t['content']} {cat_key.upper()}**\n" + "\n".join([f"- {item}" for item in content])
    await callback_query.message.edit_text(text, reply_markup=back_menu(lang), parse_mode="Markdown")
    await callback_query.answer()

# --- زر العودة ---
@dp.callback_query_handler(lambda c: c.data.startswith("back_"))
async def go_back(callback_query: types.CallbackQuery):
    lang = callback_query.data.split("_")[1]
    t = translations[lang]
    await callback_query.message.edit_text(t["welcome"], reply_markup=main_menu(lang))
    await callback_query.answer()

# --- تشغيل البوت ---
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
