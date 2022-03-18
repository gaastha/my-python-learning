num=5
fact=1
if num<1: 
    print("Factorial does'nt exist for negative number")
elif num==0: 
    print("Factorial is 1")
else: 

    for i in range(1,num+1): 
        fact=fact* i
print("The factorial of number is",fact)