import time
import json
import schedule
import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5144241796:AAFjDNg6aBthGVhcLlzHgAXz6lyAIRGPWYM'
    bot_chatID = '-236624266'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def dexreport():
    page = requests.get("https://api.dexscreener.io/latest/dex/pairs/cronos/0xc924da29d37f3b8c62c4c3e4e6958bf2b5ebf677", verify=False)
    parsed = json.loads(page.content)
    data = parsed["pair"]["priceUsd"]
    my_message = "MSHARE/MMF: ${} USD".format(data)
    return my_message

def coingeckoreport(coin, name):
    page = requests.get("https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd".format(coin))
    parsed = json.loads(page.content)
    data = parsed[coin]["usd"]
    my_message = "{}: ${} USD".format(name, data)
    return my_message
   
## schedule.every().day.at("12:00").do(report)
messageList = ["Current Prices Of:"];
messageList.append(dexreport())
messageList.append(coingeckoreport("bitcoin", "Bitcoin"))
messageList.append(coingeckoreport("crypto-com-chain", "Cronos"))
schedule.every(30).minutes.do(telegram_bot_sendtext, '\n'.join(str(s) for s in messageList))

while True:
    schedule.run_pending()
    time.sleep(1)