import utility

class Node:
    def __init__(self,data):
        self.l_child = None
        self.r_child = None
        self.data = data
    

def tree(key,r,i,j):
    k = r[i][j]
    if(k==0):
        return
    else:
        p=Node(key[k])
        p.l_child = tree(key,r,i,k-1)
        p.r_child = tree(key,r,k+1,j)
        return p

key = ["","A","B","C","D","E"] # Node name
p = [0,3/16,4/16,2/16,6/16,1/16] #검색 요청 빈도
n = len(p)-1

a = [[0 for j in range(0,n+2)] for i in range(0,n+2)]
r = [[0 for j in range(0,n+2)] for i in range(0,n+2)]

for i in range(1,n+1):
    a[i][i-1] = 0
    a[i][i] = p[i]
    r[i][i] = i
    r[i][i-1] = 0
a[n+1][n] = 0
r[n+1][n] = 0

def printMatirxF(d):
    n = len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print(f'{d[i][j]:5.2f}', end = " ")
        print()

#구현
for diagonal in range(1,n):
    for ii in range(1,n-diagonal+1):
        j = ii + diagonal
        sum = 0
        min_index = -1
        min = 1583188
        for x in range(ii, j+1):
            sum += a[x][x]
        for k in range(ii,j+1):
            temp = a[ii][k-1] + a[k+1][j]
            if(min > temp):
                min  = temp
                min_index = k
        a[ii][j] = min + sum
        r[ii][j] = k

utility.printMatirxF(a)
print()
utility.printMatrix(r)

root = tree(key,r,1,n)
utility.print_inOrder(root)
print()
utility.print_preOrder(root)
