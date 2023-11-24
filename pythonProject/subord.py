list1 =list()
list2 = ["Good at 4","wake at 7","work at 6","sleep at 11"]
dictionary = dict()
for strings in list2:
    p =""
    for j in strings:
        if(j.isdigit()):
            p +=j
    dictionary[p] = strings
    list1.append(p)
subord = list()
for i in list1:
    num = int(i)
    subord.append(num)
subord.sort(reverse=True)
subord2 = list()
for i in subord:
    char = str(i)
    subord2.append(char)
print(subord2)
dictionary2 = dict()
for char in subord2:
    for strings2 in list2:
        if char in strings2:
            dictionary2[char] = strings2
list3 = list()
for v in reversed(dictionary.values()):
    list3.append(v)
print(list3)









