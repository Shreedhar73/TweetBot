from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser_path = "C:/Program Files/BraveSoftware/Brave-Browser/Application/brave.exe"
driver_path = "C:/Users/Shreedhar/Desktop/chromedriver_win32/chromedriver.exe"

option = webdriver.ChromeOptions()
option.binary_location = browser_path

driver = webdriver.Chrome(executable_path= driver_path, chrome_options= option)


driver.get("https://twitter.com/login")
sleep(1)
username = input("Enter Your UserName or Email....")
password = input("Enter your Twitter Password")

driver.find_element_by_name('session[username_or_email]').send_keys(username)
driver.find_element_by_name('session[password]').send_keys(password)
driver.find_element_by_name('session[password]').send_keys(Keys.RETURN)

sleep(1)

f = open("xxx.txt", 'r')

for word in f:
    if word == "\t":
        continue
    driver.find_element_by_xpath("//a[@data-testid='SideNav_NewTweet_Button']").click()
    sleep(2)
    driver.find_element_by_class_name("notranslate").click()
    driver.find_element_by_class_name("notranslate").send_keys(word+ "#" + "CancelTUExams " +"#" + "DontPostPone_Find_An_Alternative  " +"@CCMCNEPAL "+ "@SherBDeuba  "+ "@thapagk  " )
    
    
    

    sleep(1)
    driver.find_element_by_xpath("//div[@data-testid='tweetButton']").click()

    
    
    
    sleep(5)

f.close()

