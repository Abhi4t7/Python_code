class student:
        '''Hello................'''
        def __init__(self,name,rollno):
            self.name=name
            self.rollno=rollno
        def pri(self):
            print("my name is:",self.name)

c1=student(" ", 3)
c1.name="AK"
c1.rollno=45
c1.pri()
print(c1.rollno)
    
