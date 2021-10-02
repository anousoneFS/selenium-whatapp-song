from selenium import webdriver
import time
import requests

# firefox_browser = webdriver.Firefox(executable_path='/Users/anousonefs/Downloads/geckodriver')
# firefox_browser.get('https://web.whatsapp.com/')

# options ໃຊ້ສຳຫຼັບບໍ່ຕ້ອງສະແກນ QR code
options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=/Users/anousonefs/Library/Application Support/Google/Chrome/Default')
options.add_argument('--profile-directory=default')

chrome_browser = webdriver.Chrome(executable_path='/Users/anousonefs/Downloads/chromedriver',options=options)
chrome_browser.get('https://web.whatsapp.com/')

time.sleep(15)
print('connected')

# whatsapp_name_list = ['โจ้', 'WhatsAppBot','ລັນ']
whatsapp_name_list = ['ບິ້ນ']

for whatsapp_name in whatsapp_name_list:
    user = chrome_browser.find_element_by_xpath(f'//span[@title="{whatsapp_name}"]')
    user.click()

    n = 1
    total_quote = 50
    while True:
        r = requests.get('http://api.quotable.io/random')
        if r.status_code == 200:
            data = r.json()
            quote = f'{n}. {data["content"]} (say by {data["author"]})'
        else:
            quote = 'ບໍ່ສາມາດຄົ້ນຫາຄຳຄົມໄດ້ sorry'

        message_box = chrome_browser.find_element_by_xpath('//div[@class="_2A8P4"]')
        message_box.send_keys(quote)
        button_send = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
        button_send.click()

        n += 1
        if n > total_quote:
            message_box = chrome_browser.find_element_by_xpath('//div[@class="_2A8P4"]')
            message_box.send_keys(f'ທັງໝົດນີ້ແມ່ນ ຄຳຄົມເດີ້ ຈຳນວນ {total_quote} ຄຳຄົມ ຫຼື ທ່ານຕ້ອງການໃຫ້ bot ສົ່ງໃຫ້ຫຼາຍກວ່ານີ້ກໍໄດ້')
            button_send = chrome_browser.find_element_by_xpath('//button[@class="_1E0Oz"]')
            button_send.click()
            break

print(f"Send Success for {whatsapp_name_list.join(', ')}")
