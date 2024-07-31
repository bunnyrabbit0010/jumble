import json
from generate import Generator

print('Loading function')


def lambda_handler(event, context):
    # Assume it is a GET Call
  
    generator = Generator() 
    result = generator.getJumbledWords()
    
    return {
        'statusCode': 200,
        'body': result
    }
   

