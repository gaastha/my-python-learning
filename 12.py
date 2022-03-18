''' Display Fibonacci series up to 10 terms'''

first=0
second=1
for i in range(10):
    print(first,end=" ")
    res=first+second 
    first=second 
    second=res


