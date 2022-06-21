#from itertools import combinations
## Case 1

'''
def AND(a, b):
  if (a and b):
    return True
  else:
    return False

def OR(a, b):
  if (a or b):
    return True
  else:
    return False
  
def XOR(a, b):
  if(((a==True) and (b==False)) or ((a==False) and (b==True))):
    return True
  else:
    return False

def NOT(a):
  if a:
    return False
  else:
    return True
'''

  
def Case1_output(x, y, z):
    ''' returns True if the operation is non-associative'''
    # return OR((AND(x, y)),(AND((XOR(y, z)),(z))))
    # return ((x & y) | ((y ^ z) & z))
    # return ((x & y) | (~y & z))
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
    ''' returns True if the operation is non-associative'''
    return -(y | z) + a == -(x | y) + b


def Case4_output():
    # ...
    return


#test1  = [[],[],[]]


#test1 = [[False,False,False],[False, False, True],[False, True, False],[True,False,False],[False, True, True],[True, False, True],[True, True, False],[True, True, True]]


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
    # only print the successful ones
    # if Case3_output(*i):
        # print("case 3", i, int(Case3_output(*i)))
print()



#for i in test1:
#  print(Case1_output(i[0],i[1],i[2]))

#print(combinations([0,1], 3))
