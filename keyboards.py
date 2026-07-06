from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def main_menu():
    keyboard = [
        [
            InlineKeyboardButton("🎯 تحديات اليوم", callback_data="daily"),
            InlineKeyboardButton("🗺️ Madam Nazar", callback_data="nazar"),
        ],
        [
            InlineKeyboardButton("🦌 Harriet", callback_data="harriet"),
            InlineKeyboardButton("🏕️ Cripps", callback_data="cripps"),
        ],
        [
            InlineKeyboardButton("📰 تحديثات الشهر", callback_data="monthly"),
            InlineKeyboardButton("🎁 العناصر المحدودة", callback_data="limited"),
        ],
        [
            InlineKeyboardButton("⚙️ الإدارة", callback_data="admin"),
            InlineKeyboardButton("ℹ️ المساعدة", callback_data="help"),
        ],
    ]

    return InlineKeyboardMarkup(keyboard)
