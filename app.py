from flask import Flask
import requests
import json
import os
from module import clean_data
app = Flask(__name__)

@app.route('/prices')
def prices():
    api_key = os.environ["NOMICS_API_KEY"]
    url = f'https://api.nomics.com/v1/currencies/ticker?key={api_key}&ids=BTC,ETH,ADA,SOL,XRP,BNB,AVAX&interval=1d,30d&convert=CHF'
    try:
        response = requests.get(url)
        data = response.json()
        data = clean_data(data)
        return data
    except:
        return "error"
  
@app.route('/greet')
def say_hello():
  return 'Hello from Server'