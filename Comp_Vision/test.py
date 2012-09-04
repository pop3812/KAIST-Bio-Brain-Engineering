print 'Hello, world!'
print 'Hello, Byung Shin!'

string = ''

for i in range(10):
    string += str(i/5) + ' : '

string = string.strip(': ')
print string