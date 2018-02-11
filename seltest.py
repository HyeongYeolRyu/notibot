from selenium import webdriver
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time


capabilities = webdriver.DesiredCapabilities.PHANTOMJS.copy()
#capabilities["page.settings.userAgent"] = (
#   "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:40.0) Gecko/20100101 Firefox/40.0")
capabilities['phantomjs.page.settings.userAgent'] = \
    ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36')
driver = webdriver.PhantomJS(executable_path='./../phantomjs',desired_capabilities=capabilities, service_args=['--ssl-protocol=any', '--web-security=false'])


#driver=wd.PhantomJS('/home/tk/phantom/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
#driver=webdriver.Chrome('./../chromedriver')
driver.implicitly_wait(3)


driver.get('https://accounts.kakao.com/login?continue=https://center-pf.kakao.com/signup')
#print(driver.page_source)

#driver.implicitly_wait(10)
driver.find_element_by_id('email').send_keys("fate_star@nate.com")

#driver.implicitly_wait(10)
driver.find_element_by_id('password').send_keys("050505s")
driver.find_element_by_id('btn_login').click()
driver.implicitly_wait(3)

#print(driver.page_source)
driver.get("https://center-pf.kakao.com/_hfvhC/messages/new/feed")
print(driver.page_source)
print("======================")
driver.find_element_by_id('messageWrite').send_keys("python에서 보낸 메시지입니다")
driver.find_element_by_css_selector('#mArticle > div > form > div.message_write.message_new > div.info_message > div:nth-child(4) > div > div:nth-child(4) > label > span').click()
driver.implicitly_wait(1)
driver.find_element_by_id('btnName').send_keys('인포컴 바로가기')
driver.find_element_by_id('linkUpload').send_keys('http://infocom.ssu.ac.kr/rb/?c=2/38')
driver.find_element_by_css_selector('#mArticle > div > form > div.wrap_btn > span > button.btn_g.btn_g2').click()
driver.find_element_by_css_selector('#mArticle > div > form > div.wrap_btn > button.btn_g.btn_g2').click()
driver.find_element_by_css_selector('body > div:nth-child(8) > div > div:nth-child(2) > div > div > div.wrap_btn > button.btn_g.btn_g2').click()