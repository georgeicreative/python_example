num = [1,2,3,4,5]
numbs0,numbs, *numbs2 = num
print("numbs",numbs0)
print("numbs",numbs)
print("numbs",numbs2)

chars = ['g','g','g','e','o','r','e']
print("chars",chars.count('e'))

for i in range(chars.count('g')):
    chars.remove('g')

print("chars",chars)


