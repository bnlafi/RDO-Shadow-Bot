from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎯 تحديات اليوم", callback_data="daily")],
        [InlineKeyboardButton("🗺️ موقع مادام نازار", callback_data="nazar")],
        [InlineKeyboardButton("📅 تحديثات الشهر", callback_data="monthly")],
        [InlineKeyboardButton("🎁 العناصر النادرة", callback_data="limited")],
        [InlineKeyboardButton("ℹ️ المساعدة", callback_data="help")]
    ]

    await update.message.reply_text(
        "🤠 أهلاً بك في RDO Shadow Bot\n\n"
        "اختر الخدمة التي تريدها:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
