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
no_punct = ""
for char in string:
    if char not in pruct:
        no_punct = no_punct + char
print(no_punct)

string2 = "Hello this Is an Example With cased letters"
print(string2.split())
words = [word.lower() for word in string2.split()]
print(words)
words.sort()

print("The sorted order")
for word in words:
    print(word)

string3 = 'Hello, have you tried our tutorial section yet?'
vowels = 'aeiou'
string4 = string3.casefold()
print(string4)

count = {}.fromkeys(vowels,0)
print(count)
for char in string3:
    if char in count:
        count[char] +=1
print(count)

dict1 = {1:'a',2:'b'}
dict2 = {3:'c',4:'d'}
print(dict1 | dict2)

my_list = [23,11,29,37]
for index,val in enumerate(my_list):
    print(index,val)
