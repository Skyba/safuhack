import requests
import time
from bs4 import BeautifulSoup

url = "https://etherscan.io/accounts/%i?l=Phish/Hack"

to_scan=range(1,122)

with open('scam_addresses.txt', 'w') as f:
    for index in to_scan:
        print("Getting page %i" % index)
        r = requests.get(url % index)
        soup = BeautifulSoup(r.text, 'html.parser')
        tbody = soup.find_all('table')[0].tbody
        for tr in tbody.find_all('tr'):
            addr = tr.find_all('td')[1].contents[0].text.strip()
            print(addr)
            f.write(addr + '\n')
        time.sleep(0.8)
