from whale_alert import get_whale_transactions
from telegram_bot import send_alert

# Umbral de porcentaje para considerar alerta urgente
PERCENTAGE_CHANGE_THRESHOLD = 5  # puedes ajustar

def check_and_send_alerts():
    whales = get_whale_transactions()
    
    for tx in whales:
        symbol = tx["symbol"]
        price = tx["price"]
        volume = tx["volume_usd"]

        # Mensaje de alerta
        message = (
            f"🚨 ALERTA DE MOVIMIENTO GRANDE 🚨\n"
            f"Activo: {symbol}\n"
            f"Precio actual: ${price}\n"
            f"Volumen en USD: ${volume:,}\n"
            f"Potencial impacto: Alto"
        )

        # Enviar alerta por Telegram
        send_alert(message)

# Prueba rápida
if __name__ == "__main__":
    check_and_send_alerts()
