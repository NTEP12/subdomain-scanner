#!/usr/bin/env python3
import requests
from requests.api import request

def print_banner():
        banner = '''
  _   _ _______ ______ _____  __ ___  
 | \ | |__   __|  ____|  __ \/_ |__ \ 
 |  \| |  | |  | |__  | |__) || |  ) |
 | . ` |  | |  |  __| |  ___/ | | / / 
 | |\  |  | |  | |____| |     | |/ /_ 
 |_| \_|  |_|  |______|_|     |_|____|  
 
    '''
        print(banner)
        print('Subdomain Scanner made by NTEP12, the embodiment of god.')
        print('Please enter the website you want to scan without "https://"')
print_banner()

def subf(domain_name,subd):
    discovered_subdomains = []
    print('Started scanning.')

    for subdomain in subd:
        url = f'https://{subdomain}.{domain_name}'
        try:
            requests.get(url)
            print(f'[+] {url} found.')
            discovered_subdomains.append(url)
        except requests.ConnectionError:
            pass
    with open('discovered_subdomains.txt', 'w') as f:
        for subdomain in discovered_subdomains:
            print(subdomain, file=f)
    print('\n')
    print('Thanks for using my program.')
    
if __name__ == '__main__':
    domain_name = input('Enter the domain you want to scan: ')
    print('\n')
    with open('subs.txt','r') as file:
        name = file.read()
        subda = name.splitlines()
    subf(domain_name, subda)