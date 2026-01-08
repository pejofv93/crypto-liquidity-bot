import requests
import yfinance as yf
from config import MAX_CRYPTO_SYMBOLS, MAX_STOCK_SYMBOLS

# --------------------------
# CRIPTOMONEDAS (Binance)
# --------------------------
def load_all_crypto_symbols():
    try:
        url = "https://api.binance.com/api/v3/exchangeInfo"
        data = requests.get(url).json()
        symbols = [
            s["symbol"].replace("USDT", "")
            for s in data["symbols"]
            if s["symbol"].endswith("USDT")
        ]
        return symbols[:MAX_CRYPTO_SYMBOLS]
    except Exception as e:
        print(f"Error cargando cripto: {e}")
        return []

# --------------------------
# ACCIONES (Yahoo Finance)
# --------------------------
def load_all_stock_symbols():
    """
    Carga tickers de acciones.
    Se puede ampliar con CSV de NYSE/NASDAQ/S&P500.
    """
    try:
        sp500 = yf.Tickers("AAPL MSFT TSLA GOOG AMZN")  # ejemplo inicial
        tickers = list(sp500.tickers.keys())
        return tickers[:MAX_STOCK_SYMBOLS]
    except Exception as e:
        print(f"Error cargando acciones: {e}")
        return []
