import requests, os
from pathlib import Path
from urllib.parse import urlencode, quote
import json
import traceback,re
class Download:
    def __init__(self, cookie = {}, path = ''):
        self.BASE_URL = "https://www.tiktok.com/node/"
        self.userAgent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/86.0.4240.111 Safari/537.36"
        )
        self.cookiess ={
            'tt_webid_v2': '6906584401044538882',
            'tt_webid': '6906584401044538882',
            'store-idc': 'alisg',
            'store-country-code': 'vn',
            '_abck': '81A3203635CAA8DB148C0B3C5B2BAE22~0~YAAQMqo3F+FAQgt5AQAA227AEwWalJrm5HY+NzI4mfkZN34Xm+Q4cJ8m8+IK+x87Qykob5gFzCGp5jP9TQtJmbld/bcFyGU04cYyNkjqPG5Nta8GUKRZxg6IAXcDP+dsCEAAfzqx33V4np/zH5bW7C3oQWH0ZgQA15XJh63JyCf4L6r0sNqUl/buDs0pYHQl4yhv6Ag6e4jQAIoTkQOuULXr0vFHfiTv9fR4KVZfSuHA91WQGmWNWSbc5gB576oiSxhlHCH8duAhpaZfUsJpNZFBtYmaQN4R97AJW/n9jRNlAFBA+cyRbb+dKv8EMCRi4waKpg/RlCBDVMM0DLmyMdW3vRAG+rWrysxxy29lmdL/wT5unRneit6U81gl//G6bEVs+v0=~-1~-1~-1',
            'passport_csrf_token_default': 'd213ac9db5f49b56f1d6e6fae18678b6',
            'passport_csrf_token': 'd213ac9db5f49b56f1d6e6fae18678b6',
            'tt_csrf_token': 'PB7J82XvOaH4LRCGmzXlorGN',
            'R6kq3TV7': 'AKPdLAJ7AQAA38ILzvGUijk_Uri-ymcwZvXoJuMaCwmvgZYNQmCA58n3pTLE^|1^|0^|854df14c09f7e2519acc2f0c80c256db20191afe',
            'passport_auth_status': '9f3ce415262d948f5e8297ecc0137b5b^%^2C',
            'passport_auth_status_ss': '9f3ce415262d948f5e8297ecc0137b5b^%^2C',
            'sid_guard': 'db89d4ee9c4a56749ff4547a60e26716^%^7C1627829148^%^7C5183999^%^7CThu^%^2C+30-Sep-2021+14^%^3A45^%^3A47+GMT',
            'uid_tt': '5a1d9d5f41f64aff799f10c82f263954ae12d9df688a053fdd597ed880b9e23f',
            'uid_tt_ss': '5a1d9d5f41f64aff799f10c82f263954ae12d9df688a053fdd597ed880b9e23f',
            'sid_tt': 'db89d4ee9c4a56749ff4547a60e26716',
            'sessionid': 'db89d4ee9c4a56749ff4547a60e26716',
            'sessionid_ss': 'db89d4ee9c4a56749ff4547a60e26716',
            'cmpl_token': 'AgQQAPPdF-RMpYr-erL5Odk4xbiE2CQcv4AOYP5jsg',
            'odin_tt': '8a12be3496469953c19d13cf7c6d61a3296f08f209bc43e7dbbd155ef2d108f9796c320dbadfc7a4dc6f2d3b9e4aaee4adc3caaf5a68eaeb7e83bc909694035259b044582cf74d6b55bea63f5533f394',
            'ttwid': '1^%^7C31yObapDPsmlj3wjaLTy3vG_v6bNeW_cnxw847CapnQ^%^7C1627841642^%^7C50abc621b0b394f7f4f6088110ec4aba1b3b19753f0fb5408518f7a541896d5c',
        }
        self.browser_language = 'vi'
        self.browser_platform = 'Win32'
        self.browser_name = "Mozilla"
        self.browser_version = "5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36"
        self.timezone_name = "Asia/Bangkok"
        self.width = "1920"
        self.height = "1080"
        self.cookie = cookie
        self.path = path
        try:
            path = str(Path().absolute())
            if not os.path.exists(self.path):
                os.makedirs(self.path)
        except:
            pass
    def get_user_by_html(self,url):
        r = requests.get(
            url,
            headers={
                'authority': 'www.tiktok.com',
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
                'cookie': 'tt_webid_v2=6906584401044538882; tt_webid=6906584401044538882; store-idc=alisg; store-country-code=vn; s_v_web_id=verify_kmw96uek_8lofr5Vk_1WgP_4VT1_8qhK_F7weuL2RdECF; _abck=81A3203635CAA8DB148C0B3C5B2BAE22~0~YAAQMqo3F+FAQgt5AQAA227AEwWalJrm5HY+NzI4mfkZN34Xm+Q4cJ8m8+IK+x87Qykob5gFzCGp5jP9TQtJmbld/bcFyGU04cYyNkjqPG5Nta8GUKRZxg6IAXcDP+dsCEAAfzqx33V4np/zH5bW7C3oQWH0ZgQA15XJh63JyCf4L6r0sNqUl/buDs0pYHQl4yhv6Ag6e4jQAIoTkQOuULXr0vFHfiTv9fR4KVZfSuHA91WQGmWNWSbc5gB576oiSxhlHCH8duAhpaZfUsJpNZFBtYmaQN4R97AJW/n9jRNlAFBA+cyRbb+dKv8EMCRi4waKpg/RlCBDVMM0DLmyMdW3vRAG+rWrysxxy29lmdL/wT5unRneit6U81gl//G6bEVs+v0=~-1~-1~-1; passport_csrf_token_default=d213ac9db5f49b56f1d6e6fae18678b6; passport_csrf_token=d213ac9db5f49b56f1d6e6fae18678b6; MONITOR_WEB_ID=6906584401044538882; tt_csrf_token=PB7J82XvOaH4LRCGmzXlorGN; R6kq3TV7=AKPdLAJ7AQAA38ILzvGUijk_Uri-ymcwZvXoJuMaCwmvgZYNQmCA58n3pTLE^|1^|0^|854df14c09f7e2519acc2f0c80c256db20191afe; csrf_session_id=f26a311997554ebeb59b71aba231fd84; passport_auth_status=9f3ce415262d948f5e8297ecc0137b5b^%^2C; passport_auth_status_ss=9f3ce415262d948f5e8297ecc0137b5b^%^2C; sid_guard=db89d4ee9c4a56749ff4547a60e26716^%^7C1627829148^%^7C5183999^%^7CThu^%^2C+30-Sep-2021+14^%^3A45^%^3A47+GMT; uid_tt=5a1d9d5f41f64aff799f10c82f263954ae12d9df688a053fdd597ed880b9e23f; uid_tt_ss=5a1d9d5f41f64aff799f10c82f263954ae12d9df688a053fdd597ed880b9e23f; sid_tt=db89d4ee9c4a56749ff4547a60e26716; sessionid=db89d4ee9c4a56749ff4547a60e26716; sessionid_ss=db89d4ee9c4a56749ff4547a60e26716; passport_fe_beating_status=true; odin_tt=e58a33322aa71b57c4436a6ab3df932a5bb799bc53a71ed4e15eb70bf6f795feb391a7c9bec41d827ab724208340f0bf3f056d426eceb1b3d87f9eb59f4f7daafb6fb1c2b2de5223f3cb0fe8ec840cee; cmpl_token=AgQQAPPdF-RMpYr-erL5Odk4xbiE2CQcv4AOYP5iFg; ttwid=1^%^7C31yObapDPsmlj3wjaLTy3vG_v6bNeW_cnxw847CapnQ^%^7C1627835675^%^7Ce1df72702873e335a4623d918b0af93ccff0281bf1ee4cf70d829913e57f4a82',
            }
        )
        t = r.text
        j_raw = t.split('crossorigin="anonymous">')[1].split('</script>')[0]
        # data = json.loads(j_raw)
        # j_raw = t.split(
        #     '<script id="__NEXT_DATA__" type="application/json" crossorigin="anonymous">'
        # )[1].split("</script>")[0]

        data = json.loads(j_raw)["props"]["pageProps"]
        return data
    def downloadVideo(self, url, file_name = 'video'):
        res = requests.get(
            url,
            headers={
                    "Referer": "https://www.tiktok.com/",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                },
            cookies=self.cookie
        )
        with open(self.path+"/{}.mp4".format(file_name), 'wb') as out:
            out.write(res.content)


    def downloadVideoNoWatermarkByID(self, id, file_name = 'video'):
        api = 'https://toolav.herokuapp.com/id/?video_id='+id
        r = requests.get(
            api,
            headers = {
                "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
            }
        )

        response = r.json()
        aweme_id = response.get('item', '').get('aweme_id', '')
        if aweme_id != '':
            url = 'https://api-h2.tiktokv.com/aweme/v1/play/?video_id='+aweme_id+'&vr_type=0&is_play_url=1&source=PackSourceEnum_FEED&media_type=4&ratio=default&improve_bitrate=1'
            res = requests.get(
                url,
                headers = {
                    'User-Agent' : 'okhttp',
                }
            )
            return res.url
        else:
            return False

    def getInfoUser(self, username):
        if username == '':
            return 'Username is required'
        try:
            res = requests.get(
                'https://tiktok.com/@{}?lang=en'.format(quote(username)),
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "authority": "www.tiktok.com",
                    "path": "/@{}".format(quote(username)),
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Host": "www.tiktok.com",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                }
            )
            resp = self.__extra_next_data__(res.text)
            return json.loads(resp)['props']['pageProps']
        except Exception:
            print(traceback.format_exc())
            return False

    def getUserFeed(self, username='', max_cursor=0, userid='0'):
        if username == '' and userid == '0':
            return 'Username or Userid is required'
        param = {
            "type": 1,
            "secUid": "",
            "id": '',
            "count": 30,
            "minCursor": 0,
            "maxCursor": max_cursor,
            "shareUid": "",
            "lang": "",
            "verifyFp": "",
        }
        if userid != '0':
            param['id'] = userid
        else:
            user = self.getInfoUser(username)
            if user:
                param['id'] = user['userInfo']['user']['id']
            else:
                url = "https://www.tiktok.com/@"+username
                user = self.get_user_by_html(url)
                print(user)
                param['id'] = user['userInfo']['user']['id']
        try:
            url = self.BASE_URL + 'video/feed'
            res = requests.get(
                url,
                params=param,
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "authority": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Host": "www.tiktok.com",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                }
            )
            resp = res.json()
            return resp['body'], res.cookies.get_dict()
        except Exception:
            print(traceback.format_exc())
            return False
    def __extra_next_data__(self, html):
        res = re.search('<script id="__NEXT_DATA__" type="application/json"(.*)</script><script', html).group(1)
        resp = res.split('>')[1].split('<')[0]
        return resp
    def get_all_id_video__of_user(self,username):
        list_id =[]
        list_caption = []
        list_nick = []
        list_play = []
        data_raw = self.getUserFeed(username)
        data_raw = data_raw[0]["itemListData"]
        for data in data_raw:
            list_id.append(data['itemInfos']['id'])
            list_caption.append(data['itemInfos']['text'])
            list_nick.append(data['authorInfos']['nickName'])
            list_play.append(data['itemInfos']['playCount'])
        return list_id,list_caption,list_nick,list_play

    #get trending tiktok
    def getTrendingFeed(self, max_cursor=0, cookies={}):
        param = {
            "type": 5,
            "secUid": "",
            "id": '',
            "count": 30,
            "minCursor": 0,
            "maxCursor": max_cursor,
            "shareUid": "",
            "lang": "vi-VN",
            "verifyFp": "",
            "region": "VN"
        }
        try:
            url = self.BASE_URL + 'video/feed'
            res = requests.get(
                url,
                params=param,
                headers={
                    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
                    "authority": "www.tiktok.com",
                    "Accept-Encoding": "gzip, deflate",
                    "Connection": "keep-alive",
                    "Host": "www.tiktok.com",
                    "User-Agent": "Mozilla/5.0  (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) coc_coc_browser/86.0.170 Chrome/80.0.3987.170 Safari/537.36",
                },
                cookies=cookies
            )

            resp = res.json()
            return resp['body'], res.cookies.get_dict()
        except Exception:
            print(traceback.format_exc())
            return False
    def get_all_id_video_from_trending(self):
        list_id = []
        list_caption = []
        list_nick = []
        list_play = []
        data = self.getTrendingFeed()[0]
        data_raw = data["itemListData"]
        for data in data_raw:
            list_id.append(data['itemInfos']['id'])
            list_caption.append(data['itemInfos']['text'])
            list_nick.append(data['authorInfos']['nickName'])
            list_play.append(data['itemInfos']['playCount'])
        return list_id, list_caption, list_nick, list_play

if __name__ == '__main__':
    new = Download()
    print(new.get_all_id_video_from_trending())

    # for id in list_id:
    #     print(new.downloadVideoNoWatermarkByID(id,"son"))