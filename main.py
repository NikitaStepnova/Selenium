from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox(executable_path='geckodriver.exe')
driver.get("https://nstu.ru")
time.sleep(2)

bth_login = driver.find_element_by_css_selector("div.header__login>a")
bth_login.click()

time.sleep(1)

bth_kabinert = driver.find_element_by_xpath('//a[text() = "Кабинет обучающегося"]') 
bth_kabinert.click()

time.sleep(2)

input_login = driver.find_element_by_name('callback_0')
input_password = driver.find_element_by_name('callback_1')

input_login.send_keys('stepnov.2018@stud.nstu.ru')
input_password.send_keys('*************')

input_password.send_keys(Keys.RETURN)
time.sleep(2)

bth_w = driver.find_element_by_xpath('//div[text() = "Информация об успеваемости"]') 
bth_w.click()
time.sleep(2)
bth_w2 = driver.find_element_by_xpath('//div[text() = "Результаты сессии/ Зачетка"]') 
bth_w2.click()
time.sleep(2)


tables = driver.find_elements_by_css_selector(".sysContentWithMenu>table>tbody")   
for table in tables:
    tds = table.find_elements_by_css_selector('tr.all_progress>td.tdbr:nth-child(2)')
    j = 0
    for td in tds:
        print(td.text)
    break
time.sleep(5)
driver.close()