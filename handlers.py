from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤠 أهلاً بك في RDO Shadow Bot\n\nاختر الخدمة:",
        reply_markup=main_menu(),
    )


async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "🎯 تحديات اليوم\n\nسيتم جلب التحديات قريباً."
    )


async def nazar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "🗺️ موقع Madam Nazar\n\nسيتم إضافته قريباً."
    )


async def harriet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "🦌 Harriet\n\nقريباً."
    )


async def cripps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "🏕️ Cripps\n\nقريباً."
    )


async def monthly(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "📰 تحديثات الشهر\n\nقريباً."
    )


async def limited(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "🎁 العناصر المحدودة\n\nقريباً."
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text(
        "ℹ️ المساعدة\n\nRDO Shadow Bot"
    )
