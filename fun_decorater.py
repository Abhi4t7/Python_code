def deco(func):
    def added(name):
        if name=="Abhi":
            print("Hello Abhijit")
        else:
            func(name)
    return added

@deco
def wish(name):
    print("Hello",name)

wish("jk")
wish("Abhi")

