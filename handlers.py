from telegram import Update
from telegram.ext import ContextTypes

from api import get_daily_challenges


async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = get_daily_challenges()

    if not data:
        await update.message.reply_text(
            "❌ تعذر جلب التحديات حالياً، حاول مرة أخرى لاحقاً."
        )
        return

    message = "🎯 تحديات Red Dead Online اليومية\n\n"

    try:
        if "general" in data:
            message += "🌍 التحديات العامة\n"
            for challenge in data["general"]:
                message += f"• {challenge}\n"

        await update.message.reply_text(message)

    except Exception:
        await update.message.reply_text(
            "⚠️ حدث خطأ أثناء قراءة بيانات التحديات."
        )


async def all_challenges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await daily(update, context)
