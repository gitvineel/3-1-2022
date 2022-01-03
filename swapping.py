P = int(input("Please enter value for P: "))
Q = int(input("Please enter value for Q: "))

P = P ^ Q
Q = P ^ Q
P = P ^ Q
print("After Swapping P: ", P)
print("After Swapping Q: ", Q)



