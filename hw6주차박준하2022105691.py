def printMatrix(d):
    len_rows= len(d)
    len_cols= len(d[0])
    for i in range(0,len_rows):
        for j in range(0,len_cols):
            print(f'{d[i][j]:4d}',end=" ")
        print()
    
#print float matrix
def printMatirxF(d):
    n = len(d[0])
    for i in range(0,n):
        for j in range(0,n):
            print(f'{d[i][j]:5.2f}', end = " ")
        print()
        
def print_inOrder(root):
    if not root:
        return
    print_inOrder(root.l_child)
    print(root.data)
    print_inOrder(root.r_child)

def print_preOrder(root):
    if not root:
        return
    print(root.data)
    print_preOrder(root.l_child)
    print_preOrder(root.r_child)

###############
# Q1 - 최적이진검색트리

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

printMatirxF(a)
print()
printMatrix(r)

root = tree(key,r,1,n)
print_inOrder(root)
print()
print_preOrder(root)

#####################
#Q2 - DNA 서열 맞춤 알고리즘

import math

a=['A','C','G','A','C','T']
b=['C','C','G','A','T','C','T']

m = len(a)
n = len(b)
table = [[0 for j in range(0,n+1)] for i in range(0,m+1)]
minindex = [[(0,0) for j in range(0,n+1)] for i in range(0,m+1)]

for j in range(n-1,-1,-1):
    table[m][j] = table[m][j+1]+2

for i in range(m-1,-1,-1):
    table[i][n] = table[i+1][n]+2

#테이블 생성 구현
# penalty
# 불일치 - 1
# 틈 - 2
for ai in range(m-1,-1,-1):
    for bi in range(n-1,-1,-1):
        penalty = not (a[ai]==b[bi]) 
        minT = table[ai+1][bi+1] + penalty
        minI = (ai+1, bi+1)
        if (minT>table[ai][bi+1]+2):
            minT=table[ai][bi+1]+2
            minI = (ai, bi+1)
        if (minT>table[ai+1][bi]+2):
            minT=table[ai+1][bi]+2
            minI = (ai+1, bi)
        table[ai][bi] = minT
        minindex[ai][bi] = minI
printMatrix(table)
x=0
y=0

while(x<m and y<n):
    tx, ty = x,y
    print(minindex[x][y])
    (x,y) = minindex[x][y]
    if x==tx+1 and y == ty+1:
        print(a[tx]," ",b[ty])
    elif x==tx and y == ty+1:
        print(" - "," ", b[ty])
    else:
        print(a[x]," "," -")