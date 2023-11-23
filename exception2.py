class InvalidAgeException(Exception):
    'raise when exception occuer divide by zero'
    pass
number = 18
x = 0
while x < 3:
    try:
        input_num = int(input('enter number'))
        if input_num < number:
            raise InvalidAgeException
        else:
            print('eligible for vote')
    except InvalidAgeException:
        print("Exception Handling : Inavalid Age")
    x +=1