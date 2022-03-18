'''Write a program to print the following start pattern using the for loop
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * 
* * * 
* * 
*'''

rows=5
for i in range(0,rows): 
    for j in range(i+1): 
        print("*",end="\t")
    print("\n")

for i in range(rows,0,-1): 
    for j in range(0,i-1):
        print("*",end="\t")
    print("\n")
