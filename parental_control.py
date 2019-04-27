name = input('Enter name: ')
age = input('Enter age: ')
age = int(age)

if not age > 18:
    print('You are not allowed to view this channel')
else:
    print('Welcome')