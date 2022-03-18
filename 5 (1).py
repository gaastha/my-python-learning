'''Write a program to display only those numbers from a list that satisfy the following conditions

The number must be divisible by five
If the number is greater than 150, then skip it and move to the next number
If the number is greater than 500, then stop the loop'''

list=[]
n=int(input("Enter the value of n:"))
for i in range(1,n+1):
    l=int(input())
    list.append(l)

print("The list of element that follow the condition")

for i in list: 
    if i%5==0: 
        print(i)
    elif i>150: 
        i=i+1
    elif i>500: 
        break
    else: 
        pass