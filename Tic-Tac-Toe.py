#tic-tac-toe
#from array import *

def print_array(a):
    n = 3
    i = 0
    j = 0
    for i in range(0, n):
        for j in range(0, n):
            print(a[i][j], end = " ")
        print("")

def check_array(a, x, y, c):
    k = 0
    m = x+y
    #print(m)
    if m%2 == 0 and x < y:
        if a[x][k]==a[x][k+1] and a[x][k+1]==a[x][k+2]:
            return True            
        elif a[k][y]==a[k+1][y] and a[k+1][y]==a[k+2][y]:
            return True           
        elif a[x][y]==a[x+1][y-1] and a[x+1][y-1]==a[x+2][y-2]:
            return True            
        # elif a[x][y]==a[x+1][y-1] and a[x+1][y-1]==a[x-1][y+1]:
        #     return True
        else:
            return False
        
    elif m%2 == 0 and x > y:
        if a[x][k]==a[x][k+1] and a[x][k+1]==a[x][k+2]:
            print(c, "has won")
            return True
        elif a[k][y]==a[k+1][y] and a[k+1][y]==a[k+2][y]:
            print(c, "has won")
            return True      
        # elif a[k][k]==a[k+1][k+1] and a[k+1][k+1]==a[k+2][k+2]:
        #     return True       
        elif a[x][y]==a[x-1][y+1] and a[x-1][y+1]==a[x-2][y+2]:
            print(c, "has won")
            return True           
        else:
            return False
    elif m%2 == 0 and x == y:
        if m == 2:
            if a[x][y-1]==a[x][y] and a[x][y]==a[x][y+1]:
                print(c, "has won")
                return True            
            elif a[x][y]==a[x-1][y] and a[x-1][y]==a[x+1][y]:
                print(c, "has won")
                return True            
            elif a[x][y]==a[x+1][y+1] and a[x+1][y+1]==a[x-1][y-1]:
                print(c, "has won")
                return True 
            else:
                return False          
        elif m == 4:
            if a[x][y]==a[x-1][y-1] and a[x-1][y-1]==a[x-2][y-2]:
                print(c, "has won")
                return True
            elif a[x][k]==a[x][k+1] and a[x][k+1]==a[x][k+2]:
                print(c, "has won")
                return True
            elif a[k][y]==a[k+1][y] and a[k+1][y]==a[k+2][y]:
                print(c, "has won")
                return True            
            else:
                return False
        elif m == 0:
            if a[x][y]==a[x+1][y+1] and a[x+1][y+1]==a[x+2][y+2]:
                print(c, "has won")
                return True
            elif a[x][k]==a[x][k+1] and a[x][k+1]==a[x][k+2]:
                print(c, "has won")
                return True
            elif a[k][y]==a[k+1][y] and a[k+1][y]==a[k+2][y]:
                print(c, "has won")
                return True            
            else:
                return False
        else:
            return False
    else:
        if a[x][k]==a[x][k+1] and a[x][k+1]==a[x][k+2]:
            print(c, "has won")
            return True    
        elif a[k][y]==a[k+1][y] and a[k+1][y]==a[k+2][y]:
            print(c, "has won")
            return True
            
        else:
            return False    

n = 3
rows, cols = (n, n)
a = [['*' for i in range(cols)] for j in range(rows)]

print(a)
print_array(a)

counter = n*n
while(counter>0):
    print("choose location")
    x = int(input())
    y = int(input())
    r = False

    if a[x][y] == '*':
        if counter%2 == 0:
            a[x][y] = 'o'
            print_array(a)
            #print(counter)
            r = check_array(a, x, y, a[x][y])
        else:
            a[x][y] = 'x'
            print_array(a)
            #print(counter)
            r = check_array(a, x, y, a[x][y])
    else:
        print("loaction already played...try again")
        counter = counter+1
    counter = counter-1
    if r == True:
        break



#initial state
# n = 3
# a = [[0]*n]*n
# i = 0
# j = 0
# for i in range(0, n):
#     for j in range(0, n):
#         a[i][j] = (i, j)
#         print(a[i][j], end = " ")
#     return False
#print_array(a) #method call

# counter = 9
# while(counter>0):
#     print("choose location")
#     x = int(input())
#     y = int(input())

#     if counter%2 == 0:
#         a[x][y] = ("o", "o")
#     else:
#         a[x][y] = ("x", "x")
    
#     print(a)
#     print(counter)
#     counter = counter-1