from selenium import webdriver
import time
import loginInfo

browser = webdriver.Firefox()

browser.get("https://www.instagram.com/")
time.sleep(2)

logName = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[1]/div/label/input")
logPassword = browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[2]/div/label/input")

logName.send_keys(loginInfo.name)
logPassword.send_keys(loginInfo.password)
time.sleep(2)

loginButton=browser.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[3]/button")
loginButton.click()
time.sleep(5)

simdidegilButton=browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div/div/button")
simdidegilButton.click()
time.sleep(5)

simdidegilButton_2 = browser.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]")
simdidegilButton_2.click()
time.sleep(5)

profileSelector = browser.find_element_by_xpath("/html/body/div[1]/section/main/section/div[3]/div[1]/div/div/div[2]/div[1]/div/div/a")
profileSelector.click()
time.sleep(5)

openFollowers = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/ul/li[2]/a")
openFollowers.click()
time.sleep(5)

jscommand = """
followers = document.querySelector(".isgrP");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;

"""
lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount=lenOfPage
    time.sleep(1)
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True
time.sleep(5)

followersList= []

followers = browser.find_elements_by_css_selector(".FPmhX.notranslate._0imsa ")

for follower in followers:
    followersList.append(follower.text)

with open("followers.txt","w",encoding="UTF-8") as file:
    for follower in followersList:
        file.write(follower+"\n")

"""securityCodePath = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[1]/div/label/input")
securityCodePath.send_keys(input("please write your security number:"))


confirmButton = browser.find_element_by_xpath("/html/body/div[1]/section/main/div/div/div[1]/div/form/div[2]/button")
confirmButton.click()"""

browser.close()