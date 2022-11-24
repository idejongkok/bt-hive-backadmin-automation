from selenium import webdriver
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("Legislators-9320fd14c0a6.json",scope)
gc = gspread.authorize(credentials)
wks = gc.open("testing python").sheet1
Driver = webdriver.Chrome("C:\\SeleniumDrivers\\chromedriver.exe")
Driver.set_page_load_timeout(20)
print("ready...")
print("welcome to the cheating program..")
print("login to hive.. please wait..")
Driver.get("http://hive.garenanow.com")
Driver.set_page_load_timeout(30)
Driver.find_element_by_id("identifierId").send_keys("bantuan@beetalkmobile.com")
Driver.find_element_by_id("identifierNext").click()
Driver.implicitly_wait(4)
Driver.find_element_by_name("password").send_keys("BeeTalkGarena123")
Driver.find_element_by_id("passwordNext").click()
Driver.implicitly_wait(10)
print("login success",time.strftime('%m/%d/%Y %H:%M:%S'))
#ngerjain forum image
print("start forum images review..")
Driver.implicitly_wait(10)
Driver.find_element_by_xpath('//*[@id="nav-accordion"]/li[5]').click()
Driver.find_element_by_link_text("Image Review").click()
Driver.implicitly_wait(4)
todo = Driver.find_element_by_id("todo").text
todo = int(todo)
print("there is ",todo," todo")
print("i will help you to decrease the number :v. Start passing all images..")
print("Please close the window if u want to stop this sh*t :v",time.strftime('%m/%d/%Y %H:%M:%S'))
while ( todo > 2000):
    Driver.refresh()
    time.sleep(5)
    todo = Driver.find_element_by_id("todo").text
    todo = int(todo)
    print("there is ", todo, " remaining",time.strftime('%m/%d/%Y %H:%M:%S'))
    print("continue passing..")
    wks.append_row([todo,time.strftime('%m/%d/%Y %H:%M:%S')])
    Driver.set_page_load_timeout(3000)
    Driver.find_element_by_xpath("//*[@id='profile-gallery']/div/div/section/header/form/input[2]").click()
    Driver.set_page_load_timeout(3000)
    Driver.find_element_by_xpath("//*[@id='profile-gallery']/div/div/section/header/form/input[3]").click()
    Driver.set_page_load_timeout(3000)
    time.sleep(10)
Driver.close()
print("udah om")


