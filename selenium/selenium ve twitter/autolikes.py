from selenium import webdriver
import loginInfo
import time
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()

browser.get("https://twitter.com/")

time.sleep(3)

giris_yap=browser.find_element_by_xpath("//*[@id='react-root']/div/div/div/main/div/div/div/div[1]/div/div[3]/a[2]/div/span/span")
giris_yap.click()

time.sleep(3)

username = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
password = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

username.send_keys(loginInfo.username)
password.send_keys(loginInfo.password)

login =  browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
login.click()
time.sleep(3)

"""dogrulamaname = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
dogrulamapassword = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")

dogrulamaname.send_keys("fenixxxxx3")
dogrulamapassword.send_keys("erimfb123")

login2= browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div/span/span")
login2.click()"""


searchArea = browser.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/label/div[2]/div/input")
searchArea.send_keys("#yazilimayolver")
time.sleep(2)
searchArea.send_keys(Keys.ENTER)

time.sleep(5)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount=lenOfPage
    time.sleep(3)
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

time.sleep(5)

elements=browser.find_elements_by_class_name("css-18t94o4 css-1dbjc4n r-1777fci r-bt1l66 r-1ny4l3l r-bztko3 r-lrvibr")

for element in elements:
    try:
        element.click()
    except Exception:
        print("There is an error occured....")