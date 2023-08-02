import json


def lambda_handler(event, context):
    code = event.get('code')

    if not code:
        if 'queryStringParameters' in event:
            code = event['queryStringParameters']['code']

    response = {
        'statusCode': 200,
        'headers': {'Content-Type': 'application/json'},
        'body': {}
    }

    try:
        exec(code)
        response['body']['message'] = 'success!'
    except Exception as e:
        response['statusCode'] = 400
        response['body']['message'] = str(e)

    response['body'] = json.dumps(response['body'])

    return response
