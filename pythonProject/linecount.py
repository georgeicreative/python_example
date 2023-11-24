def file_len(fname):
    with open(fname) as f:
        for i,l in enumerate(f):
            pass
        return  i+1
print(file_len('test.txt'))

import glob,os
for file in glob.glob('*.txt'):
    print(file)
greet = lambda :print('Hello World')
greet()

greet_user = lambda name:print('Hey....',name)
greet_user('george')

