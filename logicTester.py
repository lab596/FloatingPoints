def Case1_check(x, y, z):
    #returns True if the operation is non-associative
    #return (x and y) or (not y and z)
    return ((not y) & z | (x & y)) 
    #y = B'C + AB

    '''          y^z  & z
    yz = 00       0
    yz = 01       1 -> 1
    yz = 10       1 -> 0
    yz = 11       0
    '''

def Case1_output(x, y, z):
    #returns True if the operation is non-associative
    return -x - (y | z) !=  -(y | x)

def Case2_output(x, y, z, w):
    ''' returns True if the operation is non-associative'''
    return (not z and not y) or (x and not w) or (y and not w) or (w and not x)


def Case3_output(x,y,z,a,b):
    #returns True if the operation is non-associatives
    return -(y | z) + a != -(x | y) + b
#A'D'E + C'DE' + CD'E + BD'E + BDE' + ADE' + A'B'CD' + A'B'CE + AB'C'E' + AB'C'D
  
def Case3_check(A,B,C,D,E):
    #returns True if the operation is non-associatives
    return ((not A) and (not D and E)) or ((not C) and D and (not E)) or (C and (not D) and E) or (B and (not D) and E) or (B and D and (not E)) or (A and D and (not E)) or ((not A) and (not B) and C and (not D)) or (not A) and (not B) and C and E or A and (not B) and (not C) and (not E) or (not B) and (not C) and D
#y = A'D'E + C'DE' + CD'E + BD'E + BDE' + ADE' + A'B'CD' + A'B'CE + AB'C'E' + AB'C'D


def Case4_output(x,y,z,a,w,b):
    if(not((y or z)) and a):
      print(str(2))
      return 2
    else:
      return -x - (y | z) + a != -1 - w + b
#y = A'DE'F + ADE'F' + ADEF + A'CD'E'F' + A'CD'EF + A'BD'E'F' + A'BD'EF + ACD'EF' + ABD'EF' + A'B'C'E'F + AB'C'E'F' + AB'C'EF
      #Simplified: ADEF+ABCEF

#simplified: AEF+ADF+ADE+DEF+ABCF+ABCE+BCEF

def Case4_check(x,y,z,a,w,b):
  return (x and w and b) or (x and a and b) or (x and a and w) or (a and w and b) or (x and y and z and b) or (x and y and z and w) or (y and z and w and b)

def Case5_output(b2,gamma,sigma,a2p,a3,beta):
  return -b2 + gamma - sigma - (a2p or a3) != -(sigma or a2p or b2) + beta

import itertools

bools = [0, 1]

arr1 = []
result = itertools.product(bools, repeat=3)
for i in result:
    print("case 1", i, int(Case1_check(*i)))
    arr1.append(int(Case1_check(*i)))
print()
print("arr1: "+ str(arr1))


result = itertools.product(bools, repeat=3)
for i in result:
    print("case 1 Logic:", i, int(Case1_output(*i)))
print()

result = itertools.product(bools, repeat=4)
for i in result:
    print("case 2", i, int(Case2_output(*i)))
print()

arr3 = []
result = itertools.product(bools, repeat=5)
for i in result:
    print("case 3", i, int(Case3_output(*i)))
    arr3.append(int(Case3_output(*i)))
print()
print("arr3: "+ str(arr3))

result = itertools.product(bools, repeat=5)
for i in result:
    print("case 3 check", i, int(Case3_check(*i)))
print()


result = itertools.product(bools, repeat=6)
for i in result:
    print("case 4 check", i, int(Case4_check(*i)))
print()

arr4  = []
result = itertools.product(bools, repeat=6)
for i in result:
    testcase = Case4_output(*i)
    if testcase<2:
      print("case 4", str(i), int(Case4_output(*i)))
      arr4.append(int(Case4_output(*i)))
print()
print("arr4: "+ str(arr4))

arr5  = []
result = itertools.product(bools, repeat=6)
for i in result:
    print("case 5 ", i, int(Case5_output(*i)))
    arr5.append(int(Case5_output(*i)))
print()
print("arr5: "+ str(arr5))




#Case 4
#y = A'DE'F + ADE'F' + ADEF + A'CD'E'F' + A'CD'EF + A'BD'E'F' + A'BD'EF + ACD'EF' + ABD'EF' + A'B'C'E'F + AB'C'E'F' + AB'C'EF
#y = A'EF' + A'DF' + A'DE + DEF' + AE'F + CD'E'F + BD'E'F + ACD'E' + ACD'F + ABD'E' + ABD'F + A'B'C'F' + A'B'C'E + B'C'EF'
#simplified: AEF+ADF+ADE+DEF+ABCF+ABCE+BCEF

#Simplified: ADEF+ABCEF
#Case 3
#A'D'E + C'DE' + CD'E + BD'E + BDE' + ADE' + A'B'CD' + A'B'CE + AB'C'E' + AB'C'D
#Simplified: ADE + CDE + BDE + ABCD + ABCE

#Case 5 - y = B'F + B'D'E + D'EF + B'CD + CDF + AB'D + ADF + AB'C + ACF + ACE + ACD + A'BD'E'F' + BC'D'E'F' + A'BC'DF'

'''
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
'''


#website case 1: y = B'C + AB


###########################################


def convert_string_to_boolean(arr, string):
  
  ## assigns letter to each varible (shown as parameter in end function)
  letterCorrespondant = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
  variables = {}
  type(variables)
  for i in range(len(arr)):
    variables[letterCorrespondant[i]] = arr[i]

  ## splits string
  brokenString = string.split(" + ")
  newString    = []
  finalOr      = []
  finalBool    = 0

  ## splits each AND statement into an array of letters, e.g. ["A", "B", "'"] <- ["AB'"]
  for i in brokenString:
    arr = []
    for j in i:
      arr.append(j)
    newString.append(arr)


  for i in newString:
    a = 1
    for j in range(len(i)):
      if (j+2) <= len(i):
        if i[j] != "'" and i[j+1] != "'":
          a = a and variables[i[j]]
        elif i[j] != "'" and i[j+1] == "'":
          a = a and not variables[i[j]]

    if (i[len(i)-1]) != "'":  
      a = a and (variables[i[len(i)-1]])
      finalOr.append(a)

  for i in finalOr:
    finalBool = finalBool or i

  return int(finalBool)

#example run

A = 1
B = 1
C = 1

array = (A, B, C)

print(convert_string_to_boolean(array, "ABC'+AB'C'"))


arr5c = []

def Case5_check(A, B, C, D, E, F):
    #returns True if the operation is non-associative
    #return (x and y) or (not y and z)
    return convert_string_to_boolean([A, B, C, D, E, F], "B'F + B'D'E + D'EF + B'CD + CDF + AB'D + ADF + AB'C + ACF + ACE + ACD + A'BD'E'F' + BC'D'E'F' + A'BC'DF'")

result = itertools.product(bools, repeat=6)
for i in result:
    print("case 5 check:", i, int(Case5_check(*i)))
    arr5c.append(int(Case5_output(*i)))
print()
print("arr5c: " + str(arr5c))


def arrayOb(arr1, arr2):
  for i in range(len(arr1)):
    if(arr1[i] != arr2[i]):
      print("Not equal.")
  print("Equal.")

arrayOb(arr5, arr5c)
