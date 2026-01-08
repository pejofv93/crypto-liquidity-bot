def get_price_volume(symbol, market="crypto"):
    if market == "crypto":
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}USDT"
        data = requests.get(url).json()
        return float(data["lastPrice"]), float(data["quoteVolume"])
    elif market == "stock":
        # Aquí implementar la API gratuita de Yahoo Finance o Alpha Vantage
        pass
