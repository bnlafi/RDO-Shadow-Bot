from telegram.ext import (
    Application,
    CommandHandler,
)

BOT_TOKEN = "8725115947:AAHchYsmnNOdgSNl0xEIvN5X0Vl5pG2fP-Q"

GROUP_CHAT_ID = -1003973562124

from handlers import start


def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    print("✅ RDO Shadow Bot Started")
    print(f"Group ID: {GROUP_CHAT_ID}")

    app.run_polling()


if __name__ == "__main__":
    main()
