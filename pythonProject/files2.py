import os
print(os.getcwd())
print(os.listdir())


with open('test.txt','r') as file2:
    read_content = file2.read()
    print(read_content)
file2.close()
with open('test.txt','a') as file2:
    file2.write('i am from nadiad')
    file2.close()
with open('test.txt','r') as file2:
    read_content = file2.read()
    print(read_content)
    file2.close()

import os
