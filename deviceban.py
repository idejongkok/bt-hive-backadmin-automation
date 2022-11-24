from selenium import webdriver
import time
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("Legislators-9320fd14c0a6.json",scope)
gc = gspread.authorize(credentials)
wks = gc.open("testing python").sheet1
Driver = webdriver.Chrome("C:\\SeleniumDrivers\\chromedriver.exe")


#Login dulu bro
Driver.get("http://hive.garenanow.com")
Driver.set_page_load_timeout(30)
Driver.find_element_by_id("identifierId").send_keys("susenoa@garena.co.id")
Driver.find_element_by_id("identifierNext").click()
Driver.implicitly_wait(4)
Driver.find_element_by_name("password").send_keys("enggakadayangbolehtautuh")
Driver.find_element_by_id("passwordNext").click()
Driver.implicitly_wait(100)
print("check uno's phone, please press YES button")
Driver.implicitly_wait(100)
print("login success",time.strftime('%m/%d/%Y %H:%M:%S'))
time.sleep(5)

A = "a"
B = "b"
C = 1

while C <= 19 :
    ColumnA = A + str(C)
    ColumnB = B + str(C)
    InternalID = wks.acell(ColumnA).value
    #masuk search ID
    print("searching ID ",InternalID)
    Driver.find_element_by_link_text("Search").click()
    time.sleep(5)
    Driver.find_element_by_xpath("//*[@id='user_search']/div[1]/section/div/div/form[2]/div/input").send_keys(InternalID)
    Driver.find_element_by_xpath("//*[@id='user_search']/div[1]/section/div/div/form[2]/div/span/input").click()
    time.sleep(5)
    #check device status
    print("checking device status..")
    Status = Driver.find_element_by_xpath("//*[@id='user_profile']/div[1]/section/div/div[2]/p[4]/span/strong/span").text
    print("Device ",Status)
    Device = Status
    #check device sign n ban
    if Device in ("Active") :
        print("Check Device Sign..")
        Driver.find_element_by_xpath("//*[@id='show_device']").click()
        Driver.implicitly_wait(100)
        time.sleep(2)
        ButtonText = Driver.find_element_by_id("device_list").text
        if ButtonText in ("Ban Device") :
            Driver.find_element_by_xpath("//*[@id='device_list']/button").click()
            Driver.implicitly_wait(100)
            time.sleep(2)
            Driver.find_element_by_xpath("//*[@id='banDeviceModal']/div/div/div[3]/form/input[5]").click()
            print("Done")
        else :
            print("no device")
    else :
        print("Device has been banned b4")
    wks.update_acell(ColumnB,time.strftime('%m/%d/%Y %H:%M:%S'))
    C = C + 1
#back to search

