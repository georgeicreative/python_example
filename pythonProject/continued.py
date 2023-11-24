for i in range(2,9):
    if i == 5:
        print("\n")
        print("iterable i = %d is skiped"%(i))
        print("\n")
        continue
    print("iterable i =",i,end = " ")
print("\n")
string = 'javatpoint'

iterable = 0

while iterable < len(string):
    if string[iterable] == 'a':
        iterable += 1
        continue
    print(string[iterable])
    iterable += 1


