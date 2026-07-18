import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

BOT_TOKEN = "8926638329:AAEdpnU5a3hWfJpMzRmpNOvmTEBj9vR-af4"
bot = telebot.TeleBot(BOT_TOKEN)

MAIN_TEXT = (
    "👨🏻‍🔧 بوت فنس يرحّب فيكم\n"
    "📰 دليل متكامل لأبرز وصفات فنس\n\n"
    "قم بالضغط على أحد الأزرار بالأسفل للحصول على الوصفة أو المعلومة اللي تحتاجها 📝"
)

WELCOME_TEXT = (
    "👨🏻‍🔧 بوت فنس يرحّب فيكم\n"
    "📰 دليل متكامل لأبرز وصفات فنس\n\n"
    "لتفعيل البوت أكتب :\n"
    "فنس أو fenc"
)

# ================= MENUS =================

def main_menu(uid):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🔫 الأسلحة", callback_data=f"weapons|{uid}"),
        InlineKeyboardButton("🧨 المتفجرات", callback_data=f"explosive|{uid}"),
        InlineKeyboardButton("📦 زيادة مخزون الأسلحة", callback_data=f"ammo_pouch|{uid}"),
        InlineKeyboardButton("⚕️ تونيكات الصحة", callback_data=f"health|{uid}"),
        InlineKeyboardButton("🐎 الأحصنة", callback_data=f"horse|{uid}"),
        InlineKeyboardButton("🍳 الطبخ", callback_data=f"cooking|{uid}"),
        InlineKeyboardButton("⛺ المخيم المتنقل", callback_data=f"travel|{uid}"),
        InlineKeyboardButton("❌ إغلاق", callback_data=f"close|{uid}")
    )
    return kb

def back(uid, to="main"):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🔙 رجوع", callback_data=f"{to}|{uid}"),
        InlineKeyboardButton("❌ إغلاق", callback_data=f"close|{uid}")
    )
    return kb

# -------- Weapons Menu --------
def weapons_menu(uid):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🔥 الرصاص الناري", callback_data=f"incendiary|{uid}"),
        InlineKeyboardButton("🔥 السهم الناري", callback_data=f"fire_arrow|{uid}"),
        InlineKeyboardButton("🏹 الأسهم الصغيرة", callback_data=f"small_arrow|{uid}"),
        InlineKeyboardButton("🧨 سهم الديناميت", callback_data=f"dynamite_arrow|{uid}"),
        InlineKeyboardButton("🔥 زجاجة النار المتقلبة", callback_data=f"fire_bottle|{uid}"),
        InlineKeyboardButton("☠️ السهم السام", callback_data=f"poison_arrow|{uid}"),
        InlineKeyboardButton("☠️ السكين السامة", callback_data=f"poison_knife|{uid}")
    )
    kb.row(InlineKeyboardButton("🔙 رجوع", callback_data=f"main|{uid}"), InlineKeyboardButton("❌ إغلاق", callback_data=f"close|{uid}"))
    return kb

# -------- Explosive Menu --------
def explosive_menu(uid):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🏹 الأسهم المتفجرة", callback_data=f"explosive_arrow|{uid}"),
        InlineKeyboardButton("💣 الرصاص المتفجر", callback_data=f"explosive_ammo|{uid}"),
        InlineKeyboardButton("🧨 الديناميت المتفجر", callback_data=f"volatile_dynamite|{uid}")
    )
    kb.row(InlineKeyboardButton("🔙 رجوع", callback_data=f"main|{uid}"), InlineKeyboardButton("❌ إغلاق", callback_data=f"close|{uid}"))
    return kb

# -------- Ammo Pouch Menu --------
def ammo_pouch_menu(uid):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🎯 الرايفل", callback_data=f"rifle_pouch|{uid}"),
        InlineKeyboardButton("🔫 الريبيتر", callback_data=f"repeater_pouch|{uid}"),
        InlineKeyboardButton("🔫 البستول", callback_data=f"pistol_pouch|{uid}"),
        InlineKeyboardButton("🔫 الفارمنت", callback_data=f"varmint_pouch|{uid}"),
        InlineKeyboardButton("🏹 الأسهم", callback_data=f"arrow_pouch|{uid}"),
        InlineKeyboardButton("💥 الشوتغن", callback_data=f"shotgun_pouch|{uid}"),
        InlineKeyboardButton("🔫 الريفولفر", callback_data=f"revolver_pouch|{uid}"),
        InlineKeyboardButton("💡 نصائح زيادة السعة", callback_data=f"ammo_tips|{uid}")
    )
    kb.row(InlineKeyboardButton("🔙 رجوع", callback_data=f"main|{uid}"), InlineKeyboardButton("❌ إغلاق", callback_data=f"close|{uid}"))
    return kb

# -------- Horse Menu --------
def horse_menu(uid):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("🧴 مرهم الأحصنة", callback_data=f"horse_ointment|{uid}"),
        InlineKeyboardButton("🍽️ وجبة الأحصنة", callback_data=f"horse_meal|{uid}"),
        InlineKeyboardButton("💊 دواء الأحصنة الخاص", callback_data=f"horse_medicine|{uid}"),
        InlineKeyboardButton("⚡ منشط الأحصنة الخاص", callback_data=f"horse_stimulant|{uid}"),
        InlineKeyboardButton("❤️‍🩹 منقذ الأحصنة", callback_data=f"horse_reviver|{uid}"),
        InlineKeyboardButton("📘 نصائح العناية بالأحصنة", callback_data=f"horse_tips|{uid}")
    )
    kb.row(InlineKeyboardButton("🔙 رجوع", callback_data=f"main|{uid}"), InlineKeyboardButton("❌ إغلاق", callback_data=f"close|{uid}"))
    return kb

# -------- Health Menu --------
def health_menu(uid):
    kb = InlineKeyboardMarkup(row_width=2)
    kb.add(
        InlineKeyboardButton("❤️ تونيك الصحة", callback_data=f"health_cure|{uid}"),
        InlineKeyboardButton("👁️ تونيك الديد آي", callback_data=f"snake_oil|{uid}"),
        InlineKeyboardButton("💪 تونيك القوة", callback_data=f"miracle_tonic|{uid}"),
        InlineKeyboardButton("⚡ تونيك الطاقة", callback_data=f"bitters|{uid}")
    )
    kb.row(InlineKeyboardButton("🔙 رجوع", callback_data=f"main|{uid}"), InlineKeyboardButton("❌ إغلاق", callback_data=f"close|{uid}"))
    return kb

# ================= START =================

@bot.message_handler(commands=["start"])
def start(msg):
    if msg.chat.type == "private":
        bot.send_message(msg.chat.id, WELCOME_TEXT, protect_content=True)
    else:
        bot.send_message(msg.chat.id, MAIN_TEXT, reply_markup=main_menu(msg.from_user.id), protect_content=True)

@bot.message_handler(func=lambda m: m.text and m.text.lower() in ["فنس", "fenc"])
def open_menu(msg):
    uid = msg.from_user.id
    bot.send_message(msg.chat.id, MAIN_TEXT, reply_markup=main_menu(uid), protect_content=True)

# ================= CALLBACK =================

@bot.callback_query_handler(func=lambda call: True)
def cb(call):
    try:
        action, uid_str = call.data.split("|")
        uid = int(uid_str)
    except:
        return

    if call.from_user.id != uid:
        bot.answer_callback_query(call.id, "❌ هذه القائمة ليست لك", show_alert=True)
        return

    bot.answer_callback_query(call.id)

    if action == "main":
        bot.edit_message_text(MAIN_TEXT, call.message.chat.id, call.message.message_id, reply_markup=main_menu(uid))

    elif action == "weapons":
        bot.edit_message_text("🔫 قسم الأسلحة:", call.message.chat.id, call.message.message_id, reply_markup=weapons_menu(uid))

    elif action == "incendiary":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🔥 Incendiary Buckshot Pamphlet\n\n"
            "المتطلبات:\n"
            "طلقات + مشروب مونشاين (تلاقونه عند فنس)\n\n"
            "المميزات:\n"
            "طلق ناري",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "weapons")
        )

    elif action == "fire_arrow":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🔥 Fire Arrow Pamphlet\n\n"
            "المتطلبات:\n"
            "سهم + دهن + ريش\n\n"
            "المميزات:\n"
            "سهم ناري",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "weapons")
        )

    elif action == "small_arrow":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🏹 Small Game Arrow Pamphlet\n\n"
            "المتطلبات:\n"
            "سهم عادي\n"
            "ريش\n"
            "طلق شوتغن\n\n"
            "المميزات:\n"
            "مخصص للحيوانات الصغيرة و أفضل طريقة للحصول على جلود بيرفكت 3 نجوم",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "weapons")
        )

    elif action == "dynamite_arrow":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🧨 Dynamite Arrow Pamphlet\n\n"
            "المتطلبات:\n"
            "سهم + ديناميت + ريشة\n\n"
            "المميزات:\n"
            "سهم متفجر",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "weapons")
        )

    elif action == "fire_bottle":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🔥 Volatile Fire Bottle Pamphlet\n\n"
            "المتطلبات:\n"
            "مونشاين + دهون حيوانية\n\n"
            "المميزات:\n"
            "قنبلة مولوتوف أقوى من العادي",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "weapons")
        )

    elif action == "poison_arrow":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "☠️ Poison Arrow Pamphlet\n\n"
            "المتطلبات:\n"
            "Oleander + سهم + ريشة\n\n"
            "المميزات:\n"
            "يسمم العدو",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "weapons")
        )

    elif action == "poison_knife":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "☠️ Poison Throwing Knife Pamphlet\n\n"
            "المتطلبات:\n"
            "سكين رمي ( من فنس ) + Oleander\n\n"
            "المميزات:\n"
            "يسبب التسمم للعدو",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "weapons")
        )

    elif action == "explosive":
        bot.edit_message_text("🧨 قسم المتفجرات:", call.message.chat.id, call.message.message_id, reply_markup=explosive_menu(uid))

    elif action == "explosive_arrow":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🏹 Explosive Arrows Pamphlet\n\n"
            "المتطلبات:\n"
            "لفل 93\n"
            "سهم + ديناميت + ريش\n\n"
            "طريقة التصنيع:\n"
            "علق على مثلث وأختر :\n"
            "Craft > Ammo > Arrows - Dynamite",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "explosive")
        )

    elif action == "explosive_ammo":
        bot.edit_message_text(
            "اسم الوصفة🗞️\n"
            "💣 Explosive Ammo Pamphlet\n\n"
            "المتطلبات:\n"
            "• لفل 90\n"
            "• رصاص حسب نوع السلاح\n"
            "• دهن\n\n"
            "طريقة التصنيع:\n"
            "علق على مثلث وأختر:\n"
            "Craft > Ammo > واختر نوع السلاح\n"
            "هذا المتفجر",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "explosive")
        )

    elif action == "volatile_dynamite":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🧨 Volatile Dynamite Pamphlet\n\n"
            "المتطلبات:\n"
            "ديناميت + دهن + High Velocity Ammo\n\n"
            "المميزات:\n"
            "انفجار أقوى من العادي\n\n"
            "طريقة التصنيع:\n"
            "علق على مثلث وأختر :\n"
            "Craft > Weapons > Dynamite- volatile",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "explosive")
        )

    elif action == "ammo_pouch":
        bot.edit_message_text("📦 قسم زيادة مخزون الأسلحة:", call.message.chat.id, call.message.message_id, reply_markup=ammo_pouch_menu(uid))

    elif action == "rifle_pouch":
        bot.edit_message_text(
            "اسم الوصفة 🗞️ :\n"
            "RIFLE AMMO POUCH PAMPHLET\n\n"
            "فائدتها :\n"
            "تزيد من سعة الرصاص العادي لـ RIFLE\n\n"
            "💡ملاحظة :\n"
            "📝 يجب قراءة الوصفه بعد شرائها من الـ FENCE",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "ammo_pouch")
        )

    elif action == "repeater_pouch":
        bot.edit_message_text(
            "اسم الوصفة 🗞️ :\n"
            "REPEATER AMMO POUCH PAMPHLET\n\n"
            "فائدتها :\n"
            "تزيد من سعة الرصاص العادي لـ REPEATER\n\n"
            "💡ملاحظة :\n"
            "📝 يجب قراءة الوصفه بعد شرائها من الـ FENCE",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "ammo_pouch")
        )

    elif action == "pistol_pouch":
        bot.edit_message_text(
            "اسم الوصفة 🗞️ :\n"
            "PISTOL AMMO POUCH PAMPHLET\n\n"
            "فائدتها :\n"
            "تزيد من سعة الرصاص العادي لـ PISTOL\n\n"
            "💡ملاحظة :\n"
            "📝 يجب قراءة الوصفه بعد شرائها من الـ FENCE",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "ammo_pouch")
        )

    elif action == "varmint_pouch":
        bot.edit_message_text(
            "اسم الوصفة 🗞️:\n"
            "VARMINT AMMO POUCH PAMPHLET\n\n"
            "فائدتها :\n"
            "تزيد من سعة الرصاص العادي لـ VARMINT\n\n"
            "💡ملاحظة :\n"
            "📝 يجب قراءة الوصفه بعد شرائها من الـ FENCE",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "ammo_pouch")
        )

    elif action == "arrow_pouch":
        bot.edit_message_text(
            "اسم الوصفة 🗞️ :\n"
            "ARROW POUCH PAMPHLET\n\n"
            "فائدتها :\n"
            "تزيد من سعة الأسهم العادي لـ ARROW\n\n"
            "💡ملاحظة :\n"
            "📝 يجب قراءة الوصفه بعد شرائها من الـ FENCE",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "ammo_pouch")
        )

    elif action == "shotgun_pouch":
        bot.edit_message_text(
            "اسم الوصفة 🗞️ :\n"
            "SHOTGUN AMMO POUCH PAMPHLET\n\n"
            "فائدتها :\n"
            "تزيد من سعة الرصاص العادي لـ SHOTGUN\n\n"
            "💡ملاحظة :\n"
            "📝 يجب قراءة الوصفه بعد شرائها من الـ FENCE",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "ammo_pouch")
        )

    elif action == "revolver_pouch":
        bot.edit_message_text(
            "اسم الوصفة 🗞️ :\n"
            "REVOLVER AMMO POUCH PAMPHLET\n\n"
            "فائدتها :\n"
            "تزيد من سعة الرصاص العادي لـ REVOLVER\n\n"
            "💡ملاحظة :\n"
            "📝 يجب قراءة الوصفه بعد شرائها من الـ FENCE",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "ammo_pouch")
        )

    elif action == "ammo_tips":
        bot.edit_message_text(
            "💡نصائح لزيادة سعة الرصاص :\n\n"
            "* أشتر الوصفه من الـ FENCE\n\n"
            "* افتح الحقيبة :\n"
            "1. SATCHEL ⇢ DOCUMENTS ⇢ PAMPHLETS ⇣\n"
            "2. اختار الوصفه و اقرائها لـ تفعيل الوصفه\n\n"
            "* لتعبئة الرصاص توجد طريقتان :\n"
            "1. GUNSMITH من محل الاسلحة\n"
            "2. من الكتاب و يتم إستلام من البريد او المخيم\n\n"
            "📌ملاحظة :\n"
            "زيادة سعة الرصاص فقط لـ ( REGULAR ) او سهم العادي .",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "ammo_pouch")
        )

    elif action == "horse":
        bot.edit_message_text("🐎 قسم الأحصنة:", call.message.chat.id, call.message.message_id, reply_markup=horse_menu(uid))

    elif action == "horse_ointment":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🧴 Horse Ointment Pamphlet\n\n"
            "المتطلبات\n"
            "Sage <Hummingbird & Desert>\n"
            "Common Bulrush\n"
            "Yarrow\n\n"
            "المميزات:\n"
            "Health Core + Gold Stamina Core",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "horse")
        )

    elif action == "horse_meal":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "🍽️ Horse Meal Pamphlet\n\n"
            "المتطلبات:\n"
            "Currant <Black & Golden> x3\n"
            "Beer x3\n"
            "Hay x3\n\n"
            "المميزات:\n"
            "يجدد Health + Stamina",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "horse")
        )

    elif action == "horse_medicine":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "💊 Special Horse Medicine Pamphlet\n\n"
            "المتطلبات:\n"
            "Ginseng x2\n"
            "Common Bulrush x2\n"
            "Wild Carrot x2\n\n"
            "المميزات:\n"
            "يعيد صحة الحصان كامله",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "horse")
        )

    elif action == "horse_stimulant":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "⚡ Special Horse Stimulant Pamphlet\n\n"
            "المتطلبات:\n"
            "Sage x2\n"
            "Common Bulrush x2\n"
            "Wild Carrot x2\n\n"
            "المميزات:\n"
            "يجدد Health + Stamina",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "horse")
        )

    elif action == "horse_reviver":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "❤️‍🩹 Special Horse Reviver Pamphlet\n\n"
            "المتطلبات:\n"
            "Ginseng x2\n"
            "Wild Carrot x2\n"
            "Parasol Mushroom x2\n\n"
            "المميزات:\n"
            "يعيد الحصان إلى الحياة",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "horse")
        )

    elif action == "horse_tips":
        bot.edit_message_text(
            "📘 نصائح مهمة للعناية بالأحصنة :\n\n"
            "⤶ يجب قراءة الوصفة بعد شرائها من Fence لتفعيلها.\n\n"
            "⤶ لا يمكن الصنع إلا عند نار المخيم أو Wilderness Camp.\n\n"
            "⤶ النباتات تُجمع من البرية أو تُشترى من مدام نزار.\n\n"
            "⤶ دواء الخيول يعالج كل الأمراض والسموم فورًا.\n\n"
            "⤶ منقذ الخيول يعيد حصانك مباشرة إذا سقط.",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "horse")
        )

    elif action == "health":
        bot.edit_message_text("⚕️ تونيكات الصحة:", call.message.chat.id, call.message.message_id, reply_markup=health_menu(uid))

    elif action == "health_cure":
        bot.edit_message_text(
            "تونيك ||| للصحة ❤️\n\n"
            "اسم الوصفة 🗞️\n"
            "Special Health Cure Pamphlet\n\n"
            "المتطلبات:\n"
            "يارو Yarrow + جنسنغ Ginseng + كشمش ذهبي Golden Currant\n\n"
            "المميزات:\n"
            "يعيد الصحة بالكامل ويحول ال Core إلى ذهبي ليبقى ممتلئًا لفترة طويلة",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "health")
        )

    elif action == "snake_oil":
        bot.edit_message_text(
            "تونيك ||| DEAD eye 👁️\n\n"
            "اسم الوصفة 🗞️\n"
            "Special Snake Oil Pamphlet\n\n"
            "المتطلبات:\n"
            "تبغ هندي + جنسنغ + مريمية أولياندر\n\n"
            "المميزات:\n"
            "يعيد Dead eye core كاملاً ويحوله إلى ذهبي",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "health")
        )

    elif action == "miracle_tonic":
        bot.edit_message_text(
            "تونيك || 💪\n\n"
            "اسم الوصفة 🗞️\n"
            "Special Miracle Tonic Pamphlet\n\n"
            "المتطلبات :\n"
            "جنسنغ + Sage + جزر بري\n\n"
            "المميزات:\n"
            "يعيد الصحة والطاقة و Dead eye بشكل كامل ويحولهم إلى Gold Core",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "health")
        )

    elif action == "bitters":
        bot.edit_message_text(
            "تونيك ||| للطاقة ⚡️\n\n"
            "اسم الوصفة 🗞️\n"
            "Special Bitters Pamphlet\n\n"
            "المتطلبات:\n"
            "Sage + Currant + جنسنغ\n\n"
            "المميزات:\n"
            "يقوي الطاقة ويحولها إلى Gold core",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "health")
        )

    elif action == "cooking":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "Efficient Cooking Pamphlet\n\n"
            "طريقة الحصول على الوصفة :\n"
            "شرائها من فنس بعد لفل 20\n\n"
            "المميزات :\n"
            "يجعل عملية الطبخ سريعة ومضاعفة بدلاً من طبخ كل قطعة لحم لوحدها\n\n"
            "الوصفة تختصر الوقت وتسمح بطبخ كميات أكبر في وقت واحد",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "main")
        )

    elif action == "travel":
        bot.edit_message_text(
            "اسم الوصفة 🗞️\n"
            "Wilderness Camp Pamphlet\n\n"
            "للحصول على الوصفة :\n"
            "لفل 5 في وظيفة الطبيعة\n"
            "بعد وصولك للفل 5 في الوظيفة تشتريه من هاريت مقابل 750$\n"
            "بعد شراء المخيم توجه لفنس واشتري الوصفة وضروري تقرأها لتفعيلها\n\n"
            "المميزات:\n"
            "تفتح مخيم متنقل صغير\n"
            "(Wilderness camp ⛺️)\n"
            "في أي مكان بالخريطة\n"
            "يمكن التنقل السريع إلى أي مكان بدون فاست ترافل أساسي\n"
            "يحتوي على نار للطبخ والتصنيع (ذخيرة، لحم، إلخ)",
            call.message.chat.id, call.message.message_id,
            reply_markup=back(uid, "main")
        )

    elif action == "close":
        bot.delete_message(call.message.chat.id, call.message.message_id)

print("✅ Fence Bot is running…")
bot.infinity_polling()
