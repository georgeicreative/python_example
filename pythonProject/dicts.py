squre_dict = {num:num*num for num in range(1,6)}
print(squre_dict)
old_price = {'milk':1.20,'coffe':2.5,'bread':2.5}
doller_pond = 0.76
new_price = {item:value*doller_pond for (item,value) in old_price.items()}
print(new_price)

original = {'jack':38,'michael':29,'guedo':32,'john':21}
even_dict = {k:v for (k,v) in original.items() if v % 2 == 0}
print(even_dict)

original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)

ori_dic = {'jack':38,'michael':48,'guido':57,'john':33}
new_dict1 = {k:('old' if v >40 else 'young')
             for (k,v) in ori_dic.items()}
print(new_dict1)

dictionary = { k1:{k2:k1*k2 for k2 in range(1,6)}for k1 in range(2,5)}
print(dictionary)

dictionary = dict()
for k1 in range(11,16):
    dictionary[k1] = {k2:k1*k2 for k2 in  range(1,6)}
print(dictionary)