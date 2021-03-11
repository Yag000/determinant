from math import sqrt
from tabulate import tabulate
import random


def extraer(A):
    
    number=['0','1','2','3','4','5','6','7','8','9','.','-']
    c=[]
    ci=[]
    ct=''
    i,num=0,0
    for x in A:
        if x ==',':
            num+=1
    num+=1
    
    if sqrt(num) == int(sqrt(num)):
        n = sqrt(num)                           

        for x in A:
            if x in number:
                ct = ct + x
            if x == ',':
                ci.append(float(ct))
                ct =''
                i+=1
            if i == n:
                c.append(ci)
                ci=[]
                i=0                 
            
    else:
        return None

    if ct != '':               
        ci.append(float(ct))
        c.append(ci)
    return c
                
def multdet (A,x):
    c,ci=[],[]
    i,z=0,0
    while i < len(A):
        while z < len(A):
            if i == 0:
                ci.append((A[i][z])*x)
            else:
                ci.append(A[i][z])
            z+=1
        c.append(ci)
        ci=[]
        z=0
        i+=1
    return c    



def adjunto(A,x,y):
    n=len(A)
    c,ci=[],[]
    i,z=0,0
    while i < n:
        if i != x:
            while z < n:
                if z != y:
                    ci.append(A[i][z])
                z+=1
        if ci != []:
            c.append(ci)
        
        ci=[]
        z=0
        i+=1
        
    if c != []:
        if (x+y)%2 != 0:
            c = multdet(c,-(A[x][y]))
        else:
            c = multdet(c,A[x][y])
        return c
    else:
        return c

def det(A):
    if type(A) is str:
        A=extraer(A)
    if A == None:
        print('Matriz no cuadrada')
        return
    a,b = 0,0
    n = len(A)

    if n > 1:
        for i in range(n):
            at = det(adjunto(A,0,i))
            a=a+at
    if n ==1:
        bt= A[0][0]
        b = b+bt

    return a+b


def randomMat(n):
    i,c=1,''
    n=n*n
    while i <= n:
        c = c + str(random.randrange(0,1000))
        z= i +1
        if z <= n:
            c=c+','
        i+=1
    
    
    return c
        

A = '1,0,786,3,-1,4,-1,4x,-3' 
B = randomMat(7)


print('El determinante de la matriz\n',tabulate(extraer(A)),' \nes %f' %(det(A)))

#for numpy testing
import numpy as np
print ('La matriz con numpy es %f' %(np.linalg.det(extraer(A)))) 

# print('Error: ', (det(B) - np.linalg.det(extraer(B)))/((det(B)+np.linalg.det(extraer(B)))/2)*100)


