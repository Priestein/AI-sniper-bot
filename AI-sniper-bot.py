import requests
import time
from sklearn.linear_model import LinearRegression  # Simple AI for price prediction
import numpy as np

# API endpoint for BTC price (using CoinGecko)
API_URL = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"

def get_btc_price():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()['bitcoin']['usd']
    return None

def predict_future_price(prices):
    # Simple linear regression AI model
    X = np.array(range(len(prices))).reshape(-1, 1)
    y = np.array(prices)
    model = LinearRegression().fit(X, y)
    next_x = np.array([[len(prices)]])
    return model.predict(next_x)[0]

def sniper_alert(threshold=50000, interval=60):
    prices = []
    while True:
        price = get_btc_price()
        if price:
            prices.append(price)
            if len(prices) > 5:  # Train on at least 5 data points
                predicted = predict_future_price(prices[-5:])
                print(f"Current BTC: ${price:.2f} | Predicted Next: ${predicted:.2f}")
                if price < threshold:
                    print("ALERT: BTC below threshold! Time to snipe.")
        time.sleep(interval)

if __name__ == "__main__":
    sniper_alert()  # Customize threshold and interval