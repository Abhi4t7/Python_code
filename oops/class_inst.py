class studen:
    cmane="AITRC"
    def __init__(self,x,y):
        self.name=x
        self.rollno=y

    def printtt(self):
        print(self.name)
        print(self.rollno)

    @classmethod
    def getname(cls):
        print(cls.cmane)

    @staticmethod
    def add(x,y):
        print(x+y)

s=studen("AK",33)
s.printtt()
s.getname()
s.add(2,2)
