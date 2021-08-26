from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

fb_friend_req = 'https://www.facebook.com/friends/requests'
driver = webdriver.Edge("./edgedriver_win64/msedgedriver.exe")
i = 1
xpath = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[{}]/div[1]/a[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]'.format(i)
print(xpath)
#Won't change even you change i

#Setup Envirement

def logincheck():
    if driver.current_url == fb_friend_req:
        return True
    else:
        return False
#Login Checker

driver.get(fb_friend_req)
time.sleep(1)
#Goto login

while True:
    if logincheck():
        print("Login Success")
        break
#Check login

time.sleep(5)
print('Now start delete friend request.')
#blank_obj = driver.find_element_by_xpath("/html/body/div[2]/div[1]/div/div[2]")
#blank_obj.click()
#push_noti_button = driver.find_element_by_tag_name("button")
#push_noti_button.click()
time.sleep(1)



def del_Friend_req():
    del_friend_button = driver.find_element_by_xpath(xpath)
    del_friend_button.click()
    time.sleep(500/1000)
#Setup Delete Friend
while(True):
    del_Friend_req()
    i = i + 1
    xpath = '/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[4]/div[{}]/div[1]/a[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[2]/div[1]'.format(i)
    if i >= 9 :
        driver.get(fb_friend_req)
        i = 1
        #time.sleep(5)
        #blank_obj2 = driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[2]')
        #blank_obj2.click()
        #push_noti_button = driver.find_element_by_tag_name("button")
        #push_noti_button.click()
        try:
            myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        except TimeoutException:
            myElem = WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, xpath)))
        print("Reloading...")