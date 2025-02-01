# A simple function with o arguments and no return value 
def greet():
  print('Hello, world')
greet()

# A function that takes paramters

def greet1(name):
  print(f'Hello, {name}!')
greet1('Akash')

# Funtion with return value

def add(a,b):
  return a+b
print(add(3,4))


# Funtion with default value
def greet2(name='World'):
  print(f'Hello, {name}!')
greet2()
greet2('kavitha')

# funcion with variable - length argument
def add(*args):
  return sum(args)
print(add(3,5,6,7))

# function wt keyword argument
def greet4(**kwargs):
  if 'name' in kwargs:
    print(f'Hello, {kwargs['name']}')
  else:
    print('Hello world')
greet4(name='amitha')
greet4()