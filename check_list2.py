 
def checkSubset(list1, list2): 
    temp1 = [] 
    temp2 = [] 
    for i in list1: 
        temp1.append(tuple(i)) 
        print(tuple(i)) 
    for i in list2: 
        temp2.append(tuple(i)) 
    return set(list1) < set(list2) 
      
# Driver Code 
list1 = [[2, 3, 1], [4, 6], [6, 8]] 
list2 = [[4, 5], [1, 8]] 
print(checkSubset(list1, list2))
