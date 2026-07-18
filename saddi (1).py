import telebot
import json
import os
import re
from datetime import datetime

BOT_TOKEN = "8947226059:AAEcyUj9kD0etinP6AJxiDngKDcEWTwHxZk"
bot = telebot.TeleBot(BOT_TOKEN)
DB_FILE = "queue_database.json"

class Database:
    def __init__(self):
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(DB_FILE):
            with open(DB_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {
            "current_queue": None,
            "queues_history": []
        }

    def save_data(self):
        with open(DB_FILE, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def create_queue(self, creator_name, creator_id, pinned_message_id, chat_id):
        queue = {
            "creator": creator_name,
            "creator_id": creator_id,
            "message_id": pinned_message_id,
            "chat_id": chat_id,
            "members": [],
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "status": "active"
        }
        self.data["current_queue"] = queue
        self.save_data()
        return queue

    def get_current_queue(self):
        return self.data.get("current_queue")

    def add_member(self, user_id, username, display_name, sony_id, join_message_id):
        queue = self.data["current_queue"]
        if not queue or queue["status"] != "active":
            return False, "لا يوجد طابور نشط حالياً", None, None

        if not (3 <= len(sony_id) <= 16):
            return False, "⚠️ الـ ID الذي أدخلته غير صالح..", None, None

        if not re.match(r"^[A-Za-z0-9_-]+$", sony_id):
            return False, "⚠️ الـ ID الذي أدخلته غير صالح..", None, None

        for member in queue["members"]:
            if member["user_id"] == user_id:
                return False, f"أنت مسجل بالفعل! رقمك هو {member['position']}.", None, None

        # تحديد الرقم الدائم للعضو
        position = len(queue["members"]) + 1

        member = {
            "user_id": user_id,
            "username": username,
            "display_name": display_name,
            "sony_id": sony_id,
            "status": "waiting",
            "join_message_id": join_message_id,
            "position": position  # الرقم الثابت
        }
        queue["members"].append(member)
        self.save_data()

        mention_name = username if username else display_name
        return True, position, mention_name, display_name

    def call_member_by_number(self, number):
        queue = self.data["current_queue"]
        if not queue or queue["status"] != "active":
            return None

        # البحث عن العضو برقمه الأصلي الثابت
        for member in queue["members"]:
            if member.get("position") == number and member["status"] == "waiting":
                member["status"] = "called"
                self.save_data()
                return member

        return None

    def return_member_by_number(self, number):
        queue = self.data["current_queue"]
        if not queue or queue["status"] != "active":
            return None

        # البحث عن العضو برقمه الأصلي الثابت
        for member in queue["members"]:
            if member.get("position") == number and member["status"] == "called":
                member["status"] = "waiting"
                self.save_data()
                return member

        return None

    def stop_queue(self):
        queue = self.data["current_queue"]
        if queue and queue["status"] == "active":
            queue["status"] = "stopped"
            self.data["queues_history"].append(queue.copy())
            self.data["current_queue"] = None
            self.save_data()
            return True
        return False

    def get_queue_status(self):
        queue = self.data["current_queue"]
        if not queue or queue["status"] != "active":
            return None

        all_members = queue["members"]
        waiting = [m for m in all_members if m["status"] == "waiting"]
        called = [m for m in all_members if m["status"] == "called"]

        creator_mention = f"<a href='tg://user?id={queue['creator_id']}'>{queue['creator']}</a>"

        status_text = f"انشاء: {creator_mention}\n"
        status_text += f"👤 إجمالي الأعضاء: {len(all_members)}\n"
        status_text += f"🗣️ تم استدعاء: {len(called)}\n"
        status_text += f"في الإنتظار: {len(waiting)}\n\n"

        if not waiting:
            return status_text

        # عرض الأعضاء بأرقامهم الأصلية الثابتة
        for member in waiting:
            user_mention = f"<a href='tg://user?id={member['user_id']}'>{member['display_name']}</a>"
            status_text += f"⏳ {member['position']}. {user_mention}\n"

        return status_text

db = Database()

def is_admin(chat_id, user_id):
    try:
        member = bot.get_chat_member(chat_id, user_id)
        return member.status in ['creator', 'administrator']
    except:
        return False

@bot.message_handler(func=lambda m: m.text == "طابور" and m.reply_to_message and m.chat.type in ['group', 'supergroup'])
def create_queue_from_reply(message):
    if not is_admin(message.chat.id, message.from_user.id):
        return

    current = db.get_current_queue()
    if current and current["status"] == "active":
        bot.reply_to(message, "يوجد طابور نشط بالفعل. اكتب «وقف الطابور» أولاً.", protect_content=True)
        return

    target_msg = message.reply_to_message

    bot.reply_to(target_msg,
        "✅ تم بدء طابور جديد بنجاح.\n(اكتب ID السوني الخاص بك على الاعلان🎮).",
        disable_notification=True, protect_content=True)

    db.create_queue(message.from_user.first_name, message.from_user.id, target_msg.message_id, message.chat.id)

@bot.message_handler(func=lambda m: m.text in ["حالة", "حاله"] and m.chat.type in ['group', 'supergroup'])
def status_command(message):
    if not is_admin(message.chat.id, message.from_user.id):
        return

    status = db.get_queue_status()
    if status:
        bot.reply_to(message, status, parse_mode='HTML', disable_web_page_preview=True, protect_content=True)
    else:
        bot.reply_to(message, "لا يوجد طابور نشط أو انتهى الطابور.", protect_content=True)

@bot.message_handler(func=lambda m: m.text == "وقف الطابور" and m.chat.type in ['group', 'supergroup'])
def stop_queue_command(message):
    if not is_admin(message.chat.id, message.from_user.id):
        return

    if db.stop_queue():
        bot.reply_to(message, "✅ تم إيقاف الطابور بنجاح.", protect_content=True)
    else:
        bot.reply_to(message, "لا يوجد طابور نشط.", protect_content=True)

@bot.message_handler(func=lambda m: m.reply_to_message and m.chat.type in ['group', 'supergroup'])
def handle_registration(message):
    queue = db.get_current_queue()
    if not queue or queue["status"] != "active":
        return

    if message.reply_to_message.message_id != queue["message_id"]:
        return

    sony_id = message.text.strip()
    if not sony_id:
        return

    user_id = message.from_user.id
    username = message.from_user.username or ""
    display_name = message.from_user.first_name
    join_message_id = message.message_id

    success, val1, val2, val3 = db.add_member(user_id, username, display_name, sony_id, join_message_id)

    if success:
        mention = f"@{val2}" if username else val3
        bot.reply_to(message, f"🥳 تم تسجيلك بنجاح يا {mention}!\nرقمك في الطابور هو: {val1}", protect_content=True)
    else:
        bot.reply_to(message, val1, protect_content=True)

@bot.message_handler(func=lambda m: m.text.isdigit() and m.chat.type in ['group', 'supergroup'])
def call_by_number(message):
    if not is_admin(message.chat.id, message.from_user.id):
        return

    queue = db.get_current_queue()
    if not queue or queue["status"] != "active":
        return

    number = int(message.text)
    member = db.call_member_by_number(number)

    if not member:
        bot.reply_to(message, f"العضو رقم {number} غير موجود في الانتظار أو تم استدعاؤه مسبقاً.", protect_content=True)
        return

    username = member['username']
    display_name = member['display_name']
    mention = f"@{username}" if username else display_name

    # 1. الرد على رسالة العضو الأصلية (اللي فيها PSN ID)
    if "join_message_id" in member and member["join_message_id"]:
        try:
            bot.send_message(
                message.chat.id,
                f"{mention} وصل دورك اقبل وجون 🥳",
                reply_to_message_id=member["join_message_id"],
                protect_content=True
            )
        except Exception as e:
            print(f"خطأ في الرد على رسالة الانضمام: {e}")
            # إذا فشل الرد على رسالة العضو (مثل حذف الرسالة)، رد على رسالة الأدمن
            bot.reply_to(message, f"{mention} وصل دورك اقبل وجون 🥳\n⚠️ (تم حذف رسالة التسجيل الأصلية)", protect_content=True)
    else:
        # إذا لم يكن هناك join_message_id، رد على رسالة الأدمن
        bot.reply_to(message, f"{mention} وصل دورك اقبل وجون 🥳", protect_content=True)

    # 2. رسالة خاصة للعضو
    try:
        bot.send_message(member['user_id'], "🥳 وصل دورك اقبل وجون!\nتعال بسرعة 🚀", protect_content=True)
    except:
        pass

@bot.message_handler(func=lambda m: m.text.startswith("اعاده ") and m.chat.type in ['group', 'supergroup'])
def return_member(message):
    if not is_admin(message.chat.id, message.from_user.id):
        return

    queue = db.get_current_queue()
    if not queue or queue["status"] != "active":
        bot.reply_to(message, "لا يوجد طابور نشط.", protect_content=True)
        return

    try:
        number = int(message.text.split()[1])
    except:
        return

    member = db.return_member_by_number(number)

    if not member:
        bot.reply_to(message, f"لا يوجد عضو مستدعى برقم إعادة {number}.", protect_content=True)
        return

    username = member['username']
    display_name = member['display_name']
    mention = f"@{username}" if username else display_name

    bot.reply_to(message, f"✅ تم إرجاع {mention} إلى قائمة الانتظار بنجاح.", protect_content=True)

@bot.message_handler(commands=['start', 'مساعده', 'مساعدة'])
def help_command(message):
    help_text = """
أهلاً بك في بوت الطابور 🥳
أوامر المشرفين:
طابور - (بالرد على رسالة) لبدء طابور جديد.
وقف الطابور - لإيقاف الطابور الحالي.
حالة / حاله - لعرض حالة الطابور.
[رقم] - لاستدعاء عضو (فقط أرسل رقمه).
اعاده [الرقم] - لإرجاع عضو إلى قائمة الانتظار.
مساعده - لعرض هذه الرسالة.

للأعضاء:
للانضمام، قم بالرد مباشرة على رسالة الإعلان واكتب ID البلايستيشن الخاص بك.
    """
    bot.send_message(message.chat.id, help_text, protect_content=True)

if __name__ == '__main__':
    print("البوت يعمل الآن...")
    bot.infinity_polling()
