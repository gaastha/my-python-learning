'''Write a program to calculate the sum of series up to n term. For example, 
if n =5 the series will become 2 + 22 + 222 + 2222 + 22222 = 24690'''

n=int(input())
start=2
sum_seq=0
for i in range(1,n+1): 
    sum_seq+=start 
    start=start*10+2
print("Sum Sequence ",sum_seq)

