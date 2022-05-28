import config
import json
import requests
import time

def telegram_bot_sendtext(bot_message):

    send_text = 'https://api.telegram.org/bot' + config.bot_token + '/sendMessage?chat_id=' + config.bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()

def dexreport(link, name):
    page = requests.get("https://api.dexscreener.io/latest/dex/pairs/{}".format(link), verify=False)
    parsed = json.loads(page.content)
    price = parsed["pair"]["priceUsd"]
    change = parsed["pair"]["priceChange"]["h24"]
    my_message = "{}: ${} USD ({}% in 24H)".format(name, price, change)
    return my_message

def executeBot():
    messageList = ["MM Finance:"];
    messageList.append(dexreport("cronos/0xc924da29d37f3b8c62c4c3e4e6958bf2b5ebf677", "MSHARE/MMF"))
    messageList.append(dexreport("cronos/0x0fcffa1ed6b91b50dc80bb652f1111464a46338f", "HKN/SVN"))
    messageList.append(dexreport("cronos/0x7444491828253452b7a933a5aa0a74b55a86cdb0", "MAD/MMF"))
    messageList.append(" ")
    time.sleep(1)
    messageList.append("DarkCrypto:");
    messageList.append(dexreport("cronos/0x9284134f3d268cdf0ef2305c9f06767e913a7ce6", "DARK/WCRO"))
    messageList.append(dexreport("cronos/0xaa0845ee17e4f1d4f3a8c22cb1e8102bacf56a77", "SKY/WCRO"))
    messageList.append(" ")
    time.sleep(1)    
    messageList.append("ToxicDeer:");
    messageList.append(dexreport("cronos/0x264f27bf0ec4fe383cfda50f1bb11588735bbe6d", "DEER/USDC"))
    messageList.append(dexreport("cronos/0x18cd20c6ca9ccfe1c8b48516e6d5e0055a0271d2", "XDSHARE/USDC"))
    messageList.append(" ")
    time.sleep(1)    
    messageList.append("Crypto:")
    messageList.append(dexreport("ethereum/0x99ac8ca7087fa4a2a1fb6357269965a2014abc35", "WBTC"))
    messageList.append(dexreport("ethereum/0x88e6a0c2ddd26feeb64f039a2c41296fcb3f5640", "WETH"))
    messageList.append(dexreport("bsc/0xff44e10662e1cd4f7afe399144636c74b0d05d80", "DOT"))
    messageList.append(dexreport("moonbeam/0x051fcf8986b30860a1341e0031e5622bd18d8a85", "ATOM"))
    messageList.append(dexreport("cronos/0xa68466208f1a3eb21650320d2520ee8eba5ba623", "CRO"))
    messageList.append(dexreport("bsc/0x0f8e31ce605f225c336dead35304d649ae8fad04", "LUNA"))
    messageList.append(dexreport("bsc/0x05faf555522fa3f93959f86b41a3808666093210", "UST"))
    
    telegram_bot_sendtext('\n'.join(str(s) for s in messageList))