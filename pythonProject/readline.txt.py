with open('name.txt','r') as f:
    content = f.readlines()
print(content)
contents = [x.strip() for x in content]
print(contents)

with open('name.txt','a') as names:
    names.write('\nwalkswagan 3035')
names.close()
with open('name.txt','r') as names:
    content = names.read()
    print(content)