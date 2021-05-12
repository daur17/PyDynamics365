import requests
import os
from dotenv import load_dotenv

# load env vars
load_dotenv('.env')

# get token request
response = requests.post(os.getenv('LOGIN_URL'), data = {
    'tenant_id': os.getenv('TENANT_ID'),
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
    'grant_type': os.getenv('GRANT_TYPE'),
    'resource': os.getenv('RESOURCE')
}).json()

def get_access_token():
    return (response['token_type'], response['access_token'])