from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
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

    app.add_handler(MessageHandler(filters.Regex("^🎯 تحديثات اليوم$"), daily))
    app.add_handler(MessageHandler(filters.Regex("^🗺️ Madam Nazar$"), nazar))
    app.add_handler(MessageHandler(filters.Regex("^🦌 Harriet$"), harriet))
    app.add_handler(MessageHandler(filters.Regex("^🏕️ Cripps$"), cripps))
    app.add_handler(MessageHandler(filters.Regex("^📰 تحديثات الشهر$"), monthly))
    app.add_handler(MessageHandler(filters.Regex("^🎁 العناصر المحدودة$"), limited))
    app.add_handler(MessageHandler(filters.Regex("^ℹ️ المساعدة$"), help_cmd))

    print("✅ RDO Shadow Bot Started")

    app.run_polling()


if __name__ == "__main__":
    main()
