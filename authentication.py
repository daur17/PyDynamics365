from dotenv import load_dotenv
import requests
import os

class Authentication:

    def __init__(self):
        # load env vars
        load_dotenv('.env')

        # set attrs
        self.tenant_id = os.getenv('TENANT_ID')
        self.client_id = os.getenv('CLIENT_ID')
        self.client_secret = os.getenv('CLIENT_SECRET')
        self.grant_type = os.getenv('GRANT_TYPE')
        self.resource = os.getenv('RESOURCE')

    def get_access_token(self):

        response = requests.post(os.getenv('LOGIN_URL'), data = {
            'tenant_id': self.tenant_id,
            'client_id': self.client_id,
            'client_secret': self.client_secret,
            'grant_type': self.grant_type,
            'resource': self.resource
        }).json()

        return (response['token_type'], response['access_token'])