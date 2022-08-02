def miss(li):
    rli=range(1,max(li)+1)
    a=set(rli)-set(li)
    a=list(a)
    print('input:',li)
    print('output:',end="")
    for i in a :
     print(i,end=",")

li=[1,5,8,6,9,10,11]
miss(li)    