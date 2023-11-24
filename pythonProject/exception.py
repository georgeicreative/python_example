try:
    div = 7/0
    print(div)
except:
    print('Error Denomitor cannot be zero')
finally:
    print('caanot ')

try:
    list = [2,3,4]
    print(list[5])
except ZeroDivisionError:
    print('Denominator cannot be zero')
except IndexError:
    print('index out bound')


