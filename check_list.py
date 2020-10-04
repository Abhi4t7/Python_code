def checkSubset(list1, list2): 
    #l1, l2 = list1[2], list2[2] 
    existt = True
    for i in list2: 
        if i not in list1: 
            existt = False
    return existt 
      
# Driver Code 
list1 = [[2, 3, 1], [4, 5], [6, 8]] 
list2 = [[4, 8], [6, 8],[4,5]] 
print(checkSubset(list1, list2))
