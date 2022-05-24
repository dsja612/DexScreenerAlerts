import json
import requests

def telegram_bot_sendtext(bot_message):
    
    bot_token = '5144241796:AAFjDNg6aBthGVhcLlzHgAXz6lyAIRGPWYM'
    bot_chatID = '-1001629434446'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def dexreport(link, name):
    page = requests.get("https://api.dexscreener.io/latest/dex/pairs/{}".format(link), verify=False)
    parsed = json.loads(page.content)
    price = parsed["pair"]["priceUsd"]
    change = parsed["pair"]["priceChange"]["h6"]
    my_message = "{}: ${} USD ({}% in 24H)".format(name, price, change)
    return my_message

# def coingeckoreport(coin, name):
#     page = requests.get("https://api.coingecko.com/api/v3/simple/price?ids={}&vs_currencies=usd".format(coin))
#     parsed = json.loads(page.content)
#     data = parsed[coin]["usd"]
#     my_message = "{}: ${} USD".format(name, data)
#     return my_message

def executeBot():
    messageList = ["Cronos Dex Pairs:"];
    messageList.append(dexreport("cronos/0xc924da29d37f3b8c62c4c3e4e6958bf2b5ebf677", "MSHARE/MMF"))
    messageList.append(dexreport("cronos/0x0fcffa1ed6b91b50dc80bb652f1111464a46338f", "HKN/SVN"))
    messageList.append(dexreport("cronos/0xaa0845ee17e4f1d4f3a8c22cb1e8102bacf56a77", "SKY/CRO"))
    messageList.append(" ")
    messageList.append("Crypto: (in USD)")
    messageList.append(dexreport("ethereum/0x99ac8ca7087fa4a2a1fb6357269965a2014abc35", "WBTC"))
    messageList.append(dexreport("ethereum/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", "WETH"))
    messageList.append(dexreport("bsc/0xff44e10662e1cd4f7afe399144636c74b0d05d80", "DOT"))
    messageList.append(dexreport("moonbeam/0x051fcf8986b30860a1341e0031e5622bd18d8a85", "ATOM"))
    messageList.append(dexreport("cronos/0xa68466208f1a3eb21650320d2520ee8eba5ba623", "CRO"))
    # messageList.append(coingeckoreport("bitcoin", "Bitcoin"))
    # messageList.append(coingeckoreport("polkadot", "Polkadot"))
    # messageList.append(coingeckoreport("cosmos", "Atom"))
    # messageList.append(coingeckoreport("matic-network", "Polygon"))
    #schedule.every(30).minutes.do(telegram_bot_sendtext, '\n'.join(str(s) for s in messageList))
    telegram_bot_sendtext('\n'.join(str(s) for s in messageList))

# while True:
#     schedule.run_pending()
#     time.sleep(1)