TRANSLATIONS = {

    # الأقسام
    "general": "🌍 التحديات العامة",
    "easy": "⭐ التحديات السهلة",
    "med": "⭐⭐ التحديات المتوسطة",
    "hard": "⭐⭐⭐ التحديات الصعبة",

    "bounty_hunter": "🤠 صائد الجوائز",
    "trader": "🚚 التاجر",
    "collector": "💰 الجامع",
    "moonshiner": "🥃 المهرب",
    "naturalist": "🦌 عالم الطبيعة",

    # التحديات العامة
    "MPRC_TURKEYS_SKINNED": "🦃 سلخ 3 ديك رومي",
    "MPRC_CONSUMABLE_BECAME_DRUNK": "🍺 اسكر مرة واحدة",
    "MPRC_CUSTOMIZATION_HORSE_KIT": "🐎 غيّر تجهيز الحصان",
    "MPRC_FME_ATTEMPTS": "🎯 أكمل حدث حر",
    "MPRC_HORSE_JUMP_FROM_HEIGHT": "🐴 اقفز من مكان مرتفع بالحصان",
    "MPRC_PLAYERS_KILLED_FROM_HIP_SHOWDOWN": "🔫 اقتل لاعبًا من الخصر",
    "MPRC_PLAYERS_KILLED_SHOWDOWN_TIMER": "⚔️ اقتل لاعبًا في المواجهات",

    # صائد الجوائز
    "MPRC_BOUNTY_GENERAL_DELIVERED": "📦 سلّم مطلوبين",
    "MPRC_BOUNTY_USED_EAGLE_EYE": "👁️ استخدم عين النسر",
    "MPRC_BOUNTY_USED_TRACK_ARROW": "🏹 استخدم سهم التتبع",
    "MPRC_BOUNTY_GENERAL_DELIVERED_HARD": "📦 سلّم مطلوبين (صعب)",
    "MPRC_BOUNTY_GENERAL_DELIVERED_MULTI_TARGET": "🎯 سلّم عدة مطلوبين",
    "MPRC_BOUNTY_GENERAL_DELIVERED_TIMED_HARD": "⏱️ أكمل مهمة مطلوبة بوقت",

    # التاجر
    "MPRC_TRADER_SUPPLIES_DONATED": "📦 تبرع بالإمدادات",
    "MPRC_TRADER_SUPPLIES_DONATED_CARCASS_PERFECT": "🦌 تبرع بجثة مثالية",
    "MPRC_TRADER_TRAVEL_WAGON": "🚚 قد عربة التاجر",
    "MPRC_TRADER_RESUPPLY_COMPLETED": "📦 أكمل إعادة التزويد",
    "MPRC_TRADER_STEW_EATEN": "🍲 تناول يخنة كريبس",

    # الجامع
    "MPRC_COLLECTOR_ARROWHEADS_FOUND": "🏹 اعثر على رؤوس سهام",
    "MPRC_COLLECTOR_COINS_FOUND": "🪙 اعثر على عملات",
    "MPRC_COLLECTOR_USED_MAP": "🗺️ استخدم خريطة جامع",
    "MPRC_COLLECTOR_ITEMS_LOOTED_ENEMY": "💰 اجمع مقتنيات من الأعداء",
    "MPRC_COLLECTOR_USED_METAL_DETECTOR": "📡 استخدم كاشف المعادن",
    "MPRC_COLLECTOR_WILD_FLOWERS_FOUND": "🌼 اعثر على زهور برية",

    # المهرب
    "MPRC_MOONSHINER_MOONSHINE_DRANK": "🥃 اشرب مون شاين",
    "MPRC_MOONSHINER_MOONSHINE_SERVED_BAR": "🍺 قدّم مون شاين في الحانة",
    "MPRC_MOONSHINER_MOONSHINE_SOLD_BUYER": "💰 بع مون شاين لمشترٍ",
    "MPRC_MOONSHINER_TRAVEL_WAGON": "🚛 قد عربة التهريب",

    # عالم الطبيعة
    "MPRC_NATURALIST_DONT_KILL_ANIMALS": "🦌 لا تقتل أي حيوان",
    "MPRC_NATURALIST_CRAFTED_BLENDING_TONIC": "🧪 اصنع منشط التخفي",
    "MPRC_NATURALIST_PHOTO_ANIMAL_LEGENDARY": "📷 صوّر حيوانًا أسطوريًا",
    "MPRC_NATURALIST_TRANQ_ANIMAL_REVIVED": "💉 أنعش حيوانًا بعد تخديره",
    "MPRC_NATURALIST_CRAFTED_COOKED_WILDERNESS_CAMP": "🔥 اطبخ في المخيم البري",
}


def translate(text: str) -> str:
    return TRANSLATIONS.get(text, text)
