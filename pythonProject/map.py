number = [2,4,6,8,10,12]

def squre(number):
    return number*number
squre = map(squre,number)
squre2 = list(squre)
print(squre2)

def calculate(n):
    return n*n

result = map(calculate,number)
print(result)
numsqure = set(result)
print(numsqure)

number = (1,3,5,7,9)
result = map(lambda x:x*x,number)
print(result)

num1 = [4,5,6]
num2 = [5,6,7]

result = map(lambda n1,n2:n1+n2,num1,num2)
print(list(result))

def check_even(number):
    if number%2==0:
        return True
    return False

number = [1,2,3,4,5,6,7,8,9,10]
eve_num = filter(check_even,number)
eve = list(eve_num)
print(eve)

letter = ['a','b','d','e','i','j','o']

def filt_vowel(letter):
    vowel = ['a','e','i','o','u']
    return  True if letter in vowel else False
vowel = filter(filt_vowel,letter)
print(vowel)
print(list(vowel))

number = [1,2,3,4,5,6,7]
eve_number_ite = filter(lambda x:(x%2==0),number)
print(eve_number_ite)
print(list(eve_number_ite))

random_list = [1, 'a', 0, False, True, '0']

filtered_iterator = filter(None, random_list)

filtered_list = list(filtered_iterator)

print(filtered_list)
