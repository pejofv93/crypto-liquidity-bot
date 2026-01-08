"""
CONFIGURACIÓN GLOBAL DEL BOT DE TRADING
"""

# ------------------------------
# TELEGRAM
# ------------------------------
TELEGRAM_TOKEN = 8167233255:AAG3HlvHOKif61HOFPYCOUEUeIY4ovMbIQ8
CHAT_ID = 389493035

# ------------------------------
# WHATSAPP Y EMAIL (opcional)
# ------------------------------
WHATSAPP_API_KEY = ""
WHATSAPP_CHAT_ID = ""
EMAIL_SENDER = ""
EMAIL_PASSWORD = ""
EMAIL_RECEIVER = ""

# ------------------------------
# UMBRALES DE ALERTA
# ------------------------------
# Volumen mínimo para considerar "movimiento grande" (USD)
WHALE_THRESHOLD = 500_000

# % de cambio mínimo para considerarse significativo
PERCENTAGE_CHANGE_THRESHOLD = 5

# Minutos antes de repetir una alerta si sigue vigente
ALERT_REPEAT_MINUTES = 10

# ------------------------------
# INDICADORES TÉCNICOS (completos)
# ------------------------------
INDICATORS = [
    # Medias móviles
    "SMA", "EMA", "WMA", "DEMA", "TEMA",
    # Osciladores
    "RSI", "Stochastic", "MACD", "CCI", "ROC",
    # Tendencia
    "ADX", "ParabolicSAR", "Ichimoku",
    # Volatilidad
    "BollingerBands", "ATR", "DonchianChannel",
    # Momentum
    "Momentum", "OBV", "ForceIndex", "EaseOfMovement",
    # Volumen
    "VWAP",
    # Estadísticos
    "Williams %R", "ChaikinMoneyFlow"
]

# ------------------------------
# LISTADO DINÁMICO DE ACTIVOS
# ------------------------------
ALL_CRYPTO_SYMBOLS = []  # se llenará desde load_symbols.py
ALL_STOCK_SYMBOLS = []   # se llenará desde load_symbols.py

# Máximos a cargar para no saturar
MAX_CRYPTO_SYMBOLS = 2000
MAX_STOCK_SYMBOLS = 5000
