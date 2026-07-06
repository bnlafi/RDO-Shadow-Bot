from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
)

from config import BOT_TOKEN

from handlers import (
    start,
    daily,
    nazar,
    harriet,
    cripps,
    monthly,
    limited,
    help_cmd,
)


def main():

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

    app.add_handler(CallbackQueryHandler(daily, pattern="^daily$"))
    app.add_handler(CallbackQueryHandler(nazar, pattern="^nazar$"))
    app.add_handler(CallbackQueryHandler(harriet, pattern="^harriet$"))
    app.add_handler(CallbackQueryHandler(cripps, pattern="^cripps$"))
    app.add_handler(CallbackQueryHandler(monthly, pattern="^monthly$"))
    app.add_handler(CallbackQueryHandler(limited, pattern="^limited$"))
    app.add_handler(CallbackQueryHandler(help_cmd, pattern="^help$"))

    print("✅ RDO Shadow Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
