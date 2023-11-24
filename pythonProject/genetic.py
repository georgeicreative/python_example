prime_number = [11,7,3,5,2]
prime_number2 = [11,7,3,5,2]

chars = ['1','8','7','9','11','22','13','10','14']
chars.sort()
prime_number.sort(reverse=True)
prime_number2.sort()
print(prime_number)
print(prime_number2)
print(chars)

vowels = ['e','a','u','o','i']
vowels.sort()
print(vowels)
nums = [8,3,12,14,16,9,6]
nums2 = sorted(nums)
print(nums2)

def takeSecond(elem):
    return elem[1]
random = [(2,2),(3,4),(4,1),(1,3)]
print(random[3])
random.sort(key=takeSecond)

print(random)

employee = [
    {'Name':'Alan Turing','Age':25,'salary':10000},
    {'Name': 'Shanon Lin', 'Age': 30, 'salary': 8000},
    {'Name': 'John Hopkings', 'Age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tail', 'Age': 40, 'salary': 15000},
]

def get_name(employee):
    return employee.get('Name')
def get_age(employee):
    return employee.get('Age')
def get_salary(employee):
    return employee.get('salary')
employee.sort(key = get_name)
print(employee,end = '\n\n')

employee.sort(key = get_age)
print(employee,end = "\n\n")

employee.sort(key = lambda x:x.get('Name'))
print(employee,end='\n\n')

numbers = [4,2,11,18,13,17,19]
sorted_nums = sorted(numbers)
print(sorted_nums)

py_list = ['e','a','u','i','o']
pl = sorted(py_list)
print(pl)

py_strig = 'python'
pl2 = sorted(py_strig)
print(pl2)

py_dict = {'e':1,'a':2,'u':3,'o':4,'i':5}
print(sorted(py_dict,reverse = False))

random = [(2,2),(3,4),(4,1),(1,3)]
sorted_list = sorted(random,key = takeSecond)
print('Sorted list=',sorted_list)

partician_list = [('Alison',50,18),
                  ('Terence',75,12),
                  ('David',75,20),
                  ('Jimmy',90,22),
                  ('John',45,12)]
language = ['java','python','javascript']
version = [14,3,6]

result1 = zip(language,version)
result2 = zip(version,language)

print(list(result1))
print(list(result2))

coordinate = ['x','y','z']
value = [3,4,5]

result = zip(coordinate,value)
result_list = list(result)
print(result_list)

c,v = zip(*result_list)
print('c =',c)
print('v =',v)

boolean_list = ['True', 'False', 'True']

result = any(boolean_list)
print(result)

l = [1, 3, 4, 0]
print(any(l))

l = [0, False]
print(any(l))

l = [0, False, 5]
print(any(l))

l = []
print(any(l))

numbers = [9, 34, 11, -4, 27,-6]

min_number = min(numbers)
print(min_number)

numbers2 = [2,3,-5,6,9,-7]
min2 = min(numbers2)
print(min2)

languages = ["Python", "C Programming", "Java", "JavaScript"]
smallest_string = min(languages);

print("The smallest string is:", smallest_string)
