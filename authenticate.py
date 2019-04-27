users = [{'username': 'xero', 'password': 'secret'}, {'username': 'henry', 'password': 'secure'}]

username = input('Enter username: ')
password = input('Enter password: ')

if username == users[0]['username'] and password == users[0]['password']:
    print('Login successful')
elif username == users[1]['username'] and password == users[1]['password']:
    print('Login successful')
else:
    print('Authentication failed')