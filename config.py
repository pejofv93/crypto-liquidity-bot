# --------------------------
# CONFIGURACIÓN GENERAL
# --------------------------

# Telegram
TELEGRAM_TOKEN = 8167233255:AAG3HlvHOKif61HOFPYCOUEUeIY4ovMbIQ8
CHAT_ID = 389493035

# WhatsApp y Email (opcional)
WHATSAPP_API_KEY = ""
WHATSAPP_CHAT_ID = ""
EMAIL_SENDER = ""
EMAIL_PASSWORD = ""
EMAIL_RECEIVER = ""

# Umbrales y configuración de alertas
WHALE_THRESHOLD = 500_000           # Volumen mínimo para considerar "movimiento grande"
PERCENTAGE_CHANGE_THRESHOLD = 5     # % de cambio para alerta
ALERT_REPEAT_MINUTES = 10           # Repetir alertas si aún aplican

# Activos a monitorear
ALL_CRYPTO_SYMBOLS = ["BTC", "ETH", "BNB", "ADA", "SOL"]  # agregar todos los que quieras
ALL_STOCK_SYMBOLS = ["AAPL", "TSLA", "MSFT"]              # agregar todos los que quieras

# Indicadores técnicos y patrones
INDICATORS = ["SMA", "EMA", "RSI", "MACD", "Bollinger"]  # se pueden usar en análisis futuros
