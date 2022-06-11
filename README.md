# DexScreenerBot
A script that gets data of defi crypto pairs from dexscreener, and sends it to a telegram channel.

### Sample pair.txt file:

![image](https://user-images.githubusercontent.com/33192754/173190051-3ccbb45f-4f06-442e-90de-2a6de78ed251.png)

- If a line contains a dexscreener pair code, the script will print its price and 24hr changes.
- If a ", i" is appended to the end of the pair code, the pair will be inversed (e.g. BTC/USD to USD/BTC)
- Otherwise, print normally.

Script is regularly run on AWS Lambda, scheduled through EventBridge (Cloudwatch Events).

Data is sent every 30 minutes to https://t.me/DegenAlerts.

Powered by https://docs.dexscreener.com/.
