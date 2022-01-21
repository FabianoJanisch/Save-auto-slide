import requests
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://slmandic.blackboard.com/ultra/stream"
url2 = "https://slmandic.blackboard.com/ultra/courses/_50286_1/outline"
data = time.gmtime()

driver = webdriver.Chrome('C:\chromedriver')

driver.get(url)

coisa = driver.find_element_by_xpath('//*[@id="agree_button"]')
webdriver.ActionChains(driver).double_click(coisa).perform()
username = driver.find_element_by_xpath('//*[@id="user_id"]')
webdriver.ActionChains(driver).click_and_hold(username).send_keys("myusername").perform()
password = driver.find_element_by_xpath('//*[@id="password"]')
webdriver.ActionChains(driver).click_and_hold(password).send_keys("mypassword" + Keys.ENTER).perform()

driver.get(url2)
time.sleep(10)
wait = WebDriverWait(driver, 10)
#ID da janela original
original_window = driver.current_window_handle
assert len(driver.window_handles) == 1

sala = driver.find_element(By.ID, "sessions-list-dropdown")
webdriver.ActionChains(driver).click(sala).perform()
salacurso = driver.find_element_by_xpath('//*[@id="sessions-list"]/li[1]/a/span')
webdriver.ActionChains(driver).click(salacurso).perform()
wait.until(EC.number_of_windows_to_be(2))
for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

time.sleep(40)
pagT = 0
try:
        daym = (str(data[2])+'.'+str(data[1]))
except FileExistsError:
        print (f'A pasta "{daym}" já existe')
while True:
        try:
                if pagT == 0:
                        nomeaula = driver.find_element_by_css_selector('span.whiteboard-viewer-name').text.replace(".pdf", "")
                if nomeaula != driver.find_element_by_css_selector('span.whiteboard-viewer-name').text.replace(".pdf", ""):
                        pagT = 0
                try:
                        pag = driver.find_element_by_xpath ('//*[@id="whiteboard"]/div[3]/span[1]/span[2]').text.replace("(", "").split('/')[0]
                except:
                        pag = driver.find_element_by_xpath ('//*[@id="whiteboard"]/div[4]/span[1]/span[2]').text.replace("(", "").split('/')[0]
                if int(pag) > int(pagT):
                        nomeaula = driver.find_element_by_css_selector('span.whiteboard-viewer-name').text.replace(".pdf", "")
                        nomeaba = driver.title
                        nomeaba2 = nomeaba.split('-')
                        nomeabaf = str(nomeaba2[2][1]).strip() + str(nomeaba2[2][2]).strip().upper() + str(nomeaba2[2][3]).strip().upper()
                        pagT = int(pag)
                        takeS = driver.find_element_by_xpath('//*[@id="wb-svg-main"]')
                        takeS.screenshot(f'/{daym}/{nomeaba} {nomeaula} {pag}.png')
        except Exception as e:
                print (e)
                print ('Um erro aconteceu')
                pass
        time.sleep(10)

