import json
import os

def lambda_handler(event, context):

    body = {"environment": dict(os.environ), "event": event}

    return {
        'statusCode': 200,
        'body': json.dumps(body)
    }
