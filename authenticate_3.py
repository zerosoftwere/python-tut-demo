users = [{'username': 'henry', 'password': 'secret'}, {'username': 'xero', 'password': 'secure'}]

username = input('Enter username: ')
password = input('Enter password: ')

authenticated = False
for user in users:
    if user['username'] == username and user['password'] == password:
        authenticated = True

if authenticated:
    print('Login successful')
else:
    print('Authentication failed')