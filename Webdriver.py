from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service



    
path=Service("C:\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get('http://www.32x8.com/var5.html')

arr3 = [0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0]

count = 0
num = 3


for i in range(32):
    row = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr["+str(num)+"]/td[8]/input")
    if arr3[i] == 1:
        row.click()
    num+=1
    count+=1

sub = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[35]/td/input")
sub.click()

