
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service



    
path=Service("C:\chromedriver_win32 (1)\chromedriver.exe")
driver = webdriver.Chrome(service=path)

driver.get('http://www.32x8.com/var6.html')

arr4 = [1, 0, 1, 1, 2, 2, 2, 2, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 2, 2, 2, 2, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 1, 0, 1, 1, 0]

count = 0
num = 3


for i in range(64):
    row = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr["+str(num)+"]/td[9]/input")
    if arr4[i] == 1:
        row.click()
    if arr4[i] == 2:
        x = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr["+str(num)+"]/td[10]/input")
        x.click()
    num+=1
    count+=1

sub = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[67]/td/input")
sub.click()





















