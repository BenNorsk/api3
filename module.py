# This cleans the data of the /prices api a bit.
def up_or_down(num):
    if num > 0:
        return "up"
    else:
        return "down"


def clean_data(data):
    currencies = {}
    for coin in data:
        currency = {}
        currency["id"] = coin["id"]
        currency["name"] = coin["name"]
        currency["logo_url"] = coin["logo_url"]
        currency["price"] = f'{float(coin["price"]):.2f}'
        num = float(coin["1d"]["price_change_pct"])
        currency["change"] = up_or_down(num)
        currency["market_cap_dominance"] = coin["market_cap_dominance"]
        currency["daily_price_change"] = coin["1d"]["price_change_pct"]
        currencies[coin["id"]] = currency
    return currencies

# This gets the fundamental data for "/"
def get_brand_data(base_url):
    brand_data = {
        "logo": f'{base_url}images/brand_images/logo.png',
        "logo_long": f'{base_url}images/brand_images/logo_long.png',
        "blockchain": f'{base_url}images/brand_images/blockchain.jpeg'
    }
    return brand_data

