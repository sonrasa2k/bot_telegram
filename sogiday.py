from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
class SoGiDay():
    def __init__(self):
        self.so = None
    def ket_qua_hientai(self,gio):
        driver = webdriver.Chrome("chromedriver.exe", options=options)
        driver.get('https://giaitri.shopee.vn/lottery/result?theme_id=e2beb3258915d83a94d50fc8b9b5393b')
        # nut = driver.find_element_by_xpath('//*[@id="__next"]/section/div[1]/main/div[1]/button[2]/div')
        # nut.click()
        if gio == 9:
            data_9h = driver.page_source.split(' class="jsx-432935148 jsx-3983037849 winner  ">')[1].split('</td><td')[0]
            return str(data_9h)
        if gio == 12:
            data_12h = driver.page_source.split(' class="jsx-432935148 jsx-3983037849 winner  ">')[3].split('</td><td')[0]
            return str(data_12h)
        if gio ==20:
            data_20h = driver.page_source.split(' class="jsx-432935148 jsx-3983037849 winner  ">')[5].split('</td><td')[0]
            return str(data_20h)
        return str("Hôm nay chả có gì hết!")
        # try:
        #     data_9h = driver.page_source.split('class="jsx-432935148 jsx-3983037849 winner pending ">')[1].split('</td><td')[0]
        #     print(data_9h)
        # except:
        #     data_9h = driver.page_source.split(' class="jsx-432935148 jsx-3983037849 winner  ">')[1].split('</td><td')[0]
        #     print(data_9h)
        # try:
        #     data_12h = driver.page_source.split('class="jsx-432935148 jsx-3983037849 winner pending ">')[2].split('</td><td')[0]
        #     print(data_12h)
        # except:
        #     data_12h = driver.page_source.split(' class="jsx-432935148 jsx-3983037849 winner  ">')[3].split('</td><td')[0]
        #     print(data_12h)
        # try:
        #     data_20h = driver.page_source.split('class="jsx-432935148 jsx-3983037849 winner pending ">')[5].split('</td><td')[0]
        #     print(data_20h)
        # except:
        #     data_20h = driver.page_source.split(' class="jsx-432935148 jsx-3983037849 winner  ">')[5].split('</td><td')[0]
        #     print(data_20h)
        driver.quit()
if __name__ == '__main__':
    so = SoGiDay()
    print(so.ket_qua_hientai(9))