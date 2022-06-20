#from itertools import combinations
## Case 1

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

  
def Case1_output (x, y, z):
  return OR((AND(x, y)),(AND((XOR(y, z)),(z))))


#test1  = [[],[],[]]


#test1 = [[False,False,False],[False, False, True],[False, True, False],[True,False,False],[False, True, True],[True, False, True],[True, True, False],[True, True, True]]


import itertools

bools = [True,False]
result = itertools.product(bools, repeat=3)

for i in result:
  print(i)
  print(Case1_output(i[0],i[1],i[2]))





#for i in test1:
#  print(Case1_output(i[0],i[1],i[2]))

#print(combinations([0,1], 3))
