"""1.prime number
n=10;
if n<2:
    print("not prime")
else:
    for i in range(2,n):
        if(n%i==0):
            print("not a prime")
            break
    else:
        print("prime number")
"""
import string

"""2.facotorial
n=10
x=1
for i in range(1,n+1):
    x=x*i
print(x)
"""
"""3.fabanoccii
a,b=0,1
n=9
c=[0]
for i in range (n):
    #print(b,end=" ")
    c.append(b)
    a,b=b,a+b
print(c)
"""
"""4.sum of element in arry
a=[1,2,3,4,5]
b=[]
c=0
for i in a:
    c=c+i
b.append(c)
print(b)
"""
"""5.lenght of list
a=[1,2,3,4,5]
print(len(a))
"""
"""6.swap 1st and last element in list
a=[1,2,3,4,5]
print(a)
c=len(a)
a[0],a[c-1]=a[c-1],a[0]
print (a)
"""
"""7.string palimdrom
a="anna"
if a==a[::-1]:
    print("is palindrom ",a)
else:
    print("not palindram",a)
"""
"""8.2nd largest  element in list 
a=[3,5,6,8,9,7,20]
a.sort()
print(a)
c=len(a)
print(a[c-2])
"""
"""9.length of string
a="mahesh"
print(len(a))
"""
"""10.reverse string
a="mahesh"
print(a[::-1])
"""
"""11.max and min number in list
a=[3,5,6,8,9,7,20]
a.sort()
print(a)
c=len(a)
print("smallest number is",a[0],"largest number is",a[c-1])
"""
a="mahesh68"
b=string.punctuation
bools = list(map(lambda char: char in b,a))
print("Valid") if any(bools) else print("Invalid")