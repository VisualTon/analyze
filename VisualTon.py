import requests
from datetime import datetime

def process_transaction(data):
    sender_address = data['account']['address']
    decoded_op_name = data['in_msg'].get('decoded_op_name')

    if decoded_op_name == "nft_ownership_assigned":
        receiver_address = data['in_msg']['source']['address']
        amount = data['in_msg']['value']
        asset = "NFT"
    elif decoded_op_name == "jetton_notify":
        receiver_address = data['in_msg']['source']['address']
        amount = int(data['in_msg']['decoded_body'].get('amount', 0)) // 10**9
        asset = "Jetton"
    else:
        return

    status = "Success" if data['success'] else "Failure"
    confirm_time = data['utime']
    transaction_time = datetime.fromtimestamp(confirm_time).strftime('%Y-%m-%d %H:%M:%S')

    print("Sender Address:", sender_address)
    print("Receiver Address:", receiver_address)
    print(f"Amount: {amount} {asset}")
    print("Status:", status)
    print("Confirm Time:", confirm_time)

transaction_id = input()
url = f"https://tonapi.io/v2/blockchain/transactions/{transaction_id}"
headers = {
    "Authorization": "Bearer AH7TI4ESXIJRFRQAAAAJCGD7ZXOXZ75HK7VO3MP6FGW7W5PHNDEYGSPHEB22TLCIZMDRMMY"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    data = response.json()
    out_msgs = data.get('out_msgs', [])

    if out_msgs:
        sender_address = data['account']['address']
        receiver_address = data['out_msgs'][0]['destination']['address']
        amount = int(data['out_msgs'][0]['value']) // 10**9
        asset = "TON"
        status = "Success" if data['success'] else "Failure"
        confirm_time = data['utime']
        transaction_time = datetime.fromtimestamp(confirm_time).strftime('%Y-%m-%d %H:%M:%S')

        print("Sender Address:", sender_address)
        print("Receiver Address:", receiver_address)
        print(f"Amount: {amount} {asset}")
        print("Status:", status)
        print("Confirm Time:", confirm_time)
    else:
        process_transaction(data)
else:
    print("Request failed with status code:", response.status_code)