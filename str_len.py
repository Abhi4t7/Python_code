str=input("Enter string: ")
print(str)
count=0
k=0
for i in str:
    if i=='b':
        print("b is present")
        k=1
        break
if k!=1:
    print("b is not present")
    count+=1

print(count)
