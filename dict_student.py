n=int(input("Enter number of student"))
d={}
for i in range(n):
    name=input("ENter name of student")
    mark=input("Enter marks of student")
    d[name]=mark
print(d)    

#while True:
name =input("Enter student name to get mark")
mark=d.get(name,-1)
if mark==-1:
    print("Student not found")
else:
    print("marks of {} : {}".format(name,mark))

