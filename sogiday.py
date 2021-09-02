from selenium import webdriver
from selenium.webdriver.chrome.options import Options
options = Options()
options.headless = True
driver = webdriver.Chrome("/usr/bin/chromedriver", options=options)

driver.get("https://giaitri.shopee.vn/lottery/result?theme_id=e2beb3258915d83a94d50fc8b9b5393b")

print(driver.page_source)
driver.quit()