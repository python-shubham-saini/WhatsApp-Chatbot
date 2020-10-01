from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import pyperclip
import time , sys
from config import CHROME_PROFILE_PATH
options = webdriver.ChromeOptions()
options.add_argument(CHROME_PROFILE_PATH)

browser = webdriver.Chrome(executable_path="C:\chromedriver\chromedriver", options=options)
browser.maximize_window()
browser.get("https://web.whatsapp.com/")
try:
    if sys.argv[1]:
        with open(sys.argv[1], 'r', encoding='utf8') as f :
            groups = [group.strip() for group in f.readlines()]
            ss = 0
            while ss <= len(groups):
                print(ss)
                ss+=1
except IndexError:
    print('Please provide grop name as first argument')
with open('msg.txt', 'r', encoding='utf8') as f :
    msg = f.read()
for group in groups:
    search_xpath ='//div[@contenteditable="true"][@data-tab="3"]'
    search_box = WebDriverWait(browser, 60).until(
        EC.presence_of_element_located((By.XPATH, search_xpath))
    )
    search_box.clear()
    time.sleep(1)
    pyperclip.copy(group)

    search_box.send_keys(Keys.SHIFT, Keys.INSERT)
    time.sleep(2)

    # group_xpath = '//span[@title="{}"]'.format(group)
    group_title = browser.find_element_by_xpath('//span[@title="{}"][@class="_3ko75 _5h6Y_ _3Whw5"]'.format(group))
    group_title.click()
        
    time.sleep(1)
    input_xpath = '//div[@contenteditable="true"][@data-tab="1"]'
    input_box = browser.find_element_by_xpath(input_xpath)
    # for i in range(1000):
    pyperclip.copy(msg)
    input_box.send_keys(Keys.SHIFT, Keys.INSERT)
    input_box.send_keys(Keys.RETURN)
    time.sleep(1)
    # try:
    #     if sys.argv[2]:
    #         attach_box = browser.find_element_by_xpath('//div[@title="Attach"]')
    #         attach_box.click()
    #         time.sleep(1)

    #         image_box = browser.find_element_by_xpath('//input[@accept="image/*,video/mp4,video/3gpp,video/quicktime"]')
    #         image_box.send_keys(sys.argv[2])
    #         time.sleep(2)

    #         send_btn = browser.find_element_by_xpath('//span[@data-icon="send"]')
    #         send_btn.click()
    #         time.sleep(3)
    # except IndexError:
    #     print('image Error')
