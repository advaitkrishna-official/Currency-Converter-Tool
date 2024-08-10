#https://www.youtube.com/watch?v=zT7niRUOs9o&t=86s
import requests
API_KEY = 'fca_live_BS6s6h29FXjzt5rDlZfeS5DpJnc4PK2PJrY17Qkj'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "CAD", "EUR", "AUD", "CNY"]

def coverts_currency(base):
    currencies = ",".join(CURRENCIES)
    url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
    try:
        response = requests.get(url)
        data = response.json()
        return data["data"]
    except Exception as e:
        print(e)
        return None 

while True:    
    base = input("Enter a currency that you would like to convert(q to quit)").upper()
    if base =="Q":
        break
    data = coverts_currency(base)
    if not data:
        continue

    del data[base]
    for ticker, value in data.items():
        print(f"{ticker} = {value}")
