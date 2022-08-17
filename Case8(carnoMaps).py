from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


    
path=Service("C:\chromedriver_win32\chromedriver.exe")
chrome_options = Options()
chrome_options.binary_location = r'C:\Program Files\Google\Chrome Beta\Application\chrome.exe'
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options = chrome_options, service=path)

driver.get('http://www.32x8.com/var6.html')

arr5 = [0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1]

count = 0
num = 3


for i in range(64):
    row = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr["+str(num)+"]/td[9]/input")
    if arr5[i] == 1:
        row.click()
    num+=1
    count+=1

sub = driver.find_element(By.XPATH,"/html/body/form/table/tbody/tr[67]/td/input")
sub.click()


'''

!x1 ^ !x2 ^ !x3 ^ k_map_0 or
!x1 ^ !x2 ^ x^3 ^ k_map_1


CASE 8  (0, 0, 0, 0, 0, 0, 0, 1, 0) 0
CASE 8  (0, 0, 0, 0, 0, 0, 1, 0, 0) 0
CASE 8  (0, 0, 0, 0, 0, 0, 1, 1, 1) 0
CASE 8  (0, 0, 0, 0, 0, 1, 0, 1, 0) 0
CASE 8  (0, 0, 0, 0, 0, 1, 1, 0, 0) 0
CASE 8  (0, 0, 0, 0, 0, 1, 1, 1, 1) 0
CASE 8  (0, 0, 0, 0, 1, 0, 1, 1, 0) 0
CASE 8  (0, 0, 0, 0, 1, 1, 1, 1, 0) 0
CASE 8  (0, 0, 0, 1, 0, 0, 1, 1, 0) 0
CASE 8  (0, 0, 0, 1, 0, 1, 1, 1, 0) 0
CASE 8  (0, 0, 0, 1, 1, 0, 1, 1, 0) 0
CASE 8  (0, 0, 0, 1, 1, 1, 1, 1, 0) 0

CASE 8  (0, 0, 1, 0, 0, 0, 1, 1, 0) 0
CASE 8  (0, 0, 1, 0, 0, 1, 1, 1, 0) 0
CASE 8  (0, 0, 1, 0, 1, 0, 0, 1, 0) 0
CASE 8  (0, 0, 1, 0, 1, 0, 1, 0, 0) 0
CASE 8  (0, 0, 1, 0, 1, 0, 1, 1, 1) 0
CASE 8  (0, 0, 1, 0, 1, 1, 0, 1, 0) 0
CASE 8  (0, 0, 1, 0, 1, 1, 1, 0, 0) 0
CASE 8  (0, 0, 1, 0, 1, 1, 1, 1, 1) 0
CASE 8  (0, 0, 1, 1, 0, 0, 0, 1, 0) 0
CASE 8  (0, 0, 1, 1, 0, 0, 1, 0, 0) 0
CASE 8  (0, 0, 1, 1, 0, 0, 1, 1, 1) 0
CASE 8  (0, 0, 1, 1, 0, 1, 0, 1, 0) 0
CASE 8  (0, 0, 1, 1, 0, 1, 1, 0, 0) 0
CASE 8  (0, 0, 1, 1, 0, 1, 1, 1, 1) 0
CASE 8  (0, 0, 1, 1, 1, 0, 0, 1, 0) 0
CASE 8  (0, 0, 1, 1, 1, 0, 1, 0, 0) 0
CASE 8  (0, 0, 1, 1, 1, 0, 1, 1, 1) 0
CASE 8  (0, 0, 1, 1, 1, 1, 0, 1, 0) 0
CASE 8  (0, 0, 1, 1, 1, 1, 1, 0, 0) 0
CASE 8  (0, 0, 1, 1, 1, 1, 1, 1, 1) 0

CASE 8  (0, 1, 0, 0, 0, 0, 0, 1, 0) 0
CASE 8  (0, 1, 0, 0, 0, 0, 1, 0, 0) 0
CASE 8  (0, 1, 0, 0, 0, 0, 1, 1, 1) 0
CASE 8  (0, 1, 0, 0, 0, 1, 0, 1, 0) 0
CASE 8  (0, 1, 0, 0, 0, 1, 1, 0, 0) 0
CASE 8  (0, 1, 0, 0, 0, 1, 1, 1, 1) 0
CASE 8  (0, 1, 0, 0, 1, 0, 0, 0, 0) 0
CASE 8  (0, 1, 0, 0, 1, 0, 0, 1, 1) 0
CASE 8  (0, 1, 0, 0, 1, 0, 1, 0, 1) 0
CASE 8  (0, 1, 0, 0, 1, 1, 0, 0, 0) 0
CASE 8  (0, 1, 0, 0, 1, 1, 0, 1, 1) 0
CASE 8  (0, 1, 0, 0, 1, 1, 1, 0, 1) 0
CASE 8  (0, 1, 0, 1, 0, 0, 0, 0, 0) 0
CASE 8  (0, 1, 0, 1, 0, 0, 0, 1, 1) 0
CASE 8  (0, 1, 0, 1, 0, 0, 1, 0, 1) 0
CASE 8  (0, 1, 0, 1, 0, 1, 0, 0, 0) 0
CASE 8  (0, 1, 0, 1, 0, 1, 0, 1, 1) 0
CASE 8  (0, 1, 0, 1, 0, 1, 1, 0, 1) 0
CASE 8  (0, 1, 0, 1, 1, 0, 0, 0, 0) 0
CASE 8  (0, 1, 0, 1, 1, 0, 0, 1, 1) 0
CASE 8  (0, 1, 0, 1, 1, 0, 1, 0, 1) 0
CASE 8  (0, 1, 0, 1, 1, 1, 0, 0, 0) 0
CASE 8  (0, 1, 0, 1, 1, 1, 0, 1, 1) 0
CASE 8  (0, 1, 0, 1, 1, 1, 1, 0, 1) 0

CASE 8  (0, 1, 1, 0, 0, 0, 0, 1, 0) 0
CASE 8  (0, 1, 1, 0, 0, 0, 1, 0, 0) 0
CASE 8  (0, 1, 1, 0, 0, 0, 1, 1, 1) 0
CASE 8  (0, 1, 1, 0, 0, 1, 0, 1, 0) 0
CASE 8  (0, 1, 1, 0, 0, 1, 1, 0, 0) 0
CASE 8  (0, 1, 1, 0, 0, 1, 1, 1, 1) 0
CASE 8  (0, 1, 1, 0, 1, 0, 1, 1, 0) 0
CASE 8  (0, 1, 1, 0, 1, 1, 1, 1, 0) 0
CASE 8  (0, 1, 1, 1, 0, 0, 1, 1, 0) 0
CASE 8  (0, 1, 1, 1, 0, 1, 1, 1, 0) 0
CASE 8  (0, 1, 1, 1, 1, 0, 1, 1, 0) 0
CASE 8  (0, 1, 1, 1, 1, 1, 1, 1, 0) 0

CASE 8  (1, 0, 0, 0, 0, 0, 0, 0, 0) 0
CASE 8  (1, 0, 0, 0, 0, 0, 0, 1, 1) 0
CASE 8  (1, 0, 0, 0, 0, 0, 1, 0, 1) 0
CASE 8  (1, 0, 0, 0, 0, 1, 0, 0, 0) 0
CASE 8  (1, 0, 0, 0, 0, 1, 0, 1, 1) 0
CASE 8  (1, 0, 0, 0, 0, 1, 1, 0, 1) 0
CASE 8  (1, 0, 0, 0, 1, 0, 0, 1, 0) 0
CASE 8  (1, 0, 0, 0, 1, 0, 1, 0, 0) 0
CASE 8  (1, 0, 0, 0, 1, 0, 1, 1, 1) 0
CASE 8  (1, 0, 0, 0, 1, 1, 0, 1, 0) 0
CASE 8  (1, 0, 0, 0, 1, 1, 1, 0, 0) 0
CASE 8  (1, 0, 0, 0, 1, 1, 1, 1, 1) 0
CASE 8  (1, 0, 0, 1, 0, 0, 0, 1, 0) 0
CASE 8  (1, 0, 0, 1, 0, 0, 1, 0, 0) 0
CASE 8  (1, 0, 0, 1, 0, 0, 1, 1, 1) 0
CASE 8  (1, 0, 0, 1, 0, 1, 0, 1, 0) 0
CASE 8  (1, 0, 0, 1, 0, 1, 1, 0, 0) 0
CASE 8  (1, 0, 0, 1, 0, 1, 1, 1, 1) 0
CASE 8  (1, 0, 0, 1, 1, 0, 0, 1, 0) 0
CASE 8  (1, 0, 0, 1, 1, 0, 1, 0, 0) 0
CASE 8  (1, 0, 0, 1, 1, 0, 1, 1, 1) 0
CASE 8  (1, 0, 0, 1, 1, 1, 0, 1, 0) 0
CASE 8  (1, 0, 0, 1, 1, 1, 1, 0, 0) 0
CASE 8  (1, 0, 0, 1, 1, 1, 1, 1, 1) 0

CASE 8  (1, 0, 1, 0, 0, 0, 0, 1, 0) 0
CASE 8  (1, 0, 1, 0, 0, 0, 1, 0, 0) 0
CASE 8  (1, 0, 1, 0, 0, 0, 1, 1, 1) 0
CASE 8  (1, 0, 1, 0, 0, 1, 0, 1, 0) 0
CASE 8  (1, 0, 1, 0, 0, 1, 1, 0, 0) 0
CASE 8  (1, 0, 1, 0, 0, 1, 1, 1, 1) 0
CASE 8  (1, 0, 1, 0, 1, 0, 0, 0, 0) 0
CASE 8  (1, 0, 1, 0, 1, 0, 0, 1, 1) 0
CASE 8  (1, 0, 1, 0, 1, 0, 1, 0, 1) 0
CASE 8  (1, 0, 1, 0, 1, 1, 0, 0, 0) 0
CASE 8  (1, 0, 1, 0, 1, 1, 0, 1, 1) 0
CASE 8  (1, 0, 1, 0, 1, 1, 1, 0, 1) 0
CASE 8  (1, 0, 1, 1, 0, 0, 0, 0, 0) 0
CASE 8  (1, 0, 1, 1, 0, 0, 0, 1, 1) 0
CASE 8  (1, 0, 1, 1, 0, 0, 1, 0, 1) 0
CASE 8  (1, 0, 1, 1, 0, 1, 0, 0, 0) 0
CASE 8  (1, 0, 1, 1, 0, 1, 0, 1, 1) 0
CASE 8  (1, 0, 1, 1, 0, 1, 1, 0, 1) 0
CASE 8  (1, 0, 1, 1, 1, 0, 0, 0, 0) 0
CASE 8  (1, 0, 1, 1, 1, 0, 0, 1, 1) 0
CASE 8  (1, 0, 1, 1, 1, 0, 1, 0, 1) 0
CASE 8  (1, 0, 1, 1, 1, 1, 0, 0, 0) 0
CASE 8  (1, 0, 1, 1, 1, 1, 0, 1, 1) 0
CASE 8  (1, 0, 1, 1, 1, 1, 1, 0, 1) 0

CASE 8  (1, 1, 0, 0, 0, 0, 0, 0, 0) 0
CASE 8  (1, 1, 0, 0, 0, 0, 0, 1, 1) 0
CASE 8  (1, 1, 0, 0, 0, 0, 1, 0, 1) 0
CASE 8  (1, 1, 0, 0, 0, 1, 0, 0, 0) 0
CASE 8  (1, 1, 0, 0, 0, 1, 0, 1, 1) 0
CASE 8  (1, 1, 0, 0, 0, 1, 1, 0, 1) 0
CASE 8  (1, 1, 0, 0, 1, 0, 0, 0, 1) 0
CASE 8  (1, 1, 0, 0, 1, 1, 0, 0, 1) 0
CASE 8  (1, 1, 0, 1, 0, 0, 0, 0, 1) 0
CASE 8  (1, 1, 0, 1, 0, 1, 0, 0, 1) 0
CASE 8  (1, 1, 0, 1, 1, 0, 0, 0, 1) 0
CASE 8  (1, 1, 0, 1, 1, 1, 0, 0, 1) 0

CASE 8  (1, 1, 1, 0, 0, 0, 0, 0, 0) 0
CASE 8  (1, 1, 1, 0, 0, 0, 0, 1, 1) 0
CASE 8  (1, 1, 1, 0, 0, 0, 1, 0, 1) 0
CASE 8  (1, 1, 1, 0, 0, 1, 0, 0, 0) 0
CASE 8  (1, 1, 1, 0, 0, 1, 0, 1, 1) 0
CASE 8  (1, 1, 1, 0, 0, 1, 1, 0, 1) 0
CASE 8  (1, 1, 1, 0, 1, 0, 0, 1, 0) 0
CASE 8  (1, 1, 1, 0, 1, 0, 1, 0, 0) 0
CASE 8  (1, 1, 1, 0, 1, 0, 1, 1, 1) 0
CASE 8  (1, 1, 1, 0, 1, 1, 0, 1, 0) 0
CASE 8  (1, 1, 1, 0, 1, 1, 1, 0, 0) 0
CASE 8  (1, 1, 1, 0, 1, 1, 1, 1, 1) 0
CASE 8  (1, 1, 1, 1, 0, 0, 0, 1, 0) 0
CASE 8  (1, 1, 1, 1, 0, 0, 1, 0, 0) 0
CASE 8  (1, 1, 1, 1, 0, 0, 1, 1, 1) 0
CASE 8  (1, 1, 1, 1, 0, 1, 0, 1, 0) 0
CASE 8  (1, 1, 1, 1, 0, 1, 1, 0, 0) 0
CASE 8  (1, 1, 1, 1, 0, 1, 1, 1, 1) 0
CASE 8  (1, 1, 1, 1, 1, 0, 0, 1, 0) 0
CASE 8  (1, 1, 1, 1, 1, 0, 1, 0, 0) 0
CASE 8  (1, 1, 1, 1, 1, 0, 1, 1, 1) 0
CASE 8  (1, 1, 1, 1, 1, 1, 0, 1, 0) 0
CASE 8  (1, 1, 1, 1, 1, 1, 1, 0, 0) 0
CASE 8  (1, 1, 1, 1, 1, 1, 1, 1, 1) 0
'''