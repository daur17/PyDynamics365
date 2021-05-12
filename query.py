from authentication import get_access_token
from dotenv import load_dotenv
import requests
import os

# load env variables
load_dotenv('.env')

# get access token
type, token = get_access_token()
bearer = f'{type} {token}'

# customer url
cust_account = 'CLI_000160'
customers_url = f"{os.getenv('RESOURCE')}/data/Customers"
customer_url = f"{os.getenv('RESOURCE')}/data/Customers?$filter=CustomerAccount eq '{cust_account}'&$select=CustomerAccount,Name,DeliveryAddressStreet"

# single customer
customer_data = requests.get(customer_url, headers = {'Authorization': bearer})

for customer in customer_data.json()['value']:
    for key, value in customer.items():
        print(f'{key}\n      {value}')