import json

def lambda_handler(event, context):
    # Deployブランチでの変更
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
