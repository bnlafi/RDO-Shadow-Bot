import telebot
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

# Replace with your actual bot token
BOT_TOKEN = "8865192188:AAG7ruXpQvcnxNw_yjQ8up03YHzpKHQMkV0"
bot = telebot.TeleBot(BOT_TOKEN)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Dictionary of 28 Free Roam Legendary Animals
LEGENDARY_ANIMALS = {
    "moon_beaver": {"name_ar": "🦫 قندس القمر الأسطوري", "name_en": "Legendary Moon Beaver", "time": "6:00 AM – 9:00 AM & 6:00 PM – 9:00 PM (ممطر)", "weakness": "بندقية فرمن (Varmint)", "triggers": ["moon", "moon beaver", "قمر", "قندس القمر", "القمر", "القمر الاسطوري", "قندس القمر الاسطوري"], "location_ar": "جنوب حوض إليسيان (Elysian Pool)", "local_path": "online_animals/moon_beaver.jpg"},
    "zizi_beaver": {"name_ar": "🦫 قندس زيزي الأسطوري", "name_en": "Legendary Zizi Beaver", "time": "6:00 AM – 9:00 AM & 6:00 PM – 9:00 PM (أي طقس)", "weakness": "بندقية فرمن (Varmint)", "triggers": ["zizi", "zizi beaver", "زيزي", "قندس زيزي", "قندس زيزي الاسطوري"], "location_ar": "بحيرة أوانجيلا (Owanjila)", "local_path": "online_animals/zizi_beaver.jpg"},
    "wakpa_boar": {"name_ar": "🐗 خنزير واكبا الأسطوري", "name_en": "Legendary Wakpa Boar", "time": "9:00 AM – 6:00 PM (ممطر)", "weakness": "بندقية عادية (Rifle)", "triggers": ["wakpa", "wakpa boar", "واكبا", "خنزير واكبا"], "location_ar": "ستيلووتر كريك (Stillwater Creek)", "local_path": "online_animals/wakpa_boar.jpg"},
    "cogi_boar": {"name_ar": "🐗 خنزير كوجي الأسطوري", "name_en": "Legendary Cogi Boar", "time": "6:00 AM – 9:00 AM (صافٍ)", "weakness": "بندقية عادية (Rifle)", "triggers": ["cogi", "cogi boar", "كوجي", "خنزير كوجي"], "location_ar": "شمال غرب مستنقع بلووتر مارش (Bluewater Marsh)", "local_path": "online_animals/cogi_boar.jpg"},
    "winyan_bison": {"name_ar": "🐂 بيسون وينيان الأسطوري", "name_en": "Legendary Winyan Bison", "time": "9:00 PM – 6:00 AM (صافٍ)", "weakness": "بندقية قنص (Sniper)", "triggers": ["winyan", "winyan bison", "وينيان", "بيسون وينيان"], "location_ar": "بحيرة إيزابيلا (Lake Isabella)", "local_path": "online_animals/winyan_bison.jpg"},
    "tatanka_bison": {"name_ar": "🐂 بيسون تاتانكا الأسطوري", "name_en": "Legendary Tatanka Bison", "time": "9:00 AM – 6:00 PM (ممطر)", "weakness": "بندقية قنص (Sniper)", "triggers": ["tatanka", "tatanka bison", "تاتانكا", "بيسون تاتانكا"], "location_ar": "حقول النفط في هارتلاند (Heartland Oil Fields)", "local_path": "online_animals/tatanka_bison.jpg"},
    "midnight_paw_coyote": {"name_ar": "🐺 كويوت مخلب منتصف الليل الأسطوري", "name_en": "Legendary Midnight Paw Coyote", "time": "6:00 AM – 9:00 PM (صافٍ)", "weakness": "بندقية تكرار (Repeater)", "triggers": ["midnight", "midnight paw", "midnight paw coyote", "منتصف الليل", "مخلب منتصف الليل", "كويوت منتصف الليل", "كويوت مخلب منتصف الليل"], "location_ar": "قرب ستروبري - مونتوس ريست (Monto's Rest)", "local_path": "online_animals/midnight_paw_coyote.jpg"},
    "red_streak_coyote": {"name_ar": "🐺 كويوت الخط الأحمر الأسطوري", "name_en": "Legendary Red Streak Coyote", "time": "9:00 AM – 9:00 PM (أي طقس)", "weakness": "بندقية تكرار (Repeater)", "triggers": ["red streak", "red streak coyote", "الخط الأحمر", "الخط الاحمر", "كويوت الخط الأحمر", "streak"], "location_ar": "بايكس باسين (Pike's Basin) - نيو أوستين", "local_path": "online_animals/red_streak_coyote.jpg"},
    "maza_cougar": {"name_ar": "🐆 كوجر مازا الأسطوري", "name_en": "Legendary Maza Cougar", "time": "6:00 AM – 9:00 AM (صافٍ)", "weakness": "بندقية قنص / متفجرات", "triggers": ["maza", "maza cougar", "مازا", "كوجر مازا"], "location_ar": "بالقرب من بحر كورونادو (Sea of Coronado) - نيو أوستين", "local_path": "online_animals/maza_cougar.jpg"},
    "iguga_cougar": {"name_ar": "🐆 كوجر إيغوغا الأسطوري", "name_en": "Legendary Iguga Cougar", "time": "6:00 PM – 9:00 PM (عاصف)", "weakness": "بندقية قنص / متفجرات", "triggers": ["iguga", "iguga cougar", "إيغوغا", "ايغوغا", "كوجر إيغوغا", "كوجر ايغوغا"], "location_ar": "غريت بلينز (Great Plains) - ويست إليزابيث", "local_path": "online_animals/iguga_cougar.jpg"},
    "ozula_elk": {"name_ar": "🦌 أيل أوزولا الأسطوري", "name_en": "Legendary Ozula Elk", "time": "6:00 PM – 4:00 AM (ضبابي)", "weakness": "بندقية قنص (Sniper)", "triggers": ["ozula", "ozula elk", "أوزولا", "اوزولا", "أيل أوزولا", "ايل اوزولا"], "location_ar": "تشولا سبرينغز (Cholla Springs) - نيو أوستين", "local_path": "online_animals/ozula_elk.jpg"},
    "katata_elk": {"name_ar": "🦌 أيل كاتاتا الأسطوري", "name_en": "Legendary Katata Elk", "time": "6:00 AM – 6:00 PM (ضبابي)", "weakness": "بندقية قنص (Sniper)", "triggers": ["katata", "katata elk", "كاتاتا", "أيل كاتاتا", "ايل كاتاتا"], "location_ar": "جنوب غرب كمبرلاند فورست (Cumberland Forest)", "local_path": "online_animals/katata_elk.jpg"},
    "teca_gator": {"name_ar": "🐊 تمساح تيكا الأسطوري", "name_en": "Legendary Teca Gator", "time": "9:00 PM – 6:00 AM (عاصف)", "weakness": "بندقية قنص / متفجرات", "triggers": ["teca", "teca gator", "تيكا", "تمساح تيكا"], "location_ar": "الأرخبيل والمستنقعات جنوب سانت دينيس", "local_path": "online_animals/teca_gator.jpg"},
    "sun_gator": {"name_ar": "🐊 تمساح الشمس الأسطوري", "name_en": "Legendary Sun Gator", "time": "6:00 AM – 9:00 AM (ضبابي)", "weakness": "بندقية قنص / متفجرات", "triggers": ["sun", "sun gator", "الشمس", "شمس", "تمساح الشمس"], "location_ar": "شمال سانت دينيس في مستنقع لاغراس (Lagras)", "local_path": "online_animals/sun_gator.jpg"},
    "onyx_wolf": {"name_ar": "🐺 الذئب العقيقي الأسطوري", "name_en": "Legendary Onyx Wolf", "time": "9:00 PM – 6:00 AM (صافٍ)", "weakness": "بندقية قنص / متفجرات", "triggers": ["onyx", "onyx wolf", "عقيقي", "العقيقي", "ذئب العقيقي", "الذئب العقيقي"], "location_ar": "قرب ينابيع كوتورا (Cotorra Springs) وشمال الخريطة", "local_path": "online_animals/onyx_wolf.jpg"},
    "emerald_wolf": {"name_ar": "🐺 ذئب الزمرد الأسطوري", "name_en": "Legendary Emerald Wolf", "time": "6:00 PM – 6:00 AM (أي طقس)", "weakness": "بندقية قنص / متفجرات", "triggers": ["emerald", "emerald wolf", "زمرد", "الزمرد", "ذئب الزمرد", "ذئب زمرد"], "location_ar": "غرب أوكريغز رن (O'Creagh's Run)", "local_path": "online_animals/emerald_wolf.jpg"},
    "ota_fox": {"name_ar": "🦊 ثعلب أوتا الأسطوري", "name_en": "Legendary Ota Fox", "time": "6:00 AM – 9:00 AM & 6:00 PM – 9:00 PM (صافٍ)", "weakness": "بندقية تكرار (Repeater)", "triggers": ["ota", "ota fox", "أوتا", "اوتا", "ثعلب أوتا", "ثعلب اوتا"], "location_ar": "جنوب غرب رودس (Rhodes)", "local_path": "online_animals/ota_fox.jpg"},
    "marble_fox": {"name_ar": "🦊 الثعلب الرخامي الأسطوري", "name_en": "Legendary Marble Fox", "time": "6:00 AM – 9:00 AM & 6:00 PM – 9:00 PM (صافٍ)", "weakness": "بندقية تكرار (Repeater)", "triggers": ["marble", "marble fox", "رخامي", "الرخامي", "الثعلب الرخامي", "ثعلب رخامي"], "location_ar": "سبايدر جورج (Spider Gorge) - آمبارينو", "local_path": "online_animals/marble_fox.jpg"},
    "gabbro_horn_ram": {"name_ar": "🐏 كبش قرن الغابرو الأسطوري", "name_en": "Legendary Gabbro Horn Ram", "time": "6:00 AM – 6:00 PM (صافٍ)", "weakness": "بندقية عادية (Rifle)", "triggers": ["gabbro", "gabbro horn", "gabbro horn ram", "غابرو", "الغابرو", "قرن الغابرو", "كبش قرن الغابرو", "كبش الغابرو"], "location_ar": "بحيرة دون خوليو (Lake Don Julio) - نيو أوستين", "local_path": "online_animals/gabbro_horn_ram.jpg"},
    "chalk_horn_ram": {"name_ar": "🐏 كبش قرن الطباشير الأسطوري", "name_en": "Legendary Chalk Horn Ram", "time": "9:00 AM – 6:00 PM (صافٍ)", "weakness": "بندقية عادية (Rifle)", "triggers": ["chalk", "chalk horn", "chalk horn ram", "طباشير", "الطباشير", "قرن الطباشير", "كبش قرن الطباشير", "كبش الطباشير"], "location_ar": "جنوب ينابيع كوتورا (Cotorra Springs)", "local_path": "online_animals/chalk_horn_ram.jpg"},
    "owiza_bear": {"name_ar": "🐻 دب أويزا الأسطوري", "name_en": "Legendary Owiza Bear", "time": "9:00 PM – 6:00 AM (ممطر)", "weakness": "بندقية قنص / متفجرات", "triggers": ["owiza", "owiza bear", "أويزا", "اويزا", "دب أويزا", "دب اويزا"], "location_ar": "على طول نهر داكوتا (Dakota River)", "local_path": "online_animals/owiza_bear.jpg"},
    "ridgeback_spirit_bear": {"name_ar": "🐻 دب روح السلسلة (Ridgeback Spirit) الأسطوري", "name_en": "Legendary Ridgeback Spirit Bear", "time": "9:00 AM – 6:00 PM (صافٍ)", "weakness": "بندقية قنص / متفجرات", "triggers": ["ridgeback", "ridgeback spirit", "ridgeback spirit bear", "سلسلة", "السلسلة", "روح", "الروح", "دب روح", "دب روح السلسلة", "دب الروح"], "location_ar": "نهر ليتل كريك (Little Creek River)", "local_path": "online_animals/ridgeback_spirit_bear.jpg"},
    "snowflake_moose": {"name_ar": "🫎 موظ الثلج الأسطوري", "name_en": "Legendary Snowflake Moose", "time": "9:00 PM – 6:00 AM (ممطر)", "weakness": "بندقية قنص", "triggers": ["snowflake", "snowflake moose", "ثلج", "الثلج", "موظ الثلج", "موظ ثلج"], "location_ar": "بارو لاغون (Barrow Lagoon)", "local_path": "online_animals/snowflake_moose.jpg"},
    "knight_moose": {"name_ar": "🫎 موظ الفارس الأسطوري", "name_en": "Legendary Knight Moose", "time": "9:00 AM – 6:00 PM (أي طقس)", "weakness": "بندقية قنص", "triggers": ["knight", "knight moose", "فارس", "الفارس", "موظ الفارس"], "location_ar": "على طول نهر كماسا (Kamassa River)", "local_path": "online_animals/knight_moose.jpg"},
    "ghost_panther": {"name_ar": "🐆 النمر الشبح (Ghost) الأسطوري", "name_en": "Legendary Ghost Panther", "time": "9:00 PM – 6:00 AM (ممطر)", "weakness": "بندقية قنص", "triggers": ["ghost", "ghost panther", "شبح", "الشبح", "النمر الشبح", "نمر الشبح", "نمر شبح"], "location_ar": "مستنقع بلووتر مارش (Bluewater Marsh) وشمال لاغراس", "local_path": "online_animals/ghost_panther.jpg"},
    "nightwalker_panther": {"name_ar": "🐆 النمر السائر الليلي (Nightwalker) الأسطوري", "name_en": "Legendary Nightwalker Panther", "time": "6:00 PM – 9:00 PM (ضبابي)", "weakness": "بندقية قنص", "triggers": ["nightwalker", "nightwalker panther", "سائر", "السائر", "الليلي", "النمر السائر", "السائر الليلي", "نمر الليل"], "location_ar": "جنوب بولجر غليد (Bolger Glade)", "local_path": "online_animals/nightwalker_panther.jpg"},
    "snow_buck": {"name_ar": "🦌 غزال الثلج الأسطوري", "name_en": "Legendary Snow Buck", "time": "6:00 AM – 9:00 AM (صافٍ)", "weakness": "بندقية عادية / قنص", "triggers": ["snow", "snow buck", "غزال ثلج", "غزال الثلج"], "location_ar": "أورورا باسين (Aurora Basin)", "local_path": "online_animals/snow_buck.jpg"},
    "mud_runner_buck": {"name_ar": "🦌 غزال راكض الطين الأسطوري", "name_en": "Legendary Mud Runner Buck", "time": "9:00 AM – 6:00 PM (صافٍ)", "weakness": "بندقية عادية / قنص", "triggers": ["mud runner", "mud runner buck", "mud", "طين", "الطين", "غزال الطين", "راكض الطين", "غزال راكض الطين"], "location_ar": "جنوب محطة فلاتنيك (Flatneck Station)", "local_path": "online_animals/mud_runner_buck.jpg"}
}

# Dictionary of Plants / Herbs
PLANTS = {
    "plant_1": {"name_ar": "جينسنغ 🌿", "name_en": "Ginseng", "url": "https://www.rdr2.org/wp-content/uploads/2020/02/Alaskan-Ginseng-Location.png"},
    "plant_2": {"name_ar": "يارو 🌼", "name_en": "Yarrow", "url": "https://www.rdr2.org/wp-content/uploads/2020/02/Yarrow-Location.png"},
    "plant_3": {"name_ar": "ميلكويد 🌱", "name_en": "Milkweed", "url": "https://www.rdr2.org/wp-content/uploads/2020/02/Milkweed-Location.png"},
    "plant_4": {"name_ar": "البوص الشائع 🌿", "name_en": "Common Bulrush", "url": "https://www.rdr2.org/wp-content/uploads/2020/02/Common-Bulrush-Location.png"},
    "plant_5": {"name_ar": "نعناع 🌿", "name_en": "Mint", "url": "https://www.rdr2.org/wp-content/uploads/2020/02/Wild-Mint-Location.png"},
    "plant_6": {"name_ar": "زعتر 🌿", "name_en": "Thyme", "url": "https://www.rdr2.org/wp-content/uploads/2020/02/Creeping-Thyme-Location.png"},
    "plant_7": {"name_ar": "اوريجانو 🌿", "name_en": "Oregano", "url": "https://www.rdr2.org/wp-content/uploads/2020/02/Oregano-Location.png"}
}

def send_animal_info(chat_id, animal):
    info_text = (
        f"**{animal['name_en']}**\n\n"
        f"📍 **الموقع:**\n"
        f"┗ {animal.get('location_ar', 'غير محدد')}\n\n"
        f"🕐 **أفضل وقت للصيد:**\n"
        f"┗ {animal['time']}\n\n"
        f"⚔️ **السلاح الموصى به:**\n"
        f"┗ {animal['weakness']}"
    )
    
    try:
        if "local_path" in animal:
            photo_path = os.path.join(BASE_DIR, animal["local_path"])
            with open(photo_path, 'rb') as photo:
                bot.send_photo(chat_id, photo, caption=info_text, parse_mode='Markdown', protect_content=True)
        else:
            bot.send_photo(chat_id, animal['url'], caption=info_text, parse_mode='Markdown', protect_content=True)
    except Exception as e:
        print(f"Failed to send image for animal {animal['name_en']}: {e}")
        bot.send_message(chat_id, info_text + "\n\n*(عذراً، تعذر جلب صورة الموقع حالياً)*", parse_mode='Markdown', protect_content=True)

def send_plant_info(chat_id, plant):
    info_text = (
        f"🌿 **{plant['name_ar']}** ({plant['name_en']})\n\n"
        "📍 إليك مناطق نمو هذه النبتة في الخريطة:"
    )
    
    try:
        bot.send_photo(chat_id, plant['url'], caption=info_text, parse_mode='Markdown', protect_content=True)
    except Exception as e:
        print(f"Failed to send image for plant {plant['name_en']}: {e}")
        bot.send_message(chat_id, info_text + "\n*(عذراً، تعذر جلب صورة الخريطة)*", parse_mode='Markdown', protect_content=True)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    welcome_text = (
        "🐾 **مرحباً بك في بوت Harriet لتعقب الأساطير!** 🐾\n\n"
        "هذا البوت يساعدك في العثور على الحيوانات الأسطورية والنباتات النادرة في Red Dead Online.\n\n"
        "💡 **طريقة الاستخدام:**\n"
        "• ارسل كلمة **(الحيوانات)** للحصول على قائمة بكل الحيوانات الأسطورية.\n"
        "• ارسل كلمة **(النباتات)** لعرض قائمة النباتات والأعشاب.\n"
        "• أو اكتب اسم الحيوان مباشرة (مثلاً: `Ghost` أو `شبح`) للحصول على موقعه.\n\n"
        "⚠️ **ملاحظة:** يمكنك الكتابة باللغة الإنجليزية أو العربية للحصول على الرد بسرعة."
    )
    bot.send_message(message.chat.id, welcome_text, parse_mode='Markdown', protect_content=True)


@bot.message_handler(func=lambda message: message.text == 'الحيوانات')
def handle_animals_command(message):
    welcome_text = "اختر حيواناً من القائمة أدناه لمعرفة موقعه وتفاصيله المتاحة:"
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    buttons = []
    
    for animal_id, details in LEGENDARY_ANIMALS.items():
        btn_text = details["name_en"].replace("Legendary ", "") + " " + details["name_ar"].split(" ")[0]
        button = InlineKeyboardButton(btn_text, callback_data=animal_id)
        buttons.append(button)
        
    markup.add(*buttons)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, protect_content=True)


@bot.message_handler(func=lambda message: message.text == 'النباتات')
def handle_plants_command(message):
    welcome_text = "اختر نبتة من القائمة أدناه لمعرفة مناطق نموها التقريبية:"
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    buttons = []
    
    for plant_id, details in PLANTS.items():
        btn_text = details["name_ar"]
        button = InlineKeyboardButton(btn_text, callback_data=plant_id)
        buttons.append(button)
        
    markup.add(*buttons)
    bot.send_message(message.chat.id, welcome_text, reply_markup=markup, protect_content=True)


# Handler to catch text messages and match them with animal or plant names
@bot.message_handler(func=lambda message: True, content_types=['text'])
def handle_text_interactions(message):
    user_text = message.text.lower().strip()
    if len(user_text) < 2:
        return
        
    ignore_words = {"legendary", "الأسطوري", "الاسطوري", "animal", "plant", "the", "a", "an"}
    
    # Check animals
    for animal_id, details in LEGENDARY_ANIMALS.items():
        # Check explicit triggers first — exact match only
        if "triggers" in details:
            if any(trigger.lower() == user_text for trigger in details["triggers"]):
                send_animal_info(message.chat.id, details)
                return

        # Check in English and Arabic names
        name_en = details["name_en"].lower()
        name_en_clean = " ".join([w for w in name_en.split() if w not in ignore_words])
        
        name_ar = details["name_ar"].split('(')[0].strip().lower() 
        for emoji in ["🐻", "🦊", "🐂", "🐊", "🐺", "🐆", "🦌", "🫎", "🐗", "🦫", "🐏"]:
            name_ar = name_ar.replace(emoji, "").strip()
            
        valid_matches = {name_en, name_en_clean, name_ar}
        
        if user_text in valid_matches:
            send_animal_info(message.chat.id, details)
            return

    # Check plants
    for plant_id, details in PLANTS.items():
        name_en = details["name_en"].lower()
        name_ar = details["name_ar"].replace('🌿', '').replace('🌼', '').replace('🌱', '').strip().lower()
        
        if user_text == name_en or user_text == name_ar:
            send_plant_info(message.chat.id, details)
            return


@bot.callback_query_handler(func=lambda call: True)
def handle_callback_selection(call):
    data_id = call.data
    
    if data_id in LEGENDARY_ANIMALS:
        animal = LEGENDARY_ANIMALS[data_id]
        send_animal_info(call.message.chat.id, animal)
        bot.answer_callback_query(call.id)
        
    elif data_id in PLANTS:
        plant = PLANTS[data_id]
        send_plant_info(call.message.chat.id, plant)
        bot.answer_callback_query(call.id)

if __name__ == "__main__":
    print("Bot is starting...")
    bot.polling(none_stop=True)
