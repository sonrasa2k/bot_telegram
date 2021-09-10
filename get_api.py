import requests
from datetime import datetime
from random import randrange

def get_key():

    now = datetime.now()

    now = str(now).split(" ")
    key1 = "".join(now[0].split("-"))
    key2 = "".join(("".join(now[1].split(":")).split(".")))
    key = key2 + key1
    return key
class GetApi:
    def __init__(self,phone):
        self.phone = phone
    def get_random_hash(self):
        data = {
            "phone":self.phone
        }
        #laays random hash
        random_hash = requests.post("https://my.telegram.org/auth/send_password",data=data).json()["random_hash"]
        return random_hash
    def get_api(self,random_hash,code):
        data_login = {
            "phone":self.phone,
            "random_hash":random_hash,
            "password":code
        }
        session = requests.Session()
        login = session.post("https://my.telegram.org/auth/login",data=data_login)
        apis = session.get("https://my.telegram.org/apps")

        api_data = apis.text
        try:
            api_id = api_data.split('<span class="form-control input-xlarge uneditable-input" onclick="this.select();"><strong>')[1].split('</strong></span>')[0]
            api_hash = api_data.split('<span class="form-control input-xlarge uneditable-input" onclick="this.select();">')[2].split('</span>')[0]
        except:
            hash = api_data.split('name="hash" value="')[1].split('"/>')[0]
            print(hash)
            app_title = "S"+str(get_key())+"api"
            app_shortname = "abc"+str(get_key())
            app_url = "hongtin.net"
            data_create = {
                "hash":hash,
                "app_title":app_title,
                "app_shortname":app_shortname,
                "app_url":app_url,
                "app_platform":"android",
                "app_desc":"tool auto get api"
            }
            api_new = session.post("https://my.telegram.org/apps/create",data=data_create)
            api_new_data = session.get("https://my.telegram.org/apps").text
            api_id = api_new_data.split('<span class="form-control input-xlarge uneditable-input" onclick="this.select();"><strong>')[1].split('</strong></span>')[0]
            api_hash = api_new_data.split('<span class="form-control input-xlarge uneditable-input" onclick="this.select();">')[2].split('</span>')[0]
            return {"code":200,"phone":self.phone,"api_id":api_id,"api_hash":api_hash}
        result = {"code":200,"phone":self.phone,"api_id":api_id,"api_hash":api_hash}
        return result
if __name__ == '__main__':
    apied = GetApi("+84815698714")
    random_hash = apied.get_random_hash()
    code = input("code: ")
    print(apied.get_api(random_hash,code))
# print(random_hash)


