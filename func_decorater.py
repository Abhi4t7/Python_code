def add(a,b):
    print(a+b)

def add_mod(func):
    def innerrr(a,b):
            print("Smat addition")
            a=b+1
            return func(a,b)
    return innerrr

stadd=add_mod(add)
x, y = [int(x) for x in input("Enter two value: ").split()] 
stadd(x,y)
print("ENT\n")
add(x,y)
