# This cleans the data of the /prices api a bit.
def clean_data(data):
    currencies = {}
    for coin in data:
        currency = {}
        currency["id"] = coin["id"]
        currency["name"] = coin["name"]
        currency["logo_url"] = coin["logo_url"]
        currency["price"] = coin["price"]
        currency["market_cap_dominance"] = coin["market_cap_dominance"]
        currency["daily_price_change"] = coin["1d"]["price_change_pct"]
        currencies[coin["id"]] = currency
    return currencies

# This gets the fundamental data for "/"
def get_brand_data():
    brand_data = {
        "logo": "images/brand_images/logo.png",
        "logo_long": "images/brand_images/logo_long.png",
        "blockchain": "images/brand_images/blockchain.jpeg"
    }
    return brand_data

