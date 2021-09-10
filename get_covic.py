import requests
class Covic:
    def __init__(self):
        self.coviec = 0
    def covic_vn(self):
        try:
            data = requests.get('https://static.pipezero.com/covid/data.json').json()
            data_vn = data["total"]["internal"]
            scn = data_vn["cases"]
            chet = data_vn["death"]
            scdt = data_vn["treating"]
            khoi = data_vn["recovered"]
            data_vn_today = data["today"]["internal"]
            scn_today = data_vn_today["cases"]
            khoi_today = data_vn_today["recovered"]
            chet_today = data_vn_today["death"]
            return {"code":200,"scn":scn,"scdt":scdt,"khoi":khoi,"chet":chet,"scn_today":scn_today,"khoi_today":khoi_today,"chet_today":chet_today,"msg":"OKE"}
        except:
            return {"code":0,"msg":"khong lay dc data"}

    def covic_tinnhanh(self):

        headers = {
            'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'sec-ch-ua': '^\\^',
            'sec-ch-ua-mobile': '?0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.164 Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Sec-Fetch-Site': 'cross-site',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-User': '?1',
            'Sec-Fetch-Dest': 'document',
            'Referer': 'https://www.google.com/',
            'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
        }
        try:
            response = requests.get('https://ncov.moh.gov.vn/', headers=headers, verify=False).text
            content = response.split('<div class="timeline-content">')[1]
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(content).get_text()
            return {"code":200,"content":soup}
        except:
            return {"code":0}
    def covic_diaphuong(self,name):
        data = requests.get('https://static.pipezero.com/covid/data.json').json()
        data_tinh = data["locations"]
        if name == "all":
            return data_tinh
        else:
            name = name.capitalize()
            for data in data_tinh:
                if name in data["name"]:
                    return data
            return {"name":"00"}
if __name__ == '__main__':
    c = Covic()
    print(c.covic_diaphuong("h"))


