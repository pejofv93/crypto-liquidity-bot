import requests

# Umbral mínimo para considerar "movimiento grande" en USD
WHALE_THRESHOLD = 500_000  # puedes ajustar según tu criterio

# Lista de criptos a monitorear (puedes ampliar)
CRYPTO_SYMBOLS = ["BTC", "ETH", "BNB", "ADA", "SOL"]

# Función para obtener precio y volumen de Binance
def get_binance_price_volume(symbol):
    try:
        url = f"https://api.binance.com/api/v3/ticker/24hr?symbol={symbol}USDT"
        data = requests.get(url).json()
        price = float(data["lastPrice"])
        volume = float(data["quoteVolume"])  # volumen en USD
        return price, volume
    except Exception as e:
        print(f"Error al obtener datos de {symbol}: {e}")
        return 0, 0

# Función para detectar "movimientos grandes" en el último día
def get_whale_transactions():
    whales = []
    for symbol in CRYPTO_SYMBOLS:
        price, volume = get_binance_price_volume(symbol)
        if volume >= WHALE_THRESHOLD:
            whales.append({
                "symbol": symbol,
                "price": price,
                "volume_usd": volume
            })
    return whales

# Prueba rápida
if __name__ == "__main__":
    txs = get_whale_transactions()
    for tx in txs:
        print(f"🐋 Movimiento grande detectado: {tx['symbol']} | Volumen: ${tx['volume_usd']:,} | Precio: ${tx['price']}")
