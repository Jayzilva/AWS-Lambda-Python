import json

def lambda_handler(event, context):
    # TODO implement

    count = event["stockUnits"]
    price = event["stockPrice"]
    
    
    total =  count + price
    
    return {"Total is": total}
