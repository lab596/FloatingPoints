def Case1_output(x, y, z):
    #returns True if the operation is non-associative
    return (x and y) or (not y and z)

    '''          y^z  & z
    yz = 00       0
    yz = 01       1 -> 1
    yz = 10       1 -> 0
    yz = 11       0
    '''


def Case2_output(x, y, z, w):
    ''' returns True if the operation is non-associative'''
    return (not z and not y) or (x and not w) or (y and not w) or (w and not x)


def Case3_output(x,y,z,a,b):
    #returns True if the operation is non-associatives
    return -(y | z) + a != -(x | y) + b
#A'D'E + C'DE' + CD'E + BD'E + BDE' + ADE' + A'B'CD' + A'B'CE + AB'C'E' + AB'C'D



def Case4_output(x, y, z, a, w, b):
    if(not((y or z)) and a):
      print(y,z,a)
      return 2
    else:
      return 
#y = A'DE'F + ADE'F' + ADEF + A'CD'E'F' + A'CD'EF + A'BD'E'F' + A'BD'EF + ACD'EF' + ABD'EF' + A'B'C'E'F + AB'C'E'F' + AB'C'EF

import itertools

bools = [0, 1]

result = itertools.product(bools, repeat=3)
for i in result:
    print("case 1", i, int(Case1_output(*i)))
print()

result = itertools.product(bools, repeat=4)
for i in result:
    print("case 2", i, int(Case2_output(*i)))
print()

result = itertools.product(bools, repeat=5)
for i in result:
    print("case 3", i, int(Case3_output(*i)))
print()

result = itertools.product(bools, repeat=6)
for i in result:
    testcase = int(Case4_output(*i))
    if testcase<2:
      print("case 4", i, int(Case4_output(*i)))
print()


#Case 4
#y = A'DE'F + ADE'F' + ADEF + A'CD'E'F' + A'CD'EF + A'BD'E'F' + A'BD'EF + ACD'EF' + ABD'EF' + A'B'C'E'F + AB'C'E'F' + AB'C'EF
#Simplified: ADEF+ABCEF
#Case 3
#A'D'E + C'DE' + CD'E + BD'E + BDE' + ADE' + A'B'CD' + A'B'CE + AB'C'E' + AB'C'D
#Simplified: ADE + CDE + BDE + ABCD + ABCE
