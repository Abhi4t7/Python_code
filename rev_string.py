str=input("Enter string: ")
rev=""
j=0
for i in str:
    j+=1
print("str len= ",j)
j-=1
while(j>=0):
    rev=rev+str[j]
    j-=1
print(rev)
