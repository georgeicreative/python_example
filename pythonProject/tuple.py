zoo = ('python','elephant','penguins')
print('number of animals in the zoo is',len(zoo))
new_zoo = 'monkey','camel',zoo
print(new_zoo)
print("george")
nums = [4,-2,5,0,6,3,2,7]
target = -1
list1 = []
for i in nums:
    for j in nums:
        if (i+j) == target:
            if i not in list1:
                list1.append(i)
            if j not in list1:
                list1.append((j)