from selenium import webdriver
import time
import pygame
pygame.init()

Driver = webdriver.Chrome("C:\\SeleniumDrivers\\chromedriver.exe")
Driver.set_page_load_timeout(20)
print("ready...alarm set")
print("login to hive.. please wait..")
Driver.get("http://hive.garenanow.com")
Driver.set_page_load_timeout(30)
Driver.find_element_by_id("identifierId").send_keys("beetalkid@beetalkmobile.com")
Driver.find_element_by_id("identifierNext").click()
Driver.implicitly_wait(4)
Driver.find_element_by_name("password").send_keys("B33testing%$#@!")
Driver.find_element_by_id("passwordNext").click()
Driver.implicitly_wait(10)
print("login success",time.strftime('%m/%d/%Y %H:%M:%S'))
Driver.find_element_by_xpath("//*[@id='nav-accordion']/li[1]/a/span").click()
Pending = Driver.find_element_by_xpath("//*[@id='dashboard_user']/div/div[1]/div[1]/div/span").text
Pending = int(Pending)

while True :
    print(Pending)
    time.sleep(10)
    Driver.refresh()
    if Pending >= 20 :


    else :
        print("alhamdulillah")


