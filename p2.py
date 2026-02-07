n = int(input())
counter3 = 0
counter2 = 0
counter = 0
i = 1
while i < n:
    z = i
    while z != 1:
        if z%2 == 0:
            z = z//2
            counter +=1
        else:
            z = (3*z) + 1
            counter +=1
    if counter > counter2:
        counter2 = counter
        counter3 = i
    i +=1
    counter = 0
print("for all inputs less than " , n) 
print("the longest chain starts with ", counter3)
print("and has " , counter2 + 1 , " links")


