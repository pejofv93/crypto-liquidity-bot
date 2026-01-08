def get_large_movements():
    all_assets = ALL_CRYPTO_SYMBOLS + ALL_STOCK_SYMBOLS
    movements = []
    for asset in all_assets:
        price, volume = get_price_volume(asset)
        if volume >= WHALE_THRESHOLD:
            movements.append({"asset": asset, "price": price, "volume": volume})
    return movements

