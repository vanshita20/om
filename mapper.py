import sys
from functools import reduce
def cont(characters):
return reduce(reducer,map(lambda char:dict([['char',1]]),characters))
def reducer(i,j):
for k in j:
i[k]=i.get(k,0)+j.get(k,0)
return i
print(cont("the code is running"))
