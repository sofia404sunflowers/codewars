def create_phone_number(n):
    s = "("
    for d in range(3):
        #print(n[d])
        s = s+str(n[d])
    s+=") "
    for d in range(3,6):
        s = s+str(n[d])
    s+="-"
    for d in range(6,10):
        s = s+str(n[d])

    return s
t = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(create_phone_number(t))