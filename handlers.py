from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    await update.message.reply_text(
        "🤠 أهلاً بك في RDO Shadow Bot\n\n"
        "اختر الخدمة من القائمة بالأسفل.",
        reply_markup=main_menu(),
    )
