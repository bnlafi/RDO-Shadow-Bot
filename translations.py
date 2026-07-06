TRANSLATIONS = {
    "general": "🌍 التحديات العامة",
    "bounty_hunter": "🤠 صائد الجوائز",
    "trader": "🚚 التاجر",
    "collector": "💰 الجامع",
    "moonshiner": "🥃 المهرب",
    "naturalist": "🦌 عالم الطبيعة",
}


def translate(text: str) -> str:
    return TRANSLATIONS.get(text, text)
