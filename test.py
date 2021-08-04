import requests

headers = {
    'authority': 'api.coincap.io',
    'cache-control': 'max-age=0',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    'sec-ch-ua-mobile': '?0',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'sec-fetch-site': 'none',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-user': '?1',
    'sec-fetch-dest': 'document',
    'accept-language': 'vi,en-US;q=0.9,en;q=0.8',
    'cookie': '_uetvid=6c0eefe0ed7311eb92674f6fdd3e98a3; _ga=GA1.1.330530233.1627236556; _ga_MF6R5QRX6K=GS1.1.1627245117.2.0.1627245117.0',
    'if-none-match': 'W/^\\^97fd-ozOCjGsQgQ3ALxdkXzeh3gjy7ak^\\^',
}

response = requests.get('https://api.coincap.io/v2/assets', headers=headers)
print(response.json()['data'])