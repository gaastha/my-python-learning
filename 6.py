'''Write a program to count the total number of digits in a number using a while loop.'''

number=int(input())
count=0
while number!=0 : 
    number=number//10 
    count=count+1

print("No of  digits in a number are :",count)

