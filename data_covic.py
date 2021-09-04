import requests
class DataCovicVn:
    def __init__(self):
        self.so_ca_nhiem = 0
    def get_data_covic_vn(self):
        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.google.com/',
            'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        }
        try:
            response = requests.get('https://ncov.moh.gov.vn/', headers=headers, verify=False)
            raw_data = response.text #nguyeen cunm nay la 1 string
            so_ca_nhiem = raw_data.split('Số ca nhiễm<br> <span class="font24">')[1].split('</span>')[0]
            dang_dieu_tri = raw_data.split('Đang điều trị<br> <span class="font24">')[1].split('</span>')[0]
            khoi = raw_data.split('Khỏi<br> <span class="font24">')[1].split('</span>')[0]
            tu_vong = raw_data.split('Tử vong<br> <span class="font24">')[1].split('</span>')[0]
        except:
            return {"code":402,"msg":"Khong lay duoc data"}
        return {"code":200,"so_ca_nhiem":so_ca_nhiem,"dang_dieu_tri":dang_dieu_tri,"khoi":khoi,"tu_vong":tu_vong,"msg":"OKE"}

if __name__ == '__main__':
    covicvn = DataCovicVn()
    print(covicvn.get_data_covic_vn())

