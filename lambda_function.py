import json

print('loading function')


def lambda_handler(event, context):
    print(event)
    print(context)
    print(2 + 2)
    print('HELLO WORLD !!!')
