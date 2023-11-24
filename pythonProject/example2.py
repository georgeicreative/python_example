def pypart(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
n = 5
pypart(n)

def triangle(n):
    k = n-1
    for i in range(0,n):

        for j in range(0,k):
            print(end=" ")
        k = k-1
        for j in range(0,i+1):
            print("* ",end="")
        print("\r")
n = 5
triangle(n)
for i in range(0,10):
    print("*",end="  ")
    print("\r")
k=5
for i in range(0,5):
    for s in range(0,k-i):
        print(end=" ")
    for j in range(0,i):
        print("*",end="")
    print("\r")

#string method

sentence = 'i Love PYTHON'
cs = sentence.capitalize()
print(cs)
ces = sentence.center(24,'*')
print(ces)
res = 'PyThon'
print(res.casefold())
print(sentence.count('o'))
print(sentence.endswith('N'))
str = 'xyz\tabc\t123'
print(str.expandtabs())
print(sentence.find('Le'))
print("hello {} do you have{}".format('george',123))
print("hello {name} do you have {blc}".format(name='george234',blc=123.45))

name1 = 'python321'
name2 = 'python 21'
print(name1.isalnum())
print(name2.isalnum())
import datetime

now = datetime.datetime.now()
print(now)

import datetime
current = datetime.date.today()
print(current)

print(dir(datetime))
from  datetime import date
d = date(2000,10,29)
print(d)