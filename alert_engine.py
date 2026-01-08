from telegram_bot import send_alert
from whale_alert import get_large_movements
import time

def evaluate_opportunities():
    movements = get_large_movements()
    for m in movements:
        # Aquí la IA decide si es oportunidad según tu lógica avanzada
        # Por ejemplo: combinar indicadores, patrones y flujo de liquidez
        if m["volume"] > WHALE_THRESHOLD:
            message = f"ALERTA: {m['asset']} Volumen: {m['volume']}, Precio: {m['price']}"
            send_alert(message)

# Loop 24/7
while True:
    evaluate_opportunities()
    time.sleep(ALERT_REPEAT_MINUTES * 60)
