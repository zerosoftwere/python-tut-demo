# Number data types
x = 2.4 # floating point number
print('==== Number datatype ====')
print('type of x:', type(x))
print('value of x:', x)
print('')

a = 2
print('type of a:', type(a))
print('value of a:', a)
print('')

# String data type
print('==== String datatype ====')
s1 = 'The quick brown fox jumps over the lazy dog'
print('type of s1:', type(s1))
print('value of s1:', s1)
s2 = 'and it is awesome'
print('value of s2:', s2)
print('== String operations ==')
print('concatenation#1 (s1 + s2):', s1 + s2)
print('concatenation#2 (s1 + s2):', s1 + ' ' + s2)
print('length of s1:', len(s1))
print('index of `o` in s1:', s1.index('o'))
print('rindex of `o` in s1:', s1.rindex('o'))
print('')

# List data type
print('==== List datatype ====')
ls = [1, 2, 'one', 'Hello']
print('type of ls:', type(ls))
print('value of ls:', ls)
print('value of ls at index 2:', ls[2])
print('the index of `Hello` in ls:', ls.index('Hello'))

# List operations
print('== List operations ==')
ls[3] = 'henry'
print('the new value of ls:', ls)
ls.append('xero')
print('item added to ls:', ls)
ls.insert(0, 4)
print('insert item at index 0:', ls)
ls.insert(3, 'two')
print('insert item before index 3:', ls)
print('')

# Set datatype
print('==== Set datatype ====')
s1 = {'blue', 'red', 'green', 'red'}
print('type of s1:', type(s1))
print('value of s1:', s1)
s2 = {'blue', 'purple', 'yellow', 'green'}
print('value of s2:', s2)

# Set operations
print('== Set operations ==')
print('s1 union s2', s1.union(s2))
print('s1 intersection s2', s1.intersection(s2))
print('s1 difference s2', s1.difference(s2))
print('s2 difference s1', s2.difference(s1))