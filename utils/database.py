import sqlite3

# إنشاء اتصال بقاعدة البيانات
def init_db():
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()

    # إنشاء جدول لتخزين الألعاب إذا لم يكن موجودًا
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS games (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            download_link TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()

# إضافة لعبة جديدة إلى قاعدة البيانات
def add_game(name: str, download_link: str):
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO games (name, download_link)
        VALUES (?, ?)
    ''', (name, download_link))

    conn.commit()
    conn.close()

# استرجاع جميع الألعاب
def get_all_games():
    conn = sqlite3.connect('games.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM games')
    games = cursor.fetchall()

    conn.close()
    return games
