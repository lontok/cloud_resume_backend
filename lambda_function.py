import json
import boto3

def lambda_handler(event, context):
    # Connect to the DynamoDB resource using boto3
    client = boto3.resource('dynamodb')
    
    # Create a reference to the DynamoDB table named 'visitor_count'
    table = client.Table('visitor_count')
    
    # Increment the visitor_count for the specific path 'index.html'
    # The 'ADD' action increments the existing value by 1
    table.update_item(
        Key={
            'path': 'index.html'  # Specifies the primary key (path) for the item to update
        },
        AttributeUpdates={
            'visitor_count': {
                'Value': 1,        # Increment visitor_count by 1
                'Action': 'ADD'    # 'ADD' will increase the current value of visitor_count
            }
        }
    )
    
    # Retrieve the updated visitor_count from the 'visitor_count' table
    response = table.get_item(
        Key={
            'path': 'index.html'  # Specifies the primary key (path) to get the item
        }
    )
    
    # Extract the visitor_count value from the response
    visitor_count = response['Item']['visitor_count']
    
    # Return the visitor_count value along with a status code and CORS headers
    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*'  # Allows requests from any origin
        },
        'body': visitor_count  # Return the visitor count as the body of the response
    }
