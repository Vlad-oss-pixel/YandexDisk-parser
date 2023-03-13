import requests
import random
import multiprocessing
import sys
import time
from colorama import init
init()
from colorama import Fore, Back, Style


symbol_list = list('abcdefghiklmnopqrstvxyzABCDEFGHIKLMNOPQRSTVXYZ1234567890') #abcdefghiklmnopqrstvxyzABCDEFGHIKLMNOPQRSTVXYZ
params = None
TOKEN = 'AQAAAAAz55vbAAc-fohhPDQSvU5kroy21-HguNA'
headers = {'Content-Type': 'application/json', 
'Accept': 'application/json', 
'Method': 'POST', 
'origin': 'https://disk.yandex.ru',
'pragma': 'no-cache',
'referer': 'https://disk.yandex.ru/',
'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20120101 Firefox/33.0',
'cookie':'ctrl+C ctrl+V'} # You cookie 
url = 'https://disk.yandex.ru/d/{}'
err = 0
ok = 0
while True:
    tok = ''
    for i in range(14): #14
        tok += random.choice(symbol_list)
    
    resp = requests.get(url.format(tok), headers=headers, params = params)

    if resp.status_code == 200:
        file = open("search.txt", "a")
        file.write(f'URL: {resp.url}, Status code: {resp.status_code}\n')
        file.close()
        ok += 1
 
    if resp.status_code == 404:
        err += 1

    print(Fore.RED + f'\rError: {err}', Fore.GREEN + f'Search: {ok}', end='')

    #time.sleep(1)