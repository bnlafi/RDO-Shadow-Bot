import telebot
import requests
from io import BytesIO
from datetime import datetime
from collections import defaultdict
import json
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import time
import re

BOT_TOKEN = '8959751783:AAHnX_SxbBYPdCUnn_G8yG2nujRTaVDTUdk'
GROUP_LINK = 'https://t.me/bndx1'
ADMIN_IDS = [1325798367, 7865602280, 0]
bot = telebot.TeleBot(BOT_TOKEN)
bot_info = bot.get_me()
BOT_USERNAME = bot_info.username
last_request_time = defaultdict(float)
chat_warned = defaultdict(bool)
DATA_FILE = 'bot_data.json'
mute_notifications = False
monitoring_enabled = False

# Madam Nazar Cache
NAZAR_DATA = {
    'file_id': None,
    'location': None,
    'last_update': 0
}
# ------------------------------------------------------------
# FIXED API: rdo.gg / rdocollector.com
# ------------------------------------------------------------

def fetch_madam_nazar_image():
    """Fetch Madam Nazar's current location from rdo.gg API with fallback."""
    try:
        # 1. First try RDO.gg for 100% accurate, up-to-date daily location
        api_url = "https://api.rdo.gg/nazar/"
        response = requests.get(api_url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=10)

        if response.status_code == 200:
            data = response.json()
            nazar_id = data.get('id', '')
            api_loc = data.get('location', '') # e.g. "p_4_plainview"

            locations_map = {
                "MPSW_LOCATION_00": {"name": "بلاينفيو (Plainview)", "slug": "plainview"},
                "MPSW_LOCATION_01": {"name": "تشولا سبرينجز (Cholla Springs)", "slug": "cholla-springs"},
                "MPSW_LOCATION_02": {"name": "هينيجانز ستيد (Hennigan's Stead)", "slug": "hennigan-s-stead"},
                "MPSW_LOCATION_03": {"name": "طول تريز (Tall Trees)", "slug": "tall-trees"},
                "MPSW_LOCATION_04": {"name": "بيج فالي (Big Valley)", "slug": "big-valley"},
                "MPSW_LOCATION_05": {"name": "هارتلاندز (The Heartlands)", "slug": "heartlands"},
                "MPSW_LOCATION_06": {"name": "وايندبرغ / هارتلاندز (Heartlands)", "slug": "heartlands"},
                "MPSW_LOCATION_07": {"name": "غريزليس (Grizzlies East)", "slug": "grizzlies-east"},
                "MPSW_LOCATION_08": {"name": "بولجر جليد (Bolger Glade)", "slug": "bolger-glade"},
                "MPSW_LOCATION_09": {"name": "بلوووتر مارش (Bluewater Marsh)", "slug": "bluewater-marsh"},
                "MPSW_LOCATION_10": {"name": "نهر داكوتا (Dakota River)", "slug": "dakota-river"},
                "MPSW_LOCATION_11": {"name": "روانوكي ريدج (Roanoke Ridge)", "slug": "roanoke-ridge"},
            }

            loc_info = locations_map.get(nazar_id)
            slug = None
            location_name = None

            if loc_info:
                slug = loc_info['slug']
                location_name = loc_info['name']
            elif api_loc:
                slug = api_loc.split('_')[-1]
                location_name = slug.replace('-', ' ').title()

            if slug:
                image_url = f"https://rdocollector.nyc3.digitaloceanspaces.com/img/madam-nazar-{slug}.jpg?t={int(time.time())}"
                img_response = requests.get(image_url, timeout=10)
                if img_response.status_code == 200:
                    img = BytesIO(img_response.content)
                    img.name = f'madam_nazar_{int(time.time())}.jpg'
                    return img, location_name
    except Exception as e:
        print(f"RDO.gg API check failed: {e}")

    # 2. Fallback to rdocollector.com scraping
    try:
        url = f"https://rdocollector.com/madam-nazar?t={int(time.time())}"
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'}, timeout=15)
        response.raise_for_status()
        text = response.text

        # Try to find the image URL directly in the page
        img_match = re.search(r'https://rdocollector\.nyc3\.digitaloceanspaces\.com/img/madam-nazar-([\w-]+)\.jpg', text)
        loc_match = re.search(r'Madam Nazar is in ([\w\s]+)', text)

        if img_match:
            slug = img_match.group(1)
            location = loc_match.group(1).strip() if loc_match else slug.replace('-', ' ').title()
            image_url = img_match.group(0) + f"?t={int(time.time())}"
            img_response = requests.get(image_url, timeout=10)
            if img_response.status_code == 200:
                img = BytesIO(img_response.content)
                img.name = f'madam_nazar_{int(time.time())}.jpg'
                return img, location

        if loc_match:
            location = loc_match.group(1).strip()
            slug = location.lower().replace(' ', '-')
            image_url = f"https://rdocollector.nyc3.digitaloceanspaces.com/img/madam-nazar-{slug}.jpg?t={int(time.time())}"
            img_response = requests.get(image_url, timeout=10)
            if img_response.status_code == 200:
                img = BytesIO(img_response.content)
                img.name = f'madam_nazar_{int(time.time())}.jpg'
                return img, location

        return None, "عذراً، لم يتم العثور على خريطة موقع نزار اليوم."
    except Exception as e:
        return None, f"خطأ في الاتصال بالخوادم: {str(e)}"

# ------------------------------------------------------------
# Data persistence (unchanged)
# ------------------------------------------------------------
def load_data():
    try:
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
            global mute_notifications
            global monitoring_enabled
            global ADMIN_IDS
            mute_notifications = data.get('mute_notifications', False)
            monitoring_enabled = data.get('monitoring_enabled', False)
            admins = data.get('admins', ADMIN_IDS)
            ADMIN_IDS = [admin for admin in admins if admin != 0]
            return data.get('allowed', []), data.get('known', {}), admins
    except FileNotFoundError:
        return [], {}, ADMIN_IDS

def save_data(allowed, known, admins):
    with open(DATA_FILE, 'w') as f:
        json.dump({
            'allowed': allowed,
            'known': known,
            'mute_notifications': mute_notifications,
            'monitoring_enabled': monitoring_enabled,
            'admins': admins
        }, f)

allowed_groups, known_groups, ADMIN_IDS = load_data()

# ------------------------------------------------------------
# Message forwarding (unchanged)
# ------------------------------------------------------------
def forward_to_admins(message, prefix=""):
    if not monitoring_enabled:
        return
    chat_id = message.chat.id
    user = message.from_user
    chat_title = known_groups.get(chat_id, {}).get('title', 'غير معروف')
    msg_text = f"{prefix}📨 رسالة جديدة من المجموعة: {chat_title} (ID: {chat_id})\n"
    msg_text += f"👤 المستخدم: @{user.username or 'لا يوجد'} (ID: {user.id})\n"
    msg_text += f"📝 النص: {message.text or '[رسالة غير نصية]'}"
    for admin_id in [aid for aid in ADMIN_IDS if aid != 0]:
        try:
            bot.send_message(admin_id, msg_text, protect_content=True)
            if message.content_type in ['text', 'photo', 'video', 'document', 'audio', 'voice', 'sticker']:
                try:
                    bot.forward_message(admin_id, chat_id, message.message_id)
                except:
                    pass
        except Exception as e:
            print(f"Failed to forward to admin {admin_id}: {e}")

# ------------------------------------------------------------
# Handlers (unchanged except /text uses new fetch)
# ------------------------------------------------------------
@bot.message_handler(commands=['start'])
def handle_start(message):
    chat_id = message.chat.id
    if message.chat.type in ['group', 'supergroup'] and chat_id not in allowed_groups:
        return
    bot.reply_to(message, """بوت خاص في مدام نزار

- برمجة
@c7oed • @TrlNF
- خاص بقروب : https://t.me/bndx1""", protect_content=True)
    if not mute_notifications:
        user = message.from_user
        for admin_id in [aid for aid in ADMIN_IDS if aid != 0]:
            try:
                bot.send_message(admin_id, f"المستخدم @{user.username} (ID: {user.id}) بدأ البوت في {chat_id}.", protect_content=True)
            except Exception as e:
                print(f"Failed to notify admin {admin_id}: {e}")

@bot.message_handler(commands=['admin'])
def handle_admin(message):
    if message.from_user.id not in [aid for aid in ADMIN_IDS if aid != 0]:
        bot.reply_to(message, "غير مخول لك.", protect_content=True)
        return
    markup = InlineKeyboardMarkup()
    mute_text = "إلغاء كتم الإشعارات" if mute_notifications else "كتم الإشعارات"
    markup.add(InlineKeyboardButton(mute_text, callback_data="toggle_mute"))
    monitor_text = "إيقاف المراقبة" if monitoring_enabled else "تفعيل المراقبة"
    markup.add(InlineKeyboardButton(monitor_text, callback_data="toggle_monitoring"))
    markup.add(InlineKeyboardButton("إدارة المشرفين", callback_data="manage_admins"))
    bot.reply_to(message, "لوحة التحكم:", reply_markup=markup, protect_content=True)

@bot.message_handler(content_types=['new_chat_members'])
def handle_new_chat_members(message):
    for member in message.new_chat_members:
        if member.id == bot.get_me().id:
            chat_id = message.chat.id
            title = message.chat.title or "مجموعة بدون عنوان"
            if chat_id not in known_groups:
                known_groups[chat_id] = {'title': title, 'status': 'pending'}
                save_data(allowed_groups, known_groups, ADMIN_IDS)
            if chat_id not in allowed_groups:
                markup = InlineKeyboardMarkup()
                markup.add(InlineKeyboardButton("الموافقة", callback_data=f"approve_{chat_id}"))
                markup.add(InlineKeyboardButton("المغادرة", callback_data=f"leave_{chat_id}"))
                for admin_id in [aid for aid in ADMIN_IDS if aid != 0]:
                    try:
                        bot.send_message(admin_id, f"تمت إضافة البوت إلى {title} (ID: {chat_id})", reply_markup=markup, protect_content=True)
                    except:
                        pass
            else:
                bot.send_message(chat_id, "البوت تمت الموافقة عليه وجاهز!", protect_content=True)

@bot.callback_query_handler(func=lambda call: True)
def handle_callback(call):
    if call.from_user.id not in [aid for aid in ADMIN_IDS if aid != 0]:
        bot.answer_callback_query(call.id, "غير مخول لك.")
        return
    data = call.data
    if data.startswith("approve_"):
        chat_id = int(data.split("_")[1])
        if chat_id not in allowed_groups:
            allowed_groups.append(chat_id)
            if chat_id in known_groups:
                known_groups[chat_id]['status'] = 'allowed'
            save_data(allowed_groups, known_groups, ADMIN_IDS)
            for admin_id in [aid for aid in ADMIN_IDS if aid != 0]:
                try:
                    bot.send_message(admin_id, f"تمت الموافقة على {chat_id} ({known_groups.get(chat_id, {}).get('title', '')})", protect_content=True)
                except:
                    pass
            try:
                bot.send_message(chat_id, "تمت الموافقة على البوت!", protect_content=True)
            except:
                pass
        bot.answer_callback_query(call.id, "تمت الموافقة.")
    elif data.startswith("leave_"):
        chat_id = int(data.split("_")[1])
        try:
            bot.leave_chat(chat_id)
            if chat_id in allowed_groups:
                allowed_groups.remove(chat_id)
            if chat_id in known_groups:
                known_groups[chat_id]['status'] = 'left'
            save_data(allowed_groups, known_groups, ADMIN_IDS)
            for admin_id in [aid for aid in ADMIN_IDS if aid != 0]:
                try:
                    bot.send_message(admin_id, f"مغادرة {chat_id} ({known_groups.get(chat_id, {}).get('title', '')})", protect_content=True)
                except:
                    pass
        except:
            pass
        bot.answer_callback_query(call.id, "تم المغادرة.")
    elif data == "toggle_mute":
        global mute_notifications
        mute_notifications = not mute_notifications
        save_data(allowed_groups, known_groups, ADMIN_IDS)
        status = "كتم" if mute_notifications else "إلغاء الكتم"
        bot.answer_callback_query(call.id, status)
    elif data == "toggle_monitoring":
        global monitoring_enabled
        monitoring_enabled = not monitoring_enabled
        save_data(allowed_groups, known_groups, ADMIN_IDS)
        status = "مراقبة ON" if monitoring_enabled else "مراقبة OFF"
        bot.answer_callback_query(call.id, status)
    elif data == "manage_admins":
        markup = InlineKeyboardMarkup()
        markup.add(InlineKeyboardButton("إضافة مشرف", callback_data="add_admin"))
        markup.add(InlineKeyboardButton("إزالة مشرف", callback_data="remove_admin"))
        markup.add(InlineKeyboardButton("قائمة المشرفين", callback_data="list_admins"))
        bot.send_message(call.from_user.id, "إدارة المشرفين:", reply_markup=markup, protect_content=True)
    elif data == "add_admin":
        bot.send_message(call.from_user.id, "أرسل ID المشرف الجديد:", protect_content=True)
        bot.register_next_step_handler(call.message, add_admin)
    elif data == "remove_admin":
        list_admins_for_removal(call)
    elif data == "list_admins":
        admins_list = "\n".join([f"ID: {aid}" for aid in ADMIN_IDS if aid != 0])
        bot.send_message(call.from_user.id, f"المشرفون:\n{admins_list}", protect_content=True)
    elif data.startswith("remove_admin_"):
        admin_id = int(data.split("_")[2])
        if admin_id in ADMIN_IDS and len([a for a in ADMIN_IDS if a != 0]) > 1:
            ADMIN_IDS.remove(admin_id)
            save_data(allowed_groups, known_groups, ADMIN_IDS)
        bot.answer_callback_query(call.id, "تمت الإزالة.")

def add_admin(message):
    try:
        new_id = int(message.text.strip())
        if new_id not in ADMIN_IDS:
            if 0 in ADMIN_IDS:
                ADMIN_IDS[ADMIN_IDS.index(0)] = new_id
            else:
                ADMIN_IDS.append(new_id)
            save_data(allowed_groups, known_groups, ADMIN_IDS)
            bot.send_message(message.chat.id, f"تم إضافة {new_id}.", protect_content=True)
        else:
            bot.send_message(message.chat.id, "موجود مسبقاً.", protect_content=True)
    except:
        bot.send_message(message.chat.id, "ID غير صحيح.", protect_content=True)

def list_admins_for_removal(call):
    markup = InlineKeyboardMarkup()
    for admin_id in [a for a in ADMIN_IDS if a != 0]:
        markup.add(InlineKeyboardButton(f"إزالة {admin_id}", callback_data=f"remove_admin_{admin_id}"))
    bot.send_message(call.from_user.id, "اختر مشرفاً:", reply_markup=markup, protect_content=True)

# ------------------------------------------------------------
# Main text handler
# ------------------------------------------------------------
@bot.message_handler(commands=['nazar', 'n', 'madam_nazar', 'location', 'نزار', 'مدام_نزار'])
def handle_nazar_command(message):
    process_nazar_request(message)

@bot.message_handler(content_types=['text'])
def handle_text(message):
    chat_id = message.chat.id
    text = message.text.strip()

    if message.chat.type in ['group', 'supergroup'] and chat_id in allowed_groups:
        forward_to_admins(message)

    # Triggers for the bot
    triggers = ["نزار", "مدام نزار"]
    bot_username = bot.get_me().username

    # Check if the message contains any of the triggers
    # or if it is a reply to one of the bot's messages
    match = False

    # Check for direct keyword usage (exact match)
    if text in triggers:
        match = True
    # Check for keywords with bot username mention (exact match)
    elif any(text == f"{t}@{bot_username}" for t in triggers):
        match = True
    # Check if it's a reply to the bot
    elif message.reply_to_message and message.reply_to_message.from_user.id == bot.get_me().id:
        match = True

    if match:
        process_nazar_request(message)

def process_nazar_request(message):
    chat_id = message.chat.id
    is_admin_user = message.from_user.id in [aid for aid in ADMIN_IDS if aid != 0]

    # Check if group is permitted (admins skip this check)
    if message.chat.type in ['group', 'supergroup'] and chat_id not in allowed_groups and not is_admin_user:
        return

    try:
        is_group = message.chat.type in ['group', 'supergroup']
        if is_group:
            user_status = bot.get_chat_member(chat_id, message.from_user.id).status
            is_admin = user_status in ['administrator', 'creator']
            current_time = time.time()
            if not is_admin and current_time - last_request_time[chat_id] < 300:
                return
            last_request_time[chat_id] = current_time

        global NAZAR_DATA
        now = time.time()

        # Fast path: use cache (updated within the last hour)
        if NAZAR_DATA['file_id'] and (now - NAZAR_DATA['last_update'] < 3600):
            caption = f"📍 موقع مدام نزار اليوم: {NAZAR_DATA['location']}"
            bot.send_photo(chat_id, photo=NAZAR_DATA['file_id'], caption=caption, protect_content=True)
            # Notify admins if needed
            if not mute_notifications:
                user = message.from_user
                for admin_id in [aid for aid in ADMIN_IDS if aid != 0]:
                    try:
                        chat_name = known_groups.get(chat_id, {}).get('title', 'غير معروف') if is_group else 'خاص'
                        bot.send_message(admin_id, f"📊 @{user.username} (ID: {user.id})\nاستخدم البوت في {chat_name} (Cache Hit)", protect_content=True)
                    except: pass
            return

        # Slow path: fetch and update cache
        img, result_data = fetch_madam_nazar_image()
        if img is None:
            bot.reply_to(message, result_data, protect_content=True)
            return

        caption = f"📍 موقع مدام نزار اليوم: {result_data}"
        sent_msg = bot.send_photo(chat_id, photo=img, caption=caption, protect_content=True)

        # Update cache with the file_id Telegram assigned to the photo
        try:
            NAZAR_DATA['file_id'] = sent_msg.photo[-1].file_id
            NAZAR_DATA['location'] = result_data
            NAZAR_DATA['last_update'] = now
        except:
            pass

        if not mute_notifications:
            user = message.from_user
            for admin_id in [aid for aid in ADMIN_IDS if aid != 0]:
                try:
                    chat_name = known_groups.get(chat_id, {}).get('title', 'غير معروف') if is_group else 'خاص'
                    bot.send_message(admin_id,
                        f"📊 @{user.username} (ID: {user.id})\n"
                        f"استخدم البوت في {chat_name} ({chat_id})", protect_content=True)
                except:
                    pass
    except telebot.apihelper.ApiTelegramException as te:
        if "bot was kicked" in str(te).lower():
            return
        bot.reply_to(message, "خطأ في صلاحيات البوت. تأكد من كونه مشرفاً.", protect_content=True)
    except Exception as e:
        bot.reply_to(message, "حدث خطأ غير متوقع.", protect_content=True)
        print(f"Error: {e}")

@bot.message_handler(content_types=['photo', 'video', 'document', 'audio', 'voice', 'sticker', 'animation', 'video_note'])
def handle_media(message):
    if message.chat.type in ['group', 'supergroup'] and message.chat.id in allowed_groups:
        forward_to_admins(message)

if __name__ == '__main__':
    print("🤠 البوت يعمل باستخدام API: https://rdocollector.com/madam-nazar")
    bot.infinity_polling()
