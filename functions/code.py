import json

from util import execute_and_capture_output


def lambda_handler(event, context):
    code = event["queryStringParameters"]["code"]
    output = execute_and_capture_output(code)

    print(f"Ran code {code} and got output {output}")

    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps(output),
    }
