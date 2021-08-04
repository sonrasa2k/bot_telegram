import requests
class Get_Coin:
    def __init__(self):
        self.coin = 0
    def get_all(self):
        api_url = 'http://api.coincap.io/v2/assets'
        data = requests.get(api_url).json()['data']
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
        data = requests.get(api_url).json()['data']
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
    print(coin.get_all())