print('I Love {} for "{}"!'.format('Greeks','Greeks2'))
print('{0} and {1}'.format('Greek','Portal'))
print('{1} and {0}'.format('Greek','Portal'))
print(f"I Love {'Greek'} for \"{'Greek'}!\"")

print('Number one portal is {0},{1} and {other}.'.format('Greek','For',other='Greek'))

print("Greek :{0:2d}, Portal :{1:9.2f}".format(12,546))

print("Second argument: {1:3d}, first one: {0:7.2f}".
      format(47.42, 11))

print("Geeks: {a:5d},  Portal: {p:8.2f}".
      format(a=453, p=59.058))

tab = {'geeks': 41.27, 'for': 4098, 'geek': 8637678}

print('Geeks: {0[geeks]:2.1f}; For: {0[for]:d}; '
    'Geeks: {0[geek]:d}'.format(tab))
data = dict(fun="greekforgreek",adj="Portal",ver="good")
print("I Love {fun} computer {adj} and {ver}".format(**data))
str = 'I Love Greek For Greek'
str2 = 'Love'
print(str.center(40,'#'))
print(str2.center(12,"*"))
print(str.ljust(40,"%"))
