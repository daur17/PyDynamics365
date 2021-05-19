from authentication import Authentication
from dotenv import load_dotenv
import requests
import os

# load env variables
load_dotenv('.env')

class GetData:

    def __init__(self, query):
        self.query = query

    def get_data(self):
        # get access token
        auth = Authentication()
        type, token = auth.get_access_token()
        bearer = f'{type} {token}'

        data = requests.get(f'{auth.resource}/data/{self.query}', headers = {'Authorization': bearer})

        return data.json()

cust_account = 'CLI_000160'
odata_query = f"Customers?$filter=CustomerAccount eq '{cust_account}'&$select=CustomerAccount,Name,DeliveryAddressStreet,SalesMemo"
x = GetData(odata_query)

for customer in x.get_data()['value']:
    for key, value in customer.items():
        print(f'{key}\n      {value}')