def bigger_Is_greater(w):
#Converting string to a list 
    l = list(w)
    #Find the largest index i such that l[i] < l[i+1]
    i = len(l) - 2
    while i>=0 and l[i] >= l[i+1]:
        i -=1

    if i == -1:
        return 'no answer'
    
    #find the largest index j such that l[i] < l[j] 
    j = len(l) -1
    while l[j] <= l[i]:
        j -= 1

#Next step is swap l[i] and l[j]
    l[i] ,l[j] = l[j],l[i]

    l[i+1:] = reversed(l[i+1:])

#And converting back to a string
    return ''.join(l)

print(bigger_Is_greater('abcdefghij'))
    




