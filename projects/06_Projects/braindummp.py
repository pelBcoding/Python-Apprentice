

def add(a,b):
    print( a++b )

def multiply(a,b):
    print( a*b )    

def divide(a,b):
    print( a/b )

def subtract(a,b):
    print( a--b )


def what_operation():
    if input("what operation u wan twin: add, multiply, divide, subtract  ") == add:
            print(add(int(input("num1   ")), int(input("num2   "))))
    elif input("what operation u wan twin: add, multiply, divide, subtract  ") == multiply:
            print(multiply(int(input("num1   ")), int(input("num2   "))))
    elif input("what operation u wan twin: add, multiply, divide, subtract  ") == divide:
            print(divide(int(input("num1   ")), int(input("num2   "))))
    elif input("what operation u wan twin: add, multiply, divide, subtract  ") == subtract:
            print(subtract(int(input("num1   ")), int(input("num2   "))))

print(what_operation())