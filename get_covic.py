import requests
class Covic:
    def __init__(self):
        self.coviec = 0
    def covic_vn(self):
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
            response = requests.get('https://ncov.moh.gov.vn/', headers=headers,verify=False).text
            # vn = response.split('<span class="box-vn">')[1]
            so_can_nhiem_vn = response.split('Số ca nhiễm<br> <span class="font24">')[1].split('</span>')[0]
            so_ca_dang_dieu_tri =response.split('Đang điều trị<br> <span class="font24">')[1].split('</span>')[0]
            khoi = response.split('Khỏi<br> <span class="font24">')[1].split('</span>')[0]
            chet = response.split('Tử vong<br> <span class="font24">')[1].split('</span>')[0]
        except:
            return {"code":0,"msg":"error"}
        return {"code":200,"scn":so_can_nhiem_vn,"scdt":so_ca_dang_dieu_tri,"khoi":khoi,"chet":chet}
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
    def covic_diaphuong(self,text_name):
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
            text = response.split('<table id="sailorTable" class="table table-striped table-covid19">')[1].split('</section>')[0].split('<tbody>')[1].split('</tbody>')[0]
            list_tinh = text.split('<tr style="font-weight: 600" >')
            del list_tinh[0]
            list_name_tinh = []
            from bs4 import BeautifulSoup
            for tinh in list_tinh:
                list_name_tinh.append(BeautifulSoup(tinh).get_text())
            list_tinh = []
            list_scn = []
            list_scnhn = []
            list_chet = []
            print(list_name_tinh)
            for name in list_name_tinh:
                list_tinh.append(name.split('\n')[1])
                list_scn.append(name.split('\n')[2])
                list_scnhn.append(name.split('\n')[3])
                list_chet.append(name.split('\n')[4])
                text_name = text_name.title()
                if text_name in name.split('\n')[1]:
                    return {"code":200,"name_tinh":name.split('\n')[1],"scn":name.split('\n')[2],"scnhn":name.split('\n')[3],"chet":name.split('\n')[4]}
            return {"code":99,'name_tinh':list_tinh,"scn":list_scn,"scnhn":list_scnhn,"chet":list_chet}
        except:
            return {"code":0 , "msg": "error"}
if __name__ == '__main__':
    c = Covic()
    print(c.covic_diaphuong("đồng nai"))


