'''x=100
y=200
print(x+y)

import keyword
print(keyword.kwlist)
print(keyword.softkwlist) # ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
['_', 'case', 'match']

a='vinay'
b='rahul'
print((a),(b))   # vinay rahul
print(b) # rahul

p='welcome to python',
print(p) # 'welcome to python'

print(a,b,p) # vinay rahul ('welcome to python',)
a=b=c=10.5
print(a,b,c) # 10.5 10.5 10.5
x=50
y=100
(y,x==x,y)
print(x,y)'''

x=100 # int
y=10.5 # float 
a='qac' # str 
b=True # boolean words or True or False ( to know the type of variables)
print(type(x))
print(type(y))
print(type(a))
print(type(b))

'''print(10+10) # 20
print(10+10.5) # 20.5
print(10.5+10.5) # 21.0
print('welcome'+'qac') # welcomeqac
print(True+True) # 2 True value by defult 1 & False value is 0
print(False+10) # 10
print(10+'welcome')''' # TypeError: unsupported operand type(s) for +: 'int' and 'str'

x=10
y=20
print("before swapping values are:",x,y)
x,y=y,x
print("after swapping values are:",x,y)


