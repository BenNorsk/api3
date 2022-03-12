from flask import Flask, flash, request, redirect, url_for
import requests
import json
import os
from module import clean_data, get_brand_data
from board_member_data import get_board_members
from posts_data import get_posts_data
from document_data import get_documents
from werkzeug.utils import secure_filename
from apscheduler.schedulers.background import BackgroundScheduler

# –––––––––––– GET PRICES ––––––––––––––

prices = {"ADA":{"change":"down","daily_price_change":"-0.0025","id":"ADA","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/ada.svg","market_cap_dominance":"0.0169","name":"Cardano","price":"1.01"},"AVAX":{"change":"up","daily_price_change":"0.0565","id":"AVAX","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/AVAX.svg","market_cap_dominance":"0.0113","name":"Avalanche","price":"88.11"},"BNB":{"change":"up","daily_price_change":"0.0031","id":"BNB","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/bnb.svg","market_cap_dominance":"0.0350","name":"Binance Coin","price":"397.71"},"BTC":{"change":"up","daily_price_change":"0.0004","id":"BTC","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/btc.svg","market_cap_dominance":"0.4058","name":"Bitcoin","price":"40838.48"},"ETH":{"change":"up","daily_price_change":"0.0131","id":"ETH","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/eth.svg","market_cap_dominance":"0.1828","name":"Ethereum","price":"2916.46"},"SOL":{"change":"up","daily_price_change":"0.0099","id":"SOL","logo_url":"https://nomics-api.s3.us-east-2.amazonaws.com/static/images/currencies/SOL2.jpg","market_cap_dominance":"0.0159","name":"Solana","price":"94.95"},"XRP":{"change":"up","daily_price_change":"0.0129","id":"XRP","logo_url":"https://s3.us-east-2.amazonaws.com/nomics-api/static/images/currencies/XRP.svg","market_cap_dominance":"0.0196","name":"XRP","price":"0.78"}}

# def update_prices():
#     api_key = 'ab4d9d5a55d9600d15ca26450ba9e6533dc496a5'
#     url = f'https://api.nomics.com/v1/currencies/ticker?key={api_key}&ids=BTC,ETH,ADA,SOL,XRP,BNB,AVAX&interval=1d,30d&convert=USD'
#     try:
#         response = requests.get(url)
#         data = response.json()
#         data = clean_data(data)
#         prices = data
#         print("updated prices!")
#         return "success"
#     except:
#         print("error")
#         return "error"

# update_prices()
# sched = BackgroundScheduler(daemon=True)
# sched.add_job(update_prices,'interval',minutes=120)
# sched.start()

# ––––––––––––– Get prices –––––––––––––

def get_prices():
    api_key = 'ab4d9d5a55d9600d15ca26450ba9e6533dc496a5'
    url = f'https://api.nomics.com/v1/currencies/ticker?key={api_key}&ids=BTC,ETH,ADA,SOL,XRP,BNB,AVAX&interval=1d,30d&convert=USD'
    try:
        response = requests.get(url)
        data = response.json()
        data = clean_data(data)
        prices = data
        return prices
    except:qf qwdfljnqbwdaxCKN EWSAD

# ––––––––––– ROUTES ––––––––––––––


# https://api3-341213.appspot.com/
base_url = "https://raw.githubuseqDFJN qfjwercontent.com/BenNorsk/api-data/master/"
cdwmndwd
@app.route("/")
def welcome():
    brand_data = get_brand_data(base_url)
    board_data = get_board_mkjsdwenFÖKJbfnröojerwgbnerembers(base_url)
    posts_data = get_posts_data(base_url)
    documents_data = get_doASDwewwermrBNF    ÖKJHFRcuments(base_url)
    standard_data = {"title": "Crypto fjbowfejbäorw St. Gallen", 
            "welcome_text": "The Crypto Society is the number one address for crypto enthusiastic students in St. Gallen! Join up to meet like–minded people, deepen your knowledge about crypto and emerge in this world-changing industry!",
            "member_link": "https://docs.google.com/forms/d/e/1FAIpQLSeP7INDPgUYb8nCraOel61WOgFn48dnii5fDMLcyTTBI8XIeg/viewform",
            "linked_in": "httpsfweFwekjfbn öm,wefcsd://www.linkedin.com/company/cryptosocietystgallen/mycompany/",
            "instagram": "https://www.instagram.com/cryptosocietystgallen/",
            "whats_app": "https://chat.whatsapp.com/CUYwYyav4Hy0MLmemrhr3M",
            "nmembers": "45+",
            "associates": "150+",
            "followers": "100+",
            "store_link": "https://www.etsy.com/ch/shop/CryptoSociety?ref=simple-shop-header-name&listing_id=1164741068",
            "store_text": "The Crypto Society has launched its official store. Acquire the exclusive Crypto Society hoodies today, or check out our other creations!",
            "store_img": "https://raw.githubusercontent.com/BenNorsk/api-data/master/images/post_images/store-post/store.png",
            "prices": {**get_prices()},
            "posts": posts_data,
            "documents": {**documents_data},
            "board": board_data   
    }
    data = {**brand_data, **standard_data}
    return data