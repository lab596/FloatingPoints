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
    return -x - (y | z) != -(y | x)


def Case2_output(x, y, z, w):
    ''' returns True if the operation is non-associative'''
    return (not z and not y) or (x and not w) or (y and not w) or (w and not x)


def Case3_output(x, y, z, a, b):
    #returns True if the operation is non-associatives
    return -(y | z) + a != -(x | y) + b


#A'D'E + C'DE' + CD'E + BD'E + BDE' + ADE' + A'B'CD' + A'B'CE + AB'C'E' + AB'C'D


def Case3_check(A, B, C, D, E):
    #returns True if the operation is non-associatives
    return ((not A) and (not D and E)) or (
        (not C) and D and
        (not E)) or (C and (not D) and E) or (B and (not D) and E) or (
            B and D and (not E)) or (A and D and (not E)) or (
                (not A) and (not B) and C and
                (not D)) or (not A) and (not B) and C and E or A and (
                    not B) and (not C) and (not E) or (not B) and (not C) and D


#y = A'D'E + C'DE' + CD'E + BD'E + BDE' + ADE' + A'B'CD' + A'B'CE + AB'C'E' + AB'C'D


def Case4_output(x, y, z, a, w, b):
    if (not ((y or z)) and a):
        print(str(2))
        return 2
    else:
        return -x - (y | z) + a != -1 - w + b


#y = A'DE'F + ADE'F' + ADEF + A'CD'E'F' + A'CD'EF + A'BD'E'F' + A'BD'EF + ACD'EF' + ABD'EF' + A'B'C'E'F + AB'C'E'F' + AB'C'EF
#Simplified: ADEF+ABCEF

#simplified: AEF+ADF+ADE+DEF+ABCF+ABCE+BCEF


def Case4_check(x, y, z, a, w, b):
    return (x and w and b) or (x and a and b) or (x and a and w) or (
        a and w and b) or (x and y and z and b) or (x and y and z
                                                    and w) or (y and z and w
                                                               and b)


def Case5_output(b2, gamma, sigma, a2p, a3, beta):
    return -b2 + gamma - sigma - (a2p or a3) != -(sigma or a2p or b2) + beta


import itertools


def Case6_output(b2, a2p, a3, gamma, sigma, V, delta):
    return -b2 - (a2p or a3) + gamma - sigma != -1 - V + delta


def Case7_output(b2, sigma, gamma, a2p, a3, theta, beta, beta2):
    return -b2 - ((not gamma) & sigma) + (
        (sigma ^ gamma) ^ (a2p or a3)) != (sigma or a2p or a3) + beta + beta2


def Case7_check(b2, sigma, gamma, a2p, a3, theta, beta, beta2):
    part1 = b2 or sigma or gamma or beta or beta2
    part2 = b2 or sigma or not gamma or a2p or a3 or not (beta ^ beta2)
    part3 = b2 or not sigma or not gamma or not (a2p or a3) or beta or beta2
    part4 = not b2 or sigma or not gamma or a2p or a3 or beta or beta2
    return part1 and part2 and part3 and part4


def Case8_output(b2, sigma, gamma, a2p, a3, theta, beta, beta2, V):
    return -b2 - ((not gamma) & sigma) + ((sigma ^ gamma) ^
                                          (a2p or a3)) != -1 - V + beta + beta2


import itertools

bools = [0, 1]
"""
arr1 = []
result = itertools.product(bools, repeat=3)
for i in result:
    print("CASE 1 ", i, int(Case1_check(*i)))
    arr1.append(int(Case1_check(*i)))
print()
print("arr1: " + str(arr1))

result = itertools.product(bools, repeat=3)
for i in result:
    print("case 1 Logic:", i, int(Case1_output(*i)))
print()

result = itertools.product(bools, repeat=4)
for i in result:
    print("CASE 2 ", i, int(Case2_output(*i)))
print()

arr3 = []
result = itertools.product(bools, repeat=5)
for i in result:
    print("CASE 3 ", i, int(Case3_output(*i)))
    arr3.append(int(Case3_output(*i)))
print()
print("arr3: " + str(arr3))

result = itertools.product(bools, repeat=5)
for i in result:
    print("case 3 check", i, int(Case3_check(*i)))
print()

result = itertools.product(bools, repeat=6)
for i in result:
    print("case 4 check", i, int(Case4_check(*i)))
print()

arr4 = []
result = itertools.product(bools, repeat=6)
for i in result:
    testcase = Case4_output(*i)
    if testcase < 2:
        print("CASE 4 ", str(i), int(Case4_output(*i)))
        arr4.append(int(Case4_output(*i)))
print()
print("arr4: " + str(arr4))

arr5 = []
result = itertools.product(bools, repeat=6)
for i in result:
    print("CASE 5 ", i, int(Case5_output(*i)))
    arr5.append(int(Case5_output(*i)))
print()
print("arr5: " + str(arr5))

arr6 = []
result = itertools.product(bools, repeat=7)
for i in result:
  if int(Case6_output(*i)) == 0:
    print("CASE 6 ", i, int(Case6_output(*i)))
    arr6.append(int(Case6_output(*i)))
print()
print("ARR6: " + str(arr6))

arr7 = []
result = itertools.product(bools, repeat=8)
for i in result:
    #if int(Case7_output(*i)) == 0:
        print("CASE 7 ", i, int(Case7_output(*i)))
        arr7.append(int(Case7_output(*i)))
print()
print("ARR7: " + str(arr7))

arr7c = []
result = itertools.product(bools, repeat=8)
for i in result:
    #if int(Case7_check(*i)) == 0:
        print("CASE 7 Check", i, int(Case7_check(*i)))
        arr7c.append(int(Case7_check(*i)))
print()
print("ARR7: " + str(arr7c))
"""
arr8 = []
log8 = []
result = itertools.product(bools, repeat=9)
count0 = 0
count1 = 0
for i in result:
    #    if int(Case8_output(*i)) == 0:
    if bool(i[0]) and bool(i[1]) and bool(i[2]):
        print("CASE 8 ", i, int(Case8_output(*i)))
        arr8.append(int(Case8_output(*i)))
        if int(Case8_output(*i)) == 1:
            log8.append(i)

print()
print("ARR8 (111): " + str(arr8))
print("count0: " + str(count0))
print("count1: " + str(count1))
"""

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
    newString = []
    finalOr = []
    finalBool = 0

    ## splits each AND statement into an array of letters, e.g. ["A", "B", "'"] <- ["AB'"]
    for i in brokenString:
        arr = []
        for j in i:
            arr.append(j)
        newString.append(arr)

    for i in newString:
        a = 1
        for j in range(len(i)):
            if (j + 2) <= len(i):
                if i[j] != "'" and i[j + 1] != "'":
                    a = a and variables[i[j]]
                elif i[j] != "'" and i[j + 1] == "'":
                    a = a and not variables[i[j]]

        if (i[len(i) - 1]) != "'":
            a = a and (variables[i[len(i) - 1]])
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

def Case_checker_check(A, B,C,D,E,F):
    #returns True if the operation is non-associative
    #return (x and y) or (not y and z)
    return convert_string_to_boolean([
        A, B,C,D,E,F], "A'BD'E'F' + BC"
                                     )

result = itertools.product(bools, repeat=6)
for i in result:
    print("case 5 check:", i, int(Case5_check(*i)))
    arr5c.append(int(Case5_check(*i)))
print()
print("arr5c: " + str(arr5c))


result = itertools.product(bools, repeat=6)
for i in result:
    print("case checker:", i, int(Case_checker_check(*i)))
    #arr5c.append(int(Case_checker_check(*i)))
print()
#print("arr5c: " + str(arr5c))



def arrayOb(arr1, arr2):
    for i in range(len(arr1)):
        if (arr1[i] != arr2[i]):
            print(str(i) + "Not equal.")
    print("Equal.")


arrayOb(arr5, arr5c)
arrayOb(arr6, arr6c)

"""

#y = D'E' + D'F + E'F + BD' + BE' + BF + AD' + AE' + AF + A'B'DEF'

#000
#y = D'E' + D'F + E'F + BD' + BE' + BF + AD' + AE' + AF + A'B'DEF'

#001
#y = D'E' + D'F + E'F + A'B'D' + A'B'E' + A'B'F + BDEF' + ADEF'

#010
#y = D'E'F + DEF' + BEF' + BDF' + BDE + AEF' + ADF' + ADE + A'B'D'E' + A'B'D'F + A'B'E'F

#Same as 000
#011
#y = D'E' + D'F + E'F + BD' + BE' + BF + AD' + AE' + AF + A'B'DEF'

#100
#y = D'E'F + DEF' + BD'E' + BD'F + BE'F + AD'E' + AD'F + AE'F + A'B'EF' + A'B'DF' + A'B'DE

#Same as 010
#101
#y = D'E'F + DEF' + BEF' + BDF' + BDE + AEF' + ADF' + ADE + A'B'D'E' + A'B'D'F + A'B'E'F

#110
#y = EF' + DF' + DE + BF' + BE + BD + AF' + AE + AD + A'B'D'E'F

#Same as 100
#111
#y = D'E'F + DEF' + BD'E' + BD'F + BE'F + AD'E' + AD'F + AE'F + A'B'EF' + A'B'DF' + A'B'DE

########################################################################################################
#000 011
#y = [(B2'σ'Γ' + B2'σΓ)(β'β2' + β'V + β2'V + A2p3β' + A2p3β2' + A2p3V + A2pβ' + A2pβ2' + A2pV + A2p'A2p3'ββ2V')]

#001
#y = [(B2'σ'Γ)(β'β2' + β'V + β2'V + A2p'A2p3'β' + A2p'A2p3'β2' + A2p'A2p3'V + A2p3ββ2V' + A2pββ2V')]

#010 101
#y = [(B2'σΓ' + B2σ'Γ)(β'β2'V + ββ2V' + A2p3β2V' + A2p3βV' + A2p3ββ2 + A2pβ2V' + A2pβV' + A2pββ2 + A2p'A2p3'β'β2' + A2p'A2p3'β'V + A2p'A2p3'β2'V)]



#100 111
#y = [(B2σ'Γ' + B2σΓ)(β'β2'V + ββ2V' + A2p3β'β2' + A2p3β'V + A2p3β2'V + A2pβ'β2' + A2pβ'V + A2pβ2'V + A2p'A2p3'β2V' + A2p'A2p3'βV' + A2p'A2p3'ββ2)]



#110
#y = [(B2σΓ')(β2V' + βV' + ββ2 + A2p3V' + A2p3β2 + A2p3β + A2pV' + A2pβ2 + A2pβ + A2p'A2p3'β'β2'V)]



#final = [(B2'σ'Γ' + B2'σΓ)(β'β2' + β'V + β2'V + A2p3β' + A2p3β2' + A2p3V + A2pβ' + A2pβ2' + A2pV + A2p'A2p3'ββ2V')] 
#+   
#[(B2'σ'Γ)(β'β2' + β'V + β2'V + A2p'A2p3'β' + A2p'A2p3'β2' + A2p'A2p3'V + A2p3ββ2V' + A2pββ2V')]
#+   
#[(B2'σΓ' + B2σ'Γ)(β'β2'V + ββ2V' + A2p3β2V' + A2p3βV' + A2p3ββ2 + A2pβ2V' + A2pβV' + A2pββ2 + A2p'A2p3'β'β2' + A2p'A2p3'β'V + A2p'A2p3'β2'V)]  
#+   
#[(B2σ'Γ' + B2σΓ)(β'β2'V + ββ2V' + A2p3β'β2' + A2p3β'V + A2p3β2'V + A2pβ'β2' + A2pβ'V + A2pβ2'V + A2p'A2p3'β2V' + A2p'A2p3'βV' + A2p'A2p3'ββ2)]
#+
#[(B2σΓ')(β2V' + βV' + ββ2 + A2p3V' + A2p3β2 + A2p3β + A2pV' + A2pβ2 + A2pβ + A2p'A2p3'β'β2'V)]
