class computer:
    def __init__(self,y,z):
        self.y=y
        self.z=z

    def con(self):
        print(self.y,self.z)

comp1=computer(8,9)
comp2=computer("Abhj","kore")
comp1.con()
comp2.con()

