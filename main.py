from flask import Flask
import requests
from module import clean_data, get_brand_data
from board_member_data import get_board_members
from posts_data import get_posts_data
from document_data import get_documents
from partners_data import get_partners_data

# –––––––––––– GET PRICES ––––––––––––––

prices = {"ADA":{"change":"down","daily_price_change":"-0.0025","id":"ADA","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/ada.svg","market_cap_dominance":"0.0169","name":"Cardano","price":"1.01"},"AVAX":{"change":"up","daily_price_change":"0.0565","id":"AVAX","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/AVAX.svg","market_cap_dominance":"0.0113","name":"Avalanche","price":"88.11"},"BNB":{"change":"up","daily_price_change":"0.0031","id":"BNB","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/bnb.svg","market_cap_dominance":"0.0350","name":"Binance Coin","price":"397.71"},"BTC":{"change":"up","daily_price_change":"0.0004","id":"BTC","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/btc.svg","market_cap_dominance":"0.4058","name":"Bitcoin","price":"40838.48"},"ETH":{"change":"up","daily_price_change":"0.0131","id":"ETH","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/eth.svg","market_cap_dominance":"0.1828","name":"Ethereum","price":"2916.46"},"SOL":{"change":"up","daily_price_change":"0.0099","id":"SOL","logo_url":"https://nomics-api.s3.us-east-2.amazonaws.com/static/images/currencies/SOL2.jpg","market_cap_dominance":"0.0159","name":"Solana","price":"94.95"},"XRP":{"change":"up","daily_price_change":"0.0129","id":"XRP","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/XRP.svg","market_cap_dominance":"0.0196","name":"XRP","price":"0.78"}}


# ––––––––––––– Get prices –––––––––––––

def get_prices():
    # FOR GIAN: 
    # 
    # Before you start, type:
    # ______________________
    # git checkout master
    # git pull origin master
    # git branch api-keys
    # git checkout api-keys
    # _____________________
    # GENERAL INFORMATION:
    # We use the Flask application framework. Hence our api is a flask app. To test our flask app locally, run 'flask run'
    # Then you can see if it works by accessing the link your flask server serves you (127.0.0.1/)..

    #
    # Below you see our api key, with which we make api calls.
    # The problem with the key is, that is has only a limited amount of requests we can do.
    # Therefore, you should create many (at least 20) free API keys from the Nomics API, in make the API calls
    # using these different keys. If one key expires (i.e. doesn't work anymore), make the program as such, that it 
    # automatically uses the next key. Make sure that the program does not break down if no key works. Also, old keys
    # that don't work anymore should be removed (or marked as deprecated)
    # Now how do you do this?
    # 1. create a txt or csv file containing all keys
    # 2. Create a function, that reads the txt file into python
    #    a. iterate over the valid keys
    #    b. Make an API call with the first key.
    #       I. If the key works, return the data about the prices
    #       II. If the key doesn't work, delete it or mark it as invalid (hint: use try/except)
    #    c. Should no key work, make sure that you return a dictionary of the same structure anyway (like I do below)
    # 
    # When you're done;
    # Copy / paste your code to app.py
    # then type:
    # ______________________
    # git add .
    # git commit -m "finished api key tasks"
    # git push origin api-keys

    api_key = 'ab4d9d5a55d9600d15ca26450ba9e6533dc496a5'
    url = f'https://api.nomics.com/v1/currencies/ticker?key={api_key}&ids=BTC,ETH,ADA,SOL,XRP,BNB,AVAX&interval=1d,30d&convert=USD'
    try:
        response = requests.get(url)
        data = response.json()
        data = clean_data(data)
        prices = data
        return prices
    except:
        print("error")
        return {"ADA":{"change":"down","daily_price_change":"-0.0025","id":"ADA","logo_url":"https://cryptologos.cc/logos/cardano-ada-logo.svg?v=035","market_cap_dominance":"0.0169","name":"Cardano","price":"0.00"},"AVAX":{"change":"up","daily_price_change":"0.0565","id":"AVAX","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/AVAX.svg","market_cap_dominance":"0.0113","name":"Avalanche","price":"0.00"},"BNB":{"change":"up","daily_price_change":"0.0031","id":"BNB","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/bnb.svg","market_cap_dominance":"0.0350","name":"Binance Coin","price":"0.00"},"BTC":{"change":"up","daily_price_change":"0.0004","id":"BTC","logo_url":"https://cryptologos.cc/logos/bitcoin-btc-logo.svg?v=035","market_cap_dominance":"0.4058","name":"Bitcoin","price":"0.00"},"ETH":{"change":"up","daily_price_change":"0.0131","id":"ETH","logo_url":"https://cryptologos.cc/logos/ethereum-eth-logo.svg?v=035","market_cap_dominance":"0.1828","name":"Ethereum","price":"0.00"},"SOL":{"change":"up","daily_price_change":"0.0099","id":"SOL","logo_url":"https://cryptologos.cc/logos/solana-sol-logo.svg?v=035","market_cap_dominance":"0.0159","name":"Solana","price":"0.00"},"XRP":{"change":"up","daily_price_change":"0.0129","id":"XRP","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/XRP.svg","market_cap_dominance":"0.0196","name":"XRP","price":"0.00"}}


# ––––––––––––– INITIALISE APP –––––––––––

app = Flask(__name__)

# ––––––––––– ROUTES ––––––––––––––


# https://api3-341213.appspot.com/
base_url = "https://raw.githubusercontent.com/BenNorsk/api-data/master/"

@app.route("/")
def welcome():
    brand_data = get_brand_data(base_url)
    board_data = get_board_members(base_url)
    posts_data = get_posts_data(base_url)
    documents_data = get_documents(base_url)
    partners_data = get_partners_data(base_url)
    standard_data = {"title": "Crypto Society St. Gallen", 
            "welcome_text": "The Crypto Society is the number one address for crypto enthusiastic students in St. Gallen! Join up to meet like–minded people, deepen your knowledge about crypto and emerge in this world-changing industry! In weekly meetings, and regular events with bigger companies and startups, you may learn plenty about the future of the blockchain and crypto technology. The Crypto Society will connect you perfectly with the industry, and serve as your starting point for a future in the future of finance! Also of course, never forget to miss out on our social events of the great crypto community!",
            "member_link": "https://docs.google.com/forms/d/e/1FAIpQLSeP7INDPgUYb8nCraOel61WOgFn48dnii5fDMLcyTTBI8XIeg/viewform",
            "linked_in": "https://www.linkedin.com/company/cryptosocietystgallen/mycompany/",
            "instagram": "https://www.instagram.com/cryptosocietystgallen/",
            "whats_app": "https://chat.whatsapp.com/CUYwYyav4Hy0MLmemrhr3M",
            "discord": "https://discord.gg/cUBtDBTwFB",
            "members": "85+",
            "associates": "200+",
            "followers": "1000+",
            "store_link": "https://www.etsy.com/ch/shop/CryptoSociety?ref=simple-shop-header-name&listing_id=1164741068",
            "store_text": "The Crypto Society has launched its official store. Acquire the exclusive Crypto Society hoodies today, or check out our other creations!",
            "store_img": "https://raw.githubusercontent.com/BenNorsk/api-data/master/images/post_images/store-post/store.png",
            "prices": {**get_prices()},
            "posts": posts_data,
            "documents": {**documents_data},
            "board": board_data  ,
            "partners": partners_data
    }
    data = {**brand_data, **standard_data}
    return data