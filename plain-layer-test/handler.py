import json
import sys

sys.path.insert(1, "/opt")

# Change to True to toggle a change that depends on a change
# to the lambda layer for this function
from hello_layer import layer_function

INCLUDE_CHANGE = False
if INCLUDE_CHANGE:
    from hello_layer import layer_function_two


def hello(event, context):
    strs = [
        layer_function(),
    ]

    if INCLUDE_CHANGE:
        strs.append(layer_function_two())

    msg = " and ".join(strs)
    body = {
        "message": f"Go Serverless v3.0! Your function executed successfully with {msg}!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
