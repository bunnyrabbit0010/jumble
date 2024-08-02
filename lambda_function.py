import json
from src import generate

print('Loading function')


def lambda_handler(event, context):
    # Assume it is a GET Call
  
    generator = generate.Generator() 
    result = generator.getJumbledWords()
    
    return {
        'statusCode': 200,
        'body': result
    }
   

