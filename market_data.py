import requests

BINANCE_URL = "https://api.binance.com/api/v3/ticker/24hr"

def get_market_data(symbol: str):
    params = {"symbol": f"{symbol}USDT"}
    response = requests.get(BINANCE_URL, params=params)
    data = response.json()

    return {
        "price": float(data["lastPrice"]),
        "volume": float(data["volume"]),
        "price_change_percent": float(data["priceChangePercent"])
    }
