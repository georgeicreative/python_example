num = [1,2,3,4,5]
sq = [n**2 for n in num]
print(sq)

string = 'george2910'
n_letter = [letter for letter in string]
print(n_letter)

cars = ['jaguar','land over','tesla','toyato','tata']
newlist = [x for x in cars if 's' in x]
print(newlist)

new_cars = [x if x != 'tesla' else 'audi' for x in cars]
print(new_cars)

number = [i%2 == 0 for i in range(0,21)]
print(number)
