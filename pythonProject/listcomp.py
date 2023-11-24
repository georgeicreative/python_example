list1 = [12,24,35,70,88,120,155]

list3 =[list1[x] for x in range(len(list1)) if x not in(0,4,5)]
print(list3)








list2  = [x for(i,x) in enumerate(list1) if i not in (0,4,5)]
