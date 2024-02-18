#Make POST,GET,PUT,DELETE
import json
import requests

# Http Requests - Generic Functions

#1. Get data:
def get_data(url,headers):
    response=requests.get(url=url,headers=headers)
    return response

#2. Post data:
def post_data(url,headers,payload):
    response = requests.post(url=url,headers=headers,data=json.dumps(payload))
    return response

#3. Put data:
def put_data(url,headers,payload):
    response = requests.put(url=url, headers=headers,data=json.dumps(payload))
    return response

#4. Delete data
def delete_data(url,headers):
    response = requests.delete(url=url, headers=headers)
    return response