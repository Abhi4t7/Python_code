
def mul(a,b):
    return a*b

def add(a,b):
    c=a+b
    print(c)
    d=mul(a,b)
    print(d)

def printf(x):
        for y in x:
         print(y)

a,b = [int(x) for x in input("Enter two value: ").split()]
add(a,b)
print("List is\n")
x = list(map(int, input("Enter a multiple value: ").split()))
#y = tuple(map(int, input("Enter a multiple value: ").split()))
printf(x)
