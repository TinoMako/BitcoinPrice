import requests 
import time
import json

# global variables

api_key = '81a33afe-4fe3-47b4-82cd-23e6fbfa03e'
bot_token = '1634436888:AAHQwPKNzjoaGfd1ErAi9EM4gBzqIfsN2q'
chat_id = '73061548'
threshold = 30000
time_interval = 0.5 * 60 # in seconds

def get_btc_price():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': api_key
    }
    # make a request to the coin market API
    response = requests.get(url, headers=headers)
    response_json = response.json()

    # extract the bitcoin price from the json data
    btc_price = response_json['data'][0]
    return btc_price['quote']['USD']['price']

#Function to send message through telegram

def send_message(chat_id, msg):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={msg}"

 # send the msg
    requests.get(url)   


# The Main function

def main():
    price_list = []

    #infinite loop
    while True:
        price = get_btc_price()
        price_list.append(price)

    #If the price falls below threshhold, send an immediate message

        if price < threshold:
            send_message(chat_id=chat_id, msg=f'BTC Price Drop Alert: {price}')

# send last 4 btc price
        if len(price_list) >= 10:
            send_message(chat_id=chat_id, msg=price_list)
            # empty the price_list
            price_list = []

# fetch the price for every dash minutes
        time.sleep(time_interval)

 # fancy way to activate the main() function
if __name__ == '__main__':
    main()       


