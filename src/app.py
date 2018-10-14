from __future__ import print_function # Python 2/3 compatibility
import boto3
import json
import decimal
from boto3.dynamodb.conditions import Key, Attr

# Helper class to convert a DynamoDB item to JSON.
class DecimalEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, decimal.Decimal):
            if o % 1 > 0:
                return float(o)
            else:
                return int(o)
        return super(DecimalEncoder, self).default(o)

dynamodb = boto3.resource('dynamodb', region_name='us-east1', endpoint_url="http://localhost:8000")

table = dynamodb.Table('users')

print("users")

#response = table.query(
 #   KeyConditionExpression=Key('id').eq(0)
response = table.scan()

for i in response['Items']:
    print(i['id'], ":", i['username'], ":", i['email'])