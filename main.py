from flask import Flask
import requests
import json
import os
from module import clean_data
app = Flask(__name__)

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
  return 'Hello from Server'