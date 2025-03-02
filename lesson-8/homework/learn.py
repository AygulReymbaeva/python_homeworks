def say_hello():
    print("Hello World")

say_hello()

def greet(name):
    print("Hello", name)

greet("Aygul")

def add(a,b):
    return a+b
result=add(5,3)
print(result)

def square(x):
    return x*x
result= map(square,[1,2,3,4])
print(list(result))

name = input("What's your name?")
print("Hello,", name)