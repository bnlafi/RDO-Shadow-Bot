from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤠 أهلاً بك في RDO Shadow Bot\n\n"
        "اختر الخدمة من القائمة بالأسفل.",
        reply_markup=main_menu(),
    )


async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎯 تحديثات اليوم\n\n"
        "⚠️ سيتم جلب التحديات تلقائياً قريباً."
    )


async def nazar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🗺️ موقع Madam Nazar\n\n"
        "⚠️ سيتم جلب الموقع تلقائياً قريباً."
    )


async def harriet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🦌 Harriet\n\n"
        "⚠️ قريباً."
    )


async def cripps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🏕️ Cripps\n\n"
        "⚠️ قريباً."
    )


async def monthly(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📰 تحديثات الشهر\n\n"
        "⚠️ قريباً."
    )


async def limited(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎁 العناصر المحدودة\n\n"
        "⚠️ قريباً."
    )


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ المساعدة\n\n"
        "إذا واجهت أي مشكلة تواصل مع الإدارة."
    )
