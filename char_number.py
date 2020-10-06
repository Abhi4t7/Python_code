str=input("Enter words")
p={}
for x in str:
    p[x]=p.get(x,0)+1
for k,v in p.items():
    print("{} occurs {} times".format(k,v))
