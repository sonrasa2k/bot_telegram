import requests

phone = "+84838273502"
data = {
    "phone":phone
}
#laays random hash
random_hash = requests.post("https://my.telegram.org/auth/send_password",data=data).json()["random_hash"]


#
code = input("Nhap code: ")

data_login = {
    "phone":phone,
    "random_hash":random_hash,
    "password":code
}
session = requests.Session()
login = session.post("https://my.telegram.org/auth/login",data=data_login)
print(login.text)
apis = session.get("https://my.telegram.org/apps")
print(apis.text)

# print(random_hash)


