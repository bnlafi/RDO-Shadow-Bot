import telebot
import time
import threading
from datetime import datetime, timedelta

# التوكن اللي أرسلته
TOKEN = "8633631488:AAHlXHtNeJ2SrgZMhPGAbGn78KuTxKSA4EA"

bot = telebot.TeleBot(TOKEN)

users_data = {}  # {user_id: {sale_number: start_time}}
last_use = {}    # {user_id: datetime} - كل مستخدم له وقت استخدام خاص به
cooldown_warning_sent = {}  # {user_id: bool} - كل مستخدم له حالة تحذير خاصة به

COOLDOWN_SECONDS = 120  # 2 دقيقة لكل مستخدم بشكل منفصل

# رسالة التحذير
COOLDOWN_WARNING = "⏳ الرجاء الانتظار... تقدر تستخدم البوت مرة كل دقيقتين فقط"

# الرسالة الترحيبية
WELCOME_MESSAGE = """
مرحباً انا كريبس الخاص بوظيفة التاجر 👨‍🌾

بوت خاص في قروب [𝐑𝐞𝐝 𝐃𝐞𝐚𝐝 ⚔︎ 𝐒𝐡𝐚𝐝𝐨𝐰](https://t.me/Reddead2bndx1)


مهمتي أعلمك بيعتك كم باقي لها وتجهز⏳

كل اللي عليك تكتب " بيعة والرقم اللي وصلت له " أو " بيعه والرقم "

أفضل الجلود الأسطورية لتجهيز بيعة التاجر وتعبئة الشريط الأبيض بسرعه ⬇️
1- Legendary Ghost Panther Pelt 🐆
2- Legendary Ridgback Spirit Bear Pelt 🐻
[لمعرفة مواقع الحيوانات أضغط هنا](https://jeanropke.github.io/RDOMap/)

⚒️ للحصول على ادوات التاجر بشكل أسهل وأسرع

أتجه الى طاولة التاجر واضغط مثلث ، وبعدها علق على المربع ، بعدها اضغط ستارت
 Online - Camp
وبكذا الادوات تكون وصلت 🤩
"""

CONGRATS_MESSAGE = "مبروك 🥳 بيعتك جاهزه ! دور لك مدبل 👀"

def get_remaining_time(sale_number, start_time, now=None):
    if now is None:
        now = datetime.now()
    
    base_minutes = 200
    deduction = sale_number * 2
    total_minutes = max(0, base_minutes - deduction)

    end_time = start_time + timedelta(minutes=total_minutes)
    remaining = end_time - now

    if remaining.total_seconds() <= 0:
        return "البيعة خلّصت!"

    hours = int(remaining.total_seconds() // 3600)
    minutes = int((remaining.total_seconds() % 3600) // 60)
    return f"{hours} ساعات و {minutes} دقيقه"

def send_sale_message(chat_id, sale_number, start_time, message_id):
    remaining = get_remaining_time(sale_number, start_time, now=start_time)
    message = f"⏰عشان تجهز بيعتك باقي لها {remaining}\n\n" \
              f"أهم شيء لاتطفي اللعبه عشان مايوقف شغل ولا تدخل بيعة أحد اذا ماتبي بيعتك تتصفر ❗️\n" \
              f"ولاتنسى تجيب لكريبس ال SUPPLIES كل 50 دقيقه"
    bot.send_message(chat_id, message, reply_to_message_id=message_id, parse_mode='Markdown', protect_content=True)

@bot.message_handler(commands=['start'])
def start(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, WELCOME_MESSAGE, parse_mode='Markdown', disable_web_page_preview=True, protect_content=True)


@bot.message_handler(regexp=r'(?i)كريبس')
def handle_kreeps(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, WELCOME_MESSAGE, parse_mode='Markdown', disable_web_page_preview=True, protect_content=True)


@bot.message_handler(regexp=r'^[بي][ي]ع[ةه]\s*\d+$')
def handle_sale(message):
    chat_id = message.chat.id
    message_id = message.message_id
    text = message.text.strip()
    
    # الحصول على user_id الفعلي للمستخدم
    user_id = message.from_user.id
    
    print(f"📩 User {user_id} in chat {chat_id} sent: {text}")  # Debug message
    
    now = datetime.now()
    
    # التحقق من cooldown للمستخدم الفعلي (user_id) وليس المجموعة
    if user_id in last_use:
        time_since_last = (now - last_use[user_id]).total_seconds()
        print(f"⏰ User {user_id} last used: {time_since_last} seconds ago")  # Debug
        
        if time_since_last < COOLDOWN_SECONDS:
            remaining_time = int(COOLDOWN_SECONDS - time_since_last)
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            
            # إرسال تحذير مرة واحدة فقط لهذا المستخدم
            if user_id not in cooldown_warning_sent or not cooldown_warning_sent[user_id]:
                warning_msg = f"⏳ الرجاء الانتظار {minutes} دقيقة و {seconds} ثانية قبل استخدام البوت مرة أخرى"
                bot.reply_to(message, warning_msg, protect_content=True)
                cooldown_warning_sent[user_id] = True
                print(f"⚠️ Sent cooldown warning to user {user_id}")  # Debug
            else:
                print(f"⚠️ User {user_id} already has active cooldown warning")  # Debug
            return  # تجاهل الرسالة لهذا المستخدم فقط
    
    # إذا وصلنا هنا، المستخدم ليس في cooldown
    print(f"✅ User {user_id} can use bot (no cooldown)")  # Debug
    
    # إعادة تعيين حالة التحذير لهذا المستخدم
    cooldown_warning_sent[user_id] = False

    try:
        parts = text.split()
        sale_number = int(parts[1])
        if not 1 <= sale_number <= 100:
            print(f"❌ User {user_id} sent invalid sale number: {sale_number}")  # Debug
            return  # تجاهل لو فوق 100
    except:
        bot.reply_to(message, "اكتب: بيعة [رقم] أو بيعه [رقم] مثلاً: بيعة 1", protect_content=True)
        return

    # لو 100 → مبروك
    if sale_number == 100:
        bot.reply_to(message, CONGRATS_MESSAGE, protect_content=True)
        # تحديث وقت آخر استخدام لهذا المستخدم فقط
        last_use[user_id] = now
        print(f"🎉 User {user_id} completed sale 100, cooldown started")  # Debug
        return

    # تسجيل البيعة
    start_time = datetime.now()
    if user_id not in users_data:
        users_data[user_id] = {}
    users_data[user_id][sale_number] = start_time

    # تحديث وقت آخر استخدام لهذا المستخدم فقط
    last_use[user_id] = now
    print(f"📝 User {user_id} started sale {sale_number}, cooldown started")  # Debug

    send_sale_message(chat_id, sale_number, start_time, message_id)

    # تذكير بعد 50 دقيقة
    threading.Thread(target=remind_supplies, args=(chat_id, user_id, sale_number, start_time, message_id)).start()

def remind_supplies(chat_id, user_id, sale_number, start_time, original_message_id):
    time.sleep(50 * 60)  # 50 دقيقة
    if user_id not in users_data or sale_number not in users_data[user_id]:
        return

    remaining = get_remaining_time(sale_number, start_time)
    if "خلّصت" in remaining:
        return

    message = f"⚠️ تذكير مهم للبيعة {sale_number}!\n\n" \
              f"⏰عشان تجهز بيعتك باقي لها {remaining}\n\n" \
              f"أهم شيء لاتطفي اللعبه عشان مايوقف شغل ولا تدخل بيعة أحد اذا ماتبي بيعتك تتصفر ❗️\n" \
              f"ولاتنسى تجيب لكريبس ال SUPPLIES الحين!"
    bot.send_message(chat_id, message, reply_to_message_id=original_message_id, parse_mode='Markdown', protect_content=True)

@bot.message_handler(commands=['status'])
def status(message):
    user_id = message.from_user.id
    
    if user_id not in users_data or not users_data[user_id]:
        bot.reply_to(message, "ما عندك بيعات مسجلة بعد!", protect_content=True)
        return

    msg = "وضع البيعات الحالي:\n"
    for sale_num, start_time in sorted(users_data[user_id].items()):
        remaining = get_remaining_time(sale_num, start_time)
        msg += f"بيعة {sale_num}: {remaining}\n"
    bot.reply_to(message, msg, protect_content=True)

print("البوت شغال...")
bot.polling(none_stop=True)
