import json
from DexScreenerBot import executeBot

def lambda_handler(event, context):
    # TODO implement
    executeBot()
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
