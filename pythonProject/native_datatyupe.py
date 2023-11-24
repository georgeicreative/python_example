x = [[1,2,3],
     [1,2,3],
     [1,2,3]]
y = [[1,2,3],
     [1,2,3],
     [1,2,3]]

result = [[0,0,0],
          [0,0,0],
          [0,0,0]]

print(len(x))
print(len(x[0]))

for i in range(len(x)):
     for j in range(len(x[0])):
          result[i][j] = x[i][j]+y[i][j]

print(x)
print(result)
for  r in result:
     print(r)

x2 = [[2,3],
      [3,4],
      [5,6]]
result2 = [[0,0,0],
           [0,0,0]]
for i in range(len(x2)):
     for j in range(len(x2[0])):
          result2[j][i] = x[i][j]

print(result2)

x3 = [[2,3,4],
      [3,4,5],
      [4,5,6]]
y3 = [[4,5,6],
      [7,5,2],
      [4,8,9]]

result3 = [[0,0,0],
           [0,0,0],
           [0,0,0]]
for i in range(len(x)):
     for j in range(len(y[0])):
          for k in range(len(y)):
               result3[i][j] += x[i][k]*y[k][j]
print(result3)

sting = 'aOA'
newstring = sting.casefold()
print(newstring)
revsting = reversed(newstring)
print(revsting)

if list(newstring) == list(revsting):
     print('String is palindrom')
else:
     print('string is not palindrom')

pruct = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
string = "Hello!!!, he said ---and went."
l1 = list(pruct)
print(l1)
l2 = list(string)
l3 = l2.copy()
print(l2)
print(l3)
l2.remove('!')
print(l2)

for char in l3:
     if char in l1:
          l2.remove(char)
print(l2)

