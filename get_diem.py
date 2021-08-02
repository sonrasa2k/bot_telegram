    import requests

    url = 'https://diemthi.vnanet.vn//Home/SearchBySobaodanh'

    json_request = {
        "code":30005407,
        "nam":2021
    }
    kq = requests.get(url,json=json_request).json()
    print(kq)







