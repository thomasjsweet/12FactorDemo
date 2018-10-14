from __future__ import print_function # Python 2/3 compatibility
import boto3

dynamodb = boto3.resource('dynamodb', region_name='us-east-1', endpoint_url="http://localhost:8000")


table = dynamodb.create_table(
    TableName='users',
    KeySchema=[
        {
            'AttributeName': 'id',
            'KeyType': 'HASH'  #Partition key
        },
        {
            'AttributeName': 'username',
            'KeyType': 'RANGE'  #Sort key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'id',
            'AttributeType': 'N'
        },
                {
            'AttributeName': 'username',
            'AttributeType': 'S'
        },
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    }
)

print("Table status:", table.table_status)