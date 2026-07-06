async def daily(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    data = get_daily_challenges()

    if not data:
        await query.message.reply_text("❌ تعذر جلب التحديات.")
        return

    text = "🎯 تحديات اليوم\n\n"

    # التحديات العامة
    if "general" in data:
        text += "🌍 التحديات العامة\n"

        for challenge in data["general"]:
            title = translate(challenge.get("title", ""))
            goal = challenge.get("goal", "")
            text += f"• {title} ({goal})\n"

        text += "\n"

    # تحديات الوظائف
    for level in ["easy", "med", "hard"]:

        if level not in data:
            continue

        for role, challenges in data[level].items():

            text += f"{translate(role)}\n"

            for challenge in challenges:
                title = translate(challenge.get("title", ""))
                goal = challenge.get("goal", "")
                text += f"• {title} ({goal})\n"

            text += "\n"

    await query.message.reply_text(text)
