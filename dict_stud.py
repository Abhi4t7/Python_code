rev={}
n=input("Enter number of student: ")
n=int(n)
i=1
while i<=n:
    name=input("Enter name")
    mark=input("Enter mark")
    rev[name]=mark
    i+=1

for i in rev:
    print(i , rev[i])
