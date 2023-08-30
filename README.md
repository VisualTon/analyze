## Transaction Data Analyze

This repository contains code that utilizes the [TON API](https://tonapi.io/) to retrieve transaction data and process it accordingly.

## Features

- Fetch transaction data using the TON API's transaction endpoint.
- Identify and differentiate transactions involving TON, Jetton, and NFTs.
- Display relevant transaction details such as sender, receiver, amount, asset type, status, and confirmation time.

## Challenges

1. **False Status for Successful Transactions:** In some cases, even though a transaction is successful, the status is incorrectly marked as "false".

## Usage

1. **Obtain an API Key**: Before using the script, you need to obtain an API key for the custom readable address API. This key will be used to retrieve human-readable addresses for enhanced readability in the transaction details.

2. **Update API Key**: In the `VisualTon.py` file, locate the line that says `'YOUR_API_KEY'` and replace it with your actual API key.

3. **Run the Script**

4. **Enter Transaction ID**: The script will prompt you to enter the transaction ID (in hexadecimal format) that you want to process. Provide the transaction ID and press Enter.

5. **View Transaction Details**: The script will fetch transaction data from the TON blockchain API and process it. It will display detailed information about the transaction, including:
- Sender Address: The address of the sender (originator) of the transaction.
- Receiver Address: The address of the receiver (destination) of the transaction.
- Amount: The amount of the asset being transferred in the transaction and the type of asset being transferred (e.g., TON, Jetton, NFT).
- Status: The status of the transaction (Success or Failure).
- Confirmation Time: The date and time when the transaction was confirmed.

