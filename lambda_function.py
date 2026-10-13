import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Serverless-Project-DB')

def lambda_handler(event, context):
    try:
        body = json.loads(event.get('body', '{}'))
    except Exception:
        body = {}
        
    record_id = str(uuid.uuid4())
    
    table.put_item(
        Item={
            'id': record_id,
            'message': body.get('message', 'Hello from Serverless API!')
        }
    )
    
    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'application/json'
        },
        'body': json.dumps({
            'success': True,
            'record_id': record_id,
            'status': 'Saved to Database!'
        })
    } 