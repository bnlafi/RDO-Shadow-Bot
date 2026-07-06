from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

BOT_TOKEN = "8725115947:AAHchYsmnNOdgSNl0xEIvN5X0Vl5pG2fP-Q"

GROUP_CHAT_ID = -1003973562124


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤠 أهلاً بك في RDO Shadow Bot\n\n"
        "البوت قيد التطوير وسيتم إضافة جميع المميزات قريبًا."
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - تشغيل البوت\n"
        "/help - المساعدة"
    )


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))

    print("RDO Shadow Bot Started...")
    print(f"Group ID: {GROUP_CHAT_ID}")

    app.run_polling()


if __name__ == "__main__":
    main()
