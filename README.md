# YandexDisk-parser
This script is used to search for open links to Yandex.Disk, where people can store their files. The script generates a random combination of characters (characters can be from a list that is provided in the code), and then creates a GET request to an address consisting of this combination of characters. If the requested page exists, the Yandex server.Disk will return the 200 code, and the script will save the URL in a file search.txt . If the page does not exist, the server will return the 404 code, and the script will increase the value of the error counter.

This process is repeated indefinitely using the while True loop. Whenever a new open link is successfully found, the counter will increase by one, and the script will continue searching until the user interrupts the program manually.

The script uses the requests and colorama libraries to send requests and format output to the console. Headers contain information about the user, which is usually used for authentication when accessing the Yandex.Disk API. In this case, this information is necessary so that the script can simulate user behavior.
# Donate:

BTC: 15HyEfPsYHAgn27XkbcVErwpii6kofJAtq

ETH: 0x95994147DCad49420f0b7601a888a2B002dA021a

XRP: r9WuSebiVCWxtZ3xqCmsJ2E5Cc4usfkYHy

