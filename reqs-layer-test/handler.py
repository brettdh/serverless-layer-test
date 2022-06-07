import json

import arrow

# Change to True to toggle a change that depends on a change
# to the lambda layer for this function
INCLUDE_CHANGE = False

if INCLUDE_CHANGE:
    import pendulum


def hello(event, context):
    strs = [
        f"(arrow) {arrow.get()}",
    ]
    if INCLUDE_CHANGE:
        strs.append(f"(pendulum) {pendulum.get()}")

    msg = ", ".join(strs)
    body = {
        "message": f"Go Serverless v3.0! Your function executed successfully at {msg}!",
        "input": event,
    }

    return {"statusCode": 200, "body": json.dumps(body)}
