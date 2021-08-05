import requests

cookies = {
    'tt_webid_v2': '6906584401044538882',
    'tt_webid': '6906584401044538882',
    'store-idc': 'alisg',
    'store-country-code': 'vn',
    '_abck': '81A3203635CAA8DB148C0B3C5B2BAE22~0~YAAQMqo3F+FAQgt5AQAA227AEwWalJrm5HY+NzI4mfkZN34Xm+Q4cJ8m8+IK+x87Qykob5gFzCGp5jP9TQtJmbld/bcFyGU04cYyNkjqPG5Nta8GUKRZxg6IAXcDP+dsCEAAfzqx33V4np/zH5bW7C3oQWH0ZgQA15XJh63JyCf4L6r0sNqUl/buDs0pYHQl4yhv6Ag6e4jQAIoTkQOuULXr0vFHfiTv9fR4KVZfSuHA91WQGmWNWSbc5gB576oiSxhlHCH8duAhpaZfUsJpNZFBtYmaQN4R97AJW/n9jRNlAFBA+cyRbb+dKv8EMCRi4waKpg/RlCBDVMM0DLmyMdW3vRAG+rWrysxxy29lmdL/wT5unRneit6U81gl//G6bEVs+v0=~-1~-1~-1',
    'passport_csrf_token_default': 'd213ac9db5f49b56f1d6e6fae18678b6',
    'passport_csrf_token': 'd213ac9db5f49b56f1d6e6fae18678b6',
    'passport_auth_status': '9f3ce415262d948f5e8297ecc0137b5b^%^2C',
    'passport_auth_status_ss': '9f3ce415262d948f5e8297ecc0137b5b^%^2C',
    'sid_guard': 'db89d4ee9c4a56749ff4547a60e26716^%^7C1627829148^%^7C5183999^%^7CThu^%^2C+30-Sep-2021+14^%^3A45^%^3A47+GMT',
    'uid_tt': '5a1d9d5f41f64aff799f10c82f263954ae12d9df688a053fdd597ed880b9e23f',
    'uid_tt_ss': '5a1d9d5f41f64aff799f10c82f263954ae12d9df688a053fdd597ed880b9e23f',
    'sid_tt': 'db89d4ee9c4a56749ff4547a60e26716',
    'sessionid': 'db89d4ee9c4a56749ff4547a60e26716',
    'sessionid_ss': 'db89d4ee9c4a56749ff4547a60e26716',
    'tt_csrf_token': 'bXW63Qw6VG_2QN8XlNav-cR-',
    'R6kq3TV7': 'ADTe6BZ7AQAAzIHjRQaf6asLuTXJs4EMXwAJuM3R0mEXNukEwjaRCPhlx8RG^|1^|0^|30ea7640cd8f093498fdb5a8665a8c91588fbffb',
    'csrf_session_id': '6ee0989860f6430a8f5915017bd68457',
    'cmpl_token': 'AgQQAPPdF-RMpYr-erL5Odk4xbiE2CQcv4AOYP2J6A',
    'ttwid': '1^%^7C31yObapDPsmlj3wjaLTy3vG_v6bNeW_cnxw847CapnQ^%^7C1628177045^%^7Cc31a206c17bb62200488b96ffd50de734e658932e617786727f97026ec73e064',
    'odin_tt': '8dbec1173363e1d5e75701b86835691a6db64e769716ede426040310ab18815721a2d30288308e93a0602bf69ce1a427eef47037c4e920488f0a29ec3e153608',
}

headers = {
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'sec-ch-ua': '^\\^Chromium^\\^;v=^\\^92^\\^, ^\\^',
    'sec-ch-ua-mobile': '?0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Sec-Fetch-Site': 'none',
    'Sec-Fetch-Mode': 'navigate',
    'Sec-Fetch-User': '?1',
    'Sec-Fetch-Dest': 'document',
    'Accept-Language': 'vi,en-US;q=0.9,en;q=0.8',
}

params = (
    ('aid', '1988'),
    ('app_name', 'tiktok_web'),
    ('device_platform', 'web_pc'),
    ('device_id', '6906584401044538882'),
    ('region', ''),
    ('priority_region', 'VN'),
    ('os', 'windows'),
    ('referer', ''),
    ('root_referer', ''),
    ('cookie_enabled', 'true'),
    ('screen_width', '1536'),
    ('screen_height', '864'),
    ('browser_language', 'vi'),
    ('browser_platform', 'Win32'),
    ('browser_name', 'Mozilla'),
    ('browser_version', '5.0 (Windows NT 10.0^%^3B Win64^%^3B x64) AppleWebKit^%^2F537.36 (KHTML, like Gecko) Chrome^%^2F92.0.4515.131 Safari^%^2F537.36'),
    ('browser_online', 'true'),
    ('verifyFp', 'verify_kmw96uek_8lofr5Vk_1WgP_4VT1_8qhK_F7weuL2RdECF'),
    ('app_language', 'vi-VN'),
    ('timezone_name', 'Asia^%^2FBangkok'),
    ('is_page_visible', 'true'),
    ('focus_state', 'true'),
    ('is_fullscreen', 'false'),
    ('history_len', '15'),
    ('battery_info', '1'),
    ('count', '30'),
    ('itemID', '1'),
    ('language', 'vi-VN'),
    ('from_page', 'fyp'),
    ('insertedItemID', ''),
    ('_signature', '_02B4Z6wo00d017Cm42wAAIDCbtC7y8Aa4A-wpufAAI0u5bVN'),
)

response = requests.get('https://t.tiktok.com/api/recommend/item_list/', headers=headers, params=params)
print(response.json())
#NB. Original query string below. It seems impossible to parse and
#reproduce query strings 100% accurately so the one below is given
#in case the reproduced version is not "correct".
# response = requests.get('https://t.tiktok.com/api/recommend/item_list/?aid=1988&app_name=tiktok_web&device_platform=web_pc&device_id=6906584401044538882&region=&priority_region=VN&os=windows&referer=&root_referer=&cookie_enabled=true&screen_width=1536&screen_height=864&browser_language=vi&browser_platform=Win32&browser_name=Mozilla&browser_version=5.0+(Windows+NT+10.0^%^3B+Win64^%^3B+x64)+AppleWebKit^%^2F537.36+(KHTML,+like+Gecko)+Chrome^%^2F92.0.4515.131+Safari^%^2F537.36&browser_online=true&verifyFp=verify_kmw96uek_8lofr5Vk_1WgP_4VT1_8qhK_F7weuL2RdECF&app_language=vi-VN&timezone_name=Asia^%^2FBangkok&is_page_visible=true&focus_state=true&is_fullscreen=false&history_len=15&battery_info=1&count=30&itemID=1&language=vi-VN&from_page=fyp&insertedItemID=&_signature=_02B4Z6wo00d017Cm42wAAIDCbtC7y8Aa4A-wpufAAI0u5bVN', headers=headers, cookies=cookies)