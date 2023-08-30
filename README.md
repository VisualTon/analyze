# My Transaction Data Processing Project

This folder contains code that utilizes the [TON API](https://tonapi.io/) to retrieve transaction data and process it accordingly.

## Features

- Fetch transaction data using the TON API's transaction endpoint.
- Identify and differentiate transactions involving TON, Jetton, and NFTs.
- Display relevant transaction details such as sender, receiver, amount, asset type, status, and confirmation time.

## Challenges

1. **Hashed Addresses:** The sender and receiver addresses in the fetched data are represented as hexadecimal values, making them difficult to interpret.

2. **False Status for Successful Transactions:** In some cases, even though a transaction is successful, the status is incorrectly marked as "false".
