from re import A


def sum (n):
    a=0
    for i in range(1,n+1) :
        a+=(1/i)
    return a
print(sum(8))