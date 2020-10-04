s=[1,2,3,[1,2],[3,4],[8,6]]
p=[10,[13,4],11]
m=0
for x in s:
    for y in p:
        if x==y:
            print("Same")
            m=1
            break
if m==0:
    print("Not same")


