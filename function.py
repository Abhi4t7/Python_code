
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

#a,b = [int(x) for x in input("Enter two value: ").split()]
#add(a,b)
x = list(map(int, input("Enter a multiple value for list: ").split()))
y = tuple(map(int, input("Enter a multiple value for tuple: ").split()))
print("List is")
printf(x)
print("Tuple is")
print(y)
print("END\n")
print(x,y)
x[0]=100
#y[0]=100
print(x,y)

