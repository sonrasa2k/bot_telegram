import requests
from enum import Enum
class sendVideo():
    def __init__(self):
        self.headers = {
        'Content-Type': 'application/json',
        }
        self.params = (
        ('access_token', 'EAADCmt8dSl0BAPEuQzVv0WZBgqPCpRwp7S6sP9ZBRVnhz4QYEY4FNzLDBisJ6ZCyoUtSGvBqouZBx0GgeBu1eLl2pietZAJz245RSF2HxoJmDUhrZAviu6zdoBBzcb57fO1MfVAtioqYzjAZB9QM9VuJ7HyblsLWA7hGZCllb3etpXHez5o8dOaAHkxRt8YkqZADUjOHB2LGJSQZDZD'),
        )
    def gui_video(self,url_video,id_gui):
        data = '{ "recipient":{ "id":"'+str(id_gui)+'" }, "message":{ "attachment":{ "type":"video", "payload":{ "url":"'+str(url_video)+'", "is_reusable":false } } } }'
        response = requests.post('https://graph.facebook.com/v11.0/me/messages', headers=self.headers, params=self.params, data=data)
        print(response.content)
        return True
    def gui_video2(self,url_video,recipient_id):
        payload = {
            'message':{
                'attachment':{
                    "type":"video",
                    "payload":{
                        "url":str(url_video),
                        "is_reusable":"true"
                    }
            }
            },
            'recipient': {
                'id': recipient_id
            },
            'notification_type': 'regular'
        }

        auth = {
            'access_token': 'EAADCmt8dSl0BAPEuQzVv0WZBgqPCpRwp7S6sP9ZBRVnhz4QYEY4FNzLDBisJ6ZCyoUtSGvBqouZBx0GgeBu1eLl2pietZAJz245RSF2HxoJmDUhrZAviu6zdoBBzcb57fO1MfVAtioqYzjAZB9QM9VuJ7HyblsLWA7hGZCllb3etpXHez5o8dOaAHkxRt8YkqZADUjOHB2LGJSQZDZD'
        }

        response = requests.post(
            "https://graph.facebook.com/v11.0/me/messages",
            params=auth,
            json=payload
        )

        return response.json()