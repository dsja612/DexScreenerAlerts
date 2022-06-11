import config
import json
import requests
import time

def telegram_bot_sendtext(bot_message):

    send_text = 'https://api.telegram.org/bot' + config.bot_token + '/sendMessage?chat_id=' + config.bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def dexreport(link, inverse=False):
    page = requests.get("https://api.dexscreener.io/latest/dex/pairs/{}".format(link), verify=False)
    parsed = json.loads(page.content)
    name = ""
    price = 0
    baseToken = parsed["pair"]["baseToken"]["symbol"]
    quoteToken = parsed["pair"]["quoteToken"]["symbol"]

    if inverse:
        name = "{}/{}".format(quoteToken, baseToken)
        price = 1 / float(parsed["pair"]["priceNative"])
        my_message = "{}: {:.2f} {} ".format(name, price, baseToken)
        return my_message
    else:
        name = "{}/{}".format(baseToken, quoteToken)
        price = parsed["pair"]["priceUsd"]
        change = parsed["pair"]["priceChange"]["h24"]
        my_message = "{}: ${} USD ({}% in 24H)".format(name, price, change)
        return my_message

def executeBot():
    messageList = []

    with open('pairs.txt') as f:
        lines = list(map(lambda line: line.strip('\n').split(","), f.readlines()))
        for line in lines:
            print(line)
            if (line[0].find('/') != -1): # Check if its a crypto pair
                messageList.append(dexreport((line[0]), True if (len(line) == 2) else False))
            else:
                messageList.append(line[0])
    
    telegram_bot_sendtext('\n'.join(str(s) for s in messageList))