from telegram import Update
from telegram.ext import ContextTypes

from keyboards import main_menu
from api import get_daily_challenges
from translations import translate


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤠 أهلاً بك في RDO Shadow Bot\n\n"
        "اختر الخدمة من القائمة بالأسفل.",
        reply_markup=main_menu(),
    )


async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = get_daily_challenges()

    if not data:
        await query.message.reply_text("❌ تعذر جلب التحديات.")
        return

    text = "🎯 تحديات اليوم\n\n"

    for section, challenges in data.items():

        if not isinstance(challenges, list):
            continue

        text += f"{translate(section)}\n"

        for challenge in challenges:
            title = translate(challenge.get("title", ""))
            goal = challenge.get("goal", "")

            text += f"• {title} ({goal})\n"

        text += "\n"

    await query.message.reply_text(text)


async def nazar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("🗺️ موقع Madam Nazar سيتم إضافته قريبًا.")


async def harriet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("🦌 Harriet سيتم إضافتها قريبًا.")


async def cripps(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("🏕️ Cripps سيتم إضافته قريبًا.")


async def monthly(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("📰 تحديثات الشهر قريبًا.")


async def limited(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("🎁 العناصر المحدودة قريبًا.")


async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.message.reply_text("ℹ️ RDO Shadow Bot")
