f=open("myfile",'r')
#print(f.read())  # to read entire file
print(f.readline())     # to read first line
print(f.readline(4))  # to print first 4 char

ff=open("writefile",'w') #to write data in file
ff.write("Hello world")
ff=open("writefile",'a')  # to append data in file

for data in f:
    ff.write(data)
