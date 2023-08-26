#!/usr/bin/env python
# coding: utf-8

# In[63]:


import requests
from datetime import datetime

transaction_id = "0d90d5fc328a01b91074b8d8942be6e5b4901fe89fbcaa20667d1d0e85ca8160"

url = f"https://tonapi.io/v2/blockchain/transactions/{transaction_id}"
headers = {
    "Authorization": "Bearer AH7TI4ESXIJRFRQAAAAJCGD7ZXOXZ75HK7VO3MP6FGW7W5PHNDEYGSPHEB22TLCIZMDRMMY"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()

    sender_address = data['account']['address']
    receiver_address = data['out_msgs'][0]['destination']['address']
    amount = int(data['out_msgs'][0]['value']) // 10**9
    formatted_amount = '{:} TON'.format(amount)
    success = data['success']
    unix_timestamp = data['utime']
    
    transaction_time = datetime.fromtimestamp(unix_timestamp).strftime('%Y-%m-%d %H:%M:%S')

    print("Sender Address:", sender_address)
    print("Receiver Address:", receiver_address)
    print("Amount:", formatted_amount)
    print("Status:", "Success" if success else "Fail")
    print("Confirm Time:", transaction_time)
else:
    print("Request failed with status code:", response.status_code)

