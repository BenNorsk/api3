from flask import Flask
import requests
import json
import os
from module import clean_data, get_brand_data
from board_member_data import get_board_members
from posts_data import get_posts_data
from document_data import get_documents

app = Flask(__name__)
base_link = "https://raw.githubusercontent.com/BenNorsk/api-data/master/"

@app.route("/")
def welcome():
    data = {"title": "Crypto Society St. Gallen", 
            "welcome_text": "The Crypto Society is a newly founded assosciation by students in St. Gallen. We strive to bring the emerging universe of cryptocurrencies closer to the students in St. Gallen. As laid out in our Whitepaper, we want to build a community and serve as a hub for all the local crypto-enthusiastic students! We warmly welcome anyone who wants to join the Crypto Society as a member, and would be happy to receive your application!",
            "member_link": "https://docs.google.com/forms/d/e/1FAIpQLSeP7INDPgUYb8nCraOel61WOgFn48dnii5fDMLcyTTBI8XIeg/viewform",
            "linked_in": "https://www.linkedin.com/company/cryptosocietystgallen/mycompany/",
            "instagram": "https://www.instagram.com/cryptosocietystgallen/"
    }
    return data



@app.route('/brand')
def brand():
    return get_brand_data(base_link)

@app.route('/prices')
def prices():
    api_key = '1b4000986ffd8d4f14e151e57b7dae0fbbb6e9c9'
    url = f'https://api.nomics.com/v1/currencies/ticker?key={api_key}&ids=BTC,ETH,ADA,SOL,XRP,BNB,AVAX&interval=1d,30d&convert=CHF'
    try:
        response = requests.get(url)
        data = response.json()
        data = clean_data(data)
        return data
    except:
        return "error"
  
@app.route('/board-members')
def board_members():
  return get_board_members(base_link)

@app.route("/posts")
def posts():
    return get_posts_data(base_link)

@app.route("/documents")
def documents():
    return get_documents(base_link)