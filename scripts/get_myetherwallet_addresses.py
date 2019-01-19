import json

with open('../myetherwallet-darklist.json') as f:
    addresses = [record['address'] for record in json.load(f)]

with open('../scam_addresses_myetherwallet.txt', 'w') as f:
    for addr in addresses:
        f.write(addr + '\n')