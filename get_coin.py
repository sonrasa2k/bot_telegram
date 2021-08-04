import requests
class Get_Coin:
    def __init__(self):
        self.coin = 0
        self.headers = {
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
    def get_all(self):
        api_url = 'http://api.coincap.io/v2/assets'
        data = requests.get(api_url,self.headers).json()['data']
        print(data)
        list_name = []
        list_gia = []
        list_gia_thap = []
        list_chenh_lech_gia = []
        for i in data:
            list_name.append(i['name'])
            list_gia.append(i['priceUsd'])
            list_gia_thap.append(i['vwap24Hr'])
            list_chenh_lech_gia.append(i['changePercent24Hr'])
        text = "Giá Thị Trường Tiền Điện Tử Hiện Tại:\n" \
               "Rank| Tên | Giá Hiện Tại | Thấp Nhất 24 | Tỷ lệ chênh lệch\n"
        for i in range(0,len(list_name)):
            text = text + str(i+1)+" | {0} | {1} | {2} | {3}\n".format(list_name[i],round(float(list_gia[i]),2),round(float(list_gia_thap[i]),2),round(float(list_chenh_lech_gia[i]),2))
        return text
    def get_by_name(self,name):
        api_url = 'http://api.coincap.io/v2/assets'
        data = requests.get(api_url,headers=self.headers).json()['data']
        print(data)
        for i in data:
            if name in i['id'] or name in i['name'] or name in i['symbol']:
               text = "Giá Thị Trường Đồng {0} Hiện Tại: \n" \
                      "Rank: {1}\n" \
                      "Name: {2}\n" \
                      "Giá Hiện Tại: {3}\n" \
                      "Giá Thấp Nhất 24h: {4}\n" \
                      "Tỷ Lệ Chênh Lệch 24h: {5}".format(
                   i['name'],i['rank'],i['name'],i['priceUsd'],i['vwap24Hr'],i['changePercent24Hr']
               )
               return text
        return "Vui lòng nhập đúng tên loại tiền hoặc viết tắt của tên loại tiền"
if __name__ == '__main__':
    coin = Get_Coin()
    print(coin.get_by_name("BTC"))