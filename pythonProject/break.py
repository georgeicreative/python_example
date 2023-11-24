my_list  = [1,2,3,4]
count = 0
for i in my_list:
    if i == 3:
        print('Loop is breaked')
        count += 1
        break
    else:
        print('loop is ruuning')
print("count=",count)

mystr = 'python'

for char in mystr:
    if char == 'o':
        print('loop is breaked')
        break
    print(char)
j = 0
while 1:
    print(i,"",end="")
    i = i+1
    if i == 10:
        break
print("came out of loop")

n = 2
print("\n")

while True:
    i = 1
    while i <= 10:
        print("%d X %d = %d"%(n,i,n*i))
        i += 1
    choice = int(input("do you want continued ? press 0 for no:"))
    if choice == 0:
        print('loop is breaked')
        break
    n +=1
print("program succesfully")


