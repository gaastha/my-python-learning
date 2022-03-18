'''Reverse a given integer number'''

n=int(input("Enter the value of n: "))
rem=0
rev=0
while n>0: 
    rem=n%10
    rev=(rev*10)+rem 
    n=n//10 
print("The reverse of n is "+str(rev))
