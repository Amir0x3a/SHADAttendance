
from selenium.webdriver import Chrome

driver = Chrome()

driver.get('https://web.shad.ir/')
cookies = driver.get_cookies()
for cookie in cookies:
    print(cookie)

