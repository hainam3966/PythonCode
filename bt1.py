import os
# a = input (">> ")
f = open("d:\input.txt","r")
a = f.read()
a=a+" "
b = []
i=d=0
os.system('cls')
while i<(len(a)-1):
    while (a[i]==a[i+1])and(a[i]!=" "):
        d+=1
        i+=1
    if (d!=0): 
        b.append(str(d+1)+a[i])
        d=0
    else:
        if(a[i]!=" "):b.append(a[i])
    i+=1
print(a)
print(b)