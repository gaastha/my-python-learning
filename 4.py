'''Write a program to print multiplication table of a given number'''

n=int(input("Enter the value of n:"))

for i in range(1,11):
    print(n*i,end="\n")