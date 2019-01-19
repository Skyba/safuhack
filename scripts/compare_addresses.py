
with open('../scam_addresses_etherscan.txt', 'r') as f:
    scam1 = set([a.lower() for a in f.read().splitlines()])


with open('../scam_addresses_scamdb.txt', 'r') as f:
    scam2 = set([a.lower() for a in f.read().splitlines()])

scam_union = scam1.union(scam2)
print(len(scam_union))

with open('../scam_addresses_union.txt', 'w') as f:
    for addr in scam_union:
        if len(addr) == 42:
            f.write(addr + '\n')