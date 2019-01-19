with open('../scam_addresses_etherscan.txt', 'r') as f:
    scam_ether = set([a.lower() for a in f.read().splitlines()])

with open('../scam_addresses_scamdb.txt', 'r') as f:
    scamdb = set([a.lower() for a in f.read().splitlines()])

with open('../scam_addresses_myetherwallet.txt', 'r') as f:
    scam_myetherwallet = set([a.lower() for a in f.read().splitlines()])

scam_union = scam_ether.union(scamdb).union(scam_myetherwallet)
print("UNION SIZE: %i" % len(scam_union))


with open('../scam_addresses_union.txt', 'w') as f:
    for addr in scam_union:
        if len(addr) == 42:
            f.write(addr + '\n')