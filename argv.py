#import sys 
from sys import argv 
# total arguments 
n = len(argv) 
print("Total arguments passed:", n) 
  
# Arguments passed 
print("\nName of Python script:",argv[0]) 
  
print("\nArguments passed:", end = " ") 
for i in range(1, n): 
    print(argv[i], end = " ") 
      
# Addition of numbers 
Sum = 0
for i in range(1, n): 
    Sum += int(argv[i]) 
      
print("\n\nResult:", Sum) 
