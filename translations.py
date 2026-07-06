TRANSLATIONS = {
    # الأقسام
    "general": "🌍 التحديات العامة",
    "bounty_hunter": "🤠 صائد الجوائز",
    "trader": "🚚 التاجر",
    "collector": "💰 الجامع",
    "moonshiner": "🥃 المهرب",
    "naturalist": "🦌 عالم الطبيعة",

    # Trader
    "MPRC_TRADER_STEW_EATEN": "🍲 تناول يخنة كريبس",
    "MPRC_TRADER_RESUPPLY_COMPLETED": "📦 أكمل مهمة إعادة التموين",
    "MPRC_TRADER_SUPPLIES_DONATED_ANIMAL_MEDIUM": "🦌 تبرع بحيوان متوسط",
    "MPRC_TRADER_SUPPLIES_DONATED_ANIMAL_LARGE": "🦬 تبرع بحيوان كبير",
    "MPRC_TRADER_GOODS_SOLD_LOCAL": "🚚 بع بضاعة محلية",
    "MPRC_TRADER_GOODS_SOLD_DISTANT": "🌍 بع بضاعة بعيدة",

    # Collector
    "MPRC_COLLECTOR_COINS_FOUND": "🪙 اعثر على عملات",
    "MPRC_COLLECTOR_ARROWHEADS_FOUND": "🏹 اعثر على رؤوس سهام",
    "MPRC_COLLECTOR_USED_MAP": "🗺️ استخدم خريطة جامع",
    "MPRC_COLLECTOR_COLLECTIBLES_FOUND": "💎 اعثر على مقتنيات",

    # Bounty Hunter
    "MPRC_BOUNTY_GENERAL_DELIVERED_HARD": "🤠 سلّم مطلوبًا بصعوبة عالية",
    "MPRC_BOUNTY_GENERAL_DELIVERED_MULTI_TARGET": "🎯 سلّم عدة مطلوبين",
    "MPRC_BOUNTY_GENERAL_DELIVERED_TIMED_HARD": "⏱️ سلّم مطلوبًا قبل انتهاء الوقت",

    # Moonshiner
    "MPRC_MOONSHINER_MOONSHINE_SOLD_BUYER": "🥃 بع دفعة مون شاين",
    "MPRC_MOONSHINER_MOONSHINE_SERVED_BAR": "🍺 قدّم مون شاين في الحانة",
    "MPRC_MOONSHINER_DRANK_MOONSHINE": "🥃 اشرب مون شاين",

    # Naturalist
    "MPRC_NATURALIST_USED_LEGENDARY_BAIT": "🦌 استخدم طُعمًا أسطوريًا",
    "MPRC_NATURALIST_PHOTO_ANIMAL_LEGENDARY": "📷 صوّر حيوانًا أسطوريًا",
    "MPRC_NATURALIST_CRAFTED_BLENDING_TONIC": "🧪 اصنع منشط التخفي",
    "MPRC_NATURALIST_TRANQ_ANIMAL_REVIVED": "💉 أنعش حيوانًا بعد تخديره",
}


def translate(text: str) -> str:
    return TRANSLATIONS.get(text, text.replace("_", " "))
