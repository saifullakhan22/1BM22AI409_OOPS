def largest(l):
    largest = 0 
    for i in l:
        if i>largest:
            largest = i
    print(largest)

l =[2,3,4,1,5,9,45,5,8]        

largest(l)
