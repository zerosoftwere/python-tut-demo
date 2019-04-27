# Wrong way of doing it

users = [{'username': 'henry', 'password': 'secret'}, {'username': 'xero', 'password': 'secure'}]

username = input('Enter username: ')
password = input('Enter password: ')

for user in users:
    if user['username'] == username and user['password'] == password:
        print('Login Successful')
    else:
        print('Authentication failed')