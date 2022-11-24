
import gspread
from oauth2client.service_account import ServiceAccountCredentials
scope = ["https://spreadsheets.google.com/feeds","https://www.googleapis.com/auth/drive"]
credentials = ServiceAccountCredentials.from_json_keyfile_name("Legislators-9320fd14c0a6.json",scope)
gc = gspread.authorize(credentials)
wks = gc.open("testing python").sheet1

#print(wks.get_all_records())
#wks.append_row(["kolom 1","kolom 2"])
link = wks.acell("a1").value
print(link)