import json


def hello(event, context):
    body = {
        "message": " first function executed successfully!"
    }

    return {"statusCode": 200, "body": json.dumps(body)}
