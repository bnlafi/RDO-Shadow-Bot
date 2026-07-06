import requests

API_URL = "https://api.rdo.gg/challenges"


def get_daily_challenges():
    try:
        response = requests.get(API_URL, timeout=15)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"API Error: {e}")
        return None
