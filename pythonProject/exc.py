string = input()

try:
    num = int(input())
    print(string+num)
except(TypeError,ValueError) as e:
    print(e)

from shutil import copyfile
copyfile('/root/test.txt','/root/name.txt')
