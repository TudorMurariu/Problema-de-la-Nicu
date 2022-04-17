# facem un backtracking 
#                b1
# a1:    x   x   x
#        x       x
#        x       x
# a2:    x   x   x
#        b2

from operator import truediv

def print_all(a1, a2, b1 ,b2):
        print()

        for x in a1:
            print(x,end="  ")
        print()

        print(str(b2[2]) + "     " + str(b1[1]))
        print(str(b2[1]) + "     " +str(b1[2]))
        
        for x in a2:
            print(x,end="  ")
        
        print()
        print()

def verify_x(n, x, a1, a2, b1, b2):
    return (not x in a1) and (not x in b1) and (not x in a2) and (not x in b2)

def back(n, a1, a2, b1, b2):

    # with open('test.txt', 'a') as f:
    #     f.write(str(a1))
    #     f.write(str(b1))
    #     f.write(str(a2))
    #     f.write(str(b2))
    #     f.write("\n")
    #print(a1,a2,b1,b2)

    if sum(b2) == n and len(b2) == 4:
        print(n)
        print_all(a1, a2, b1 ,b2)
    
    else:

        if sum(a1) < n and len(a1) < 3:
            for i in range(1,11,1):
                if verify_x(n, i, a1, a2, b1, b2):
                    a1.append(i)
                    if len(a1) == 3:
                        b1.append(i)
                    back(n, a1, a2, b1, b2)
                    if len(a1) == 3:
                        b1.pop()
                    a1.pop()
            
        elif sum(a1) == n and len(a1) == 3 and len(b1) < 4:
            for i in range(1,11,1):
                if verify_x(n, i, a1, a2, b1, b2):
                    b1.append(i)
                    if len(b1) == 4:
                        a2.append(i)
                    back(n, a1, a2, b1, b2)
                    if len(b1) == 4:
                        a2.pop()
                    b1.pop()

        elif sum(a1) == n and sum(b1) == n and len(a1) == 3 and len(b1) == 4 and len(a2) < 3:
            for i in range(1,11,1):
                if verify_x(n, i, a1, a2, b1, b2):
                    a2.append(i)
                    if len(a2) == 3:
                        b2.append(i)
                    back(n, a1, a2, b1, b2)
                    if len(a2) == 3:
                        b2.pop()
                    a2.pop()

        elif sum(a1) == n and sum(b1) == n and sum(a2) == n and len(a1) == 3 and len(b1) == 4 and len(a2) == 3 and len(b2) < 4:
            if len(b2) == 3:
                b2.append(a1[0])
                back(n, a1, a2, b1, b2)
                b2.pop()
            else:
                for i in range(1,11,1):
                    if verify_x(n, i, a1, a2, b1, b2):
                        b2.append(i)
                        back(n, a1, a2, b1, b2)
                        b2.pop()
    

def cauta(n):
    a1 = []
    a2 = []
    b1 = []
    b2 = []
    back(n,a1,a2,b1,b2)


if __name__ == '__main__':
    print(" : ")
    cauta(18)
    # cauta(14)
    # cauta(15)
    # cauta(16)
    # cauta(17)
    # cauta(19)
    # cauta(20)