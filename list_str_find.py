str="ssssstttrrrr"
m=0
for i in str:
    if i=='z':
        print("Present")
        m=1
        break
if m!=1:
    print("Not present")
