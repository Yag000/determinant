# -*- coding: utf-8 -*-
"""
@author: Yago Iglesias

Determinant calculator

This calculator can operate
real numbers and polynomials, with only one
variable (x), and matrices of order n.

The way to input a determinant is thought this
syntax:
    det(Matrix)
    
The input matrix needs to be in either of this formats:
    
    --------
    1  2  3
    4  5  6
    7  8  9
    --------
    
    - a string: 
        A = "1,2,3,4,5,6,7,8,9"
        
    - or a list of lists: 
        A = [[1,2,3],[4,5,6],[7,8,9]]
        
In order to input a variable:
    
    - If it is a monomial:
        
        A = 'x,2,3,4x^7,5,6,7,8,9'
        
        To input a monomial as a list of
        lists, an instance of the class polynomial
        must be created:
            
        A = [[polynomial([1,1]),2,3],[polynomial([4,7]),5,6],[7,8,9]]
        
    - If it is a polynomial: 
        -----------------------
        x-1      2         3
        x^4 +1   5         6
        7x       8         9x^5
        -----------------------
        
        A = '[1,1,-1,0],2,3,[1,4,1,0],5,6,7x,8,9x^5'
        
        In order to input a polynomial as a list
        of lists, we must use the same syntax as in the
        monomial case, creating an instance of the polynomial
        class for every polinomial:
            
        A = [[polynomial([1,1,-1,0]),2,3],
             [polynomial([1,4,1,0]),5,6],
             [polynomial([7,1]),8,polynomial([9,5])]]
"""


from math import sqrt
import random

class NonSquareException(Exception):
    """ Matrix must be square"""
    
    def __str__(self):
        return 'Non square matrix'
    
class polynomial():
    
    """   
    Representation of a polynomial.

    To create an instance of this class,
    the following syntax must be used:
        polynomial(list)
    
    The list must contain integers or floats. 
    
    In orther to write this expression (34x^2 -4x + 1) as an instance
    of this class, the following syntax must be used:
        polynomial([34,2,-4,1,1,0])
     
    """
    def __str__(self):
        self.sort()
        j=0
        c=''
        
        for i in self.num:
            if j != 0 and i >= 0:
                c = c+ ' + '
            elif i < 0:
                c = c +' '
                
            if self.x[j] != 1 and self.x[j] != 0:
                if i == 1:
                    c = c + 'x^' + str(self.x[j])
                else:
                    c = c + str(i) + 'x^' + str(self.x[j])
                
            elif self.x[j] == 1:
                if i == 1:
                    c = c + 'x'
                elif i == -1:
                    c = c +' - ' + 'x'
                else:
                    c = c + str(i) + 'x'
                
            elif self.x[j] == 0:
                c= c + str(i)

            j+=1
            
        return c
    
    def __init__(self,numx):
        
        self.num = []
        self.x= []
        j=0
        for i in numx:
            if j %2 == 0:
                
                self.num.append(i)
            else:
                self.x.append(i)
            j+=1
        
    def __add__(self, other):
        
        self.simplify()
        if isinstance(other, float) or isinstance(other, int):
            j,k=0,0
            for i in self.x:
                if i ==0:
                    self.num[j] = self.num[j] + other
                    k=1
                    break
                j+=1
            if k == 0:
                self.num.append(other)
                self.x.append(0)
            return self
        
        if isinstance(other, polynomial):
            
            self.simplify()
            other.simplify()
            h1,h2 = {},{}
            j=0      
            
            while j < len(self.x):
                h1[self.x[j]] = self.num[j]
                j +=1
                
            j=0
            while j < len(other.x):
                h2[other.x[j]] = other.num[j]
                j+=1
            
            c = polynomial([])
            k=list(h1.keys())
            
            for i in k:                
                if i in h2:
                    c.x.append(i)
                    c.num.append(h1[i]+ h2[i])
                    h2.pop(i)
                    h1.pop(i)
            if h1 != {}:
                for i in h1:
                    c.x.append(i)
                    c.num.append(h1[i])
                
            if h2 != {}:
                for i in h2:
                    c.x.append(i)
                    c.num.append(h2[i])
                    
            if c.num==[]:
                c.num=[0]
            if c.x==[]:
                c.x=[0]
            
            c.sort
            return c
                
                    
    def __sub__(self,other):
        
        self.simplify()
        
        if isinstance(other, float) or isinstance(other, int):
            j,k=0,0
            for i in self.x:
                if i ==0:
                    self.num[j] = self.num[j] - other
                    k=1
                    break
                j+=1
            if k == 0:
                self.num.append(other)
                self.x.append(0)
            return self
        
        if isinstance(other, polynomial):
            
            other.simplify()
            
            c = []
            j=0
            for i in other.num:
                c.append(-i)
                c.append(other.x[j])
                j+=1
            
            return self + other
        
    def __mul__(self,other):
        
        if isinstance(other, float) or isinstance(other, int):
            i = 0
            while i < len(self.num):
                self.num[i] = self.num[i]*other
                i +=1
            return self
        
        if isinstance(other, polynomial):
            i = 0
            c = polynomial([])
            while i < len(self.num):
                j=0
                while j < len(other.num):

                    c.num.append(self.num[i] * other.num[j])
                    c.x.append(self.x[i] + other.x[j])
                    j+=1
                    
                i+=1

            c.sort()
            if c.num == []:
                c.num =[0]
            if c.x == []:
                c.x=[0]
            return c
        

    def simplify(self):
        """
        Simplifies the polynimial
        """
        h={}
        j=0
        
        while j < len(self.x):
            if self.x[j] in h:   
                h[self.x[j]] = h[self.x[j]] + self.num[j]  
            else:
                if self.num[j] != 0:
                    h[self.x[j]] = self.num[j]
                    
            j+=1
            
        if h == {}:
            self.num=[0]
            self.x = [0]
        else:
            i =0
            self.x = []
            self.num=[]
            for i in h:
                if h[i] != 0:
                    self.x.append(i)
                    self.num.append(h[i])
                
            
    def sort(self):
        
        """ Sorts the polynomial from the biggest
        exponent to the smallest one """
        
        self.simplify()
        
        h = {}
        j=0      
        while j < len(self.x):
            h[self.x[j]] = self.num[j]
            j +=1
            
        hitems = h.items()
        hs = sorted(hitems,reverse = True)
        self.x =[]
        self.num = []
        
        j = 0
        for i in hs:
            self.x.append(i[0])
            self.num.append(i[1])

def extract(A):
    
    """ Extraction of a Matrix from an str input """
    
    number=['0','1','2','3','4','5','6','7','8','9','.','-']
    c=[]
    ci=[]
    especial =[]
    ct=''
    i,num,k,ex,w,h=0,0,0,'',0,0
    
    for x in A:
        if x == '[':
            w=1
        if x == ']':
            w=0
        if w == 0 and x ==',':
            num+=1
    num+=1
    w = 0
    
    if sqrt(num) == int(sqrt(num)):
        n = sqrt(num)                           

        for x in A:
            if x == '[':
                w=1
            if w == 0:
                if x in number:

                    if k ==0:
                        ct = ct + x
                    else:
                        ex = ex+ x
                if x == 'x':
                    k=1
                    ex='0'
                if x == ',':  
                    if ex == '':
                        ci.append(polynomial([float(ct),0]))
                    else:
                        if ct == '':
                            ct = 1
                        
                        if ex == '0':
                            ci.append(polynomial([float(ct),1]))
                        else:
                            if ct == '-':
                                ct = ct +'1'
                            ci.append(polynomial([float(ct),float(ex)]))
    
                        ex,k='',0
                    ct =''
                    i+=1
            if w == 1 and x !='[':
                if h == 1:
                    w=0
                    h=0
                elif x == ',':
                    especial.append(float(ct))
                    ct=''
                elif x ==']':
                    especial.append(float(ct))
                    ci.append(polynomial(especial))
                    especial = []
                    ct=''
                    i+=1
                    h=1
                else:
                    ct = ct + x
            if i == n:
                c.append(ci)
                ci=[]
                i=0                 
         
    else:
        return None

    if ct != '' or ex != '':
        
        if ex == '':
            ci.append(polynomial([float(ct),0]))
        else:
            if ex == '0':
                if ct == '':
                    ci.append(polynomial([1,1]))
                else:
                    ci.append(polynomial([float(ct),1]))  
            else:     
                if ct == '':
                    ci.append(polynomial([1,float(ex)]))
                else:
                    ci.append(polynomial([float(ct),float(ex)]))               
        c.append(ci)
    return c
                
def multdet (A,x):
    """
    Determinant multiplied by a number (polynomial or not)
    
    Parameters:
        A : Matrix as a string
        x : Number
    """
    
    c,ci=[],[]
    i,z=0,0

    while i < len(A):
        while z < len(A):
            if i == 0:
                ci.append(x*A[i][z])

            else:
                ci.append(A[i][z])
            z+=1
        c.append(ci)
        ci=[]
        z=0
        i+=1
    return c    

def adjugate(A,x,y):
    """
    Calculus of Adjugate Matrix
    
    Parameters:
        A : Matrix(as a list of lists)
        x : Vertical position(starting from 0)
        y : Horizaontal position(starting from 0)
        
        For example, the adjugate matrix of 
        -----
        1 2 3 
        4 5 6
        7 8 9
        -----
        
        given the parameters x = 0 and y = 1
        is:
            
        ------
        -8 -12
         7  9
        ------
        
    Returns:
        The adjugate matrix as a list of lists:
        [[-8,-12],[7,9]]
        
    """
    
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
            a = polynomial([])
            j=0
            for i in A[x][y].x:              
                a.x.append(i)
                a.num.append(-A[x][y].num[j])
                j+=1
            c = multdet(c,a)
        else:

            c = multdet(c,A[x][y])
    return c

def det(A):
    """Calculus of the determinant of a Matrix,
    through Laplace expansion
    
    Parameter:
    A : Matrix, either as a string or as a list of lists (see some
    examples at the beginning of the code)    
    
    """
    global p
    if type(A) is str:
        A=extract(A)
        
    if isinstance(A,list):
        z=0
        c,ci=[],[]
        for i in A:
            for j in i:
                if isinstance(j,polynomial):
                    ci.append(j)
                else:
                    ci.append(polynomial([j,0]))
                z+=1
            c.append(ci)
            ci=[]
        
        if sqrt(z) == int(sqrt(z)):
            A=c
        else:
            raise NonSquareException()
    i =0
    
    while i < len(A):
        j=0
        while j < len(A[i]):
            j+=1
        i+=1
        
    if A == None:
        raise NonSquareException()
        
    a = polynomial([0,0])
    n = len(A)

    if n > 1:
        for i in range(n):
            at = det(adjugate(A,0,i))
            a = a + at


    if n ==1:
        at= A[0][0]
        a = a + at
            
    return a



def randomMat(n):
    """ 
    Creates a random matrix (with natural numbers
    between 0 and 1000) of n order (str output)

    """
    
    i,c=1,''
    n=n*n
    
    while i <= n:
        c = c + str(random.randrange(0,1000))
        z= i +1
        if z <= n:
            c=c+','
        i+=1
       
    return c

A = '4x,4x^2,-x^3,x^4,[534,5,1,0],-x^6,x*7,[43,8,2,0,65,2],-3x^9'
print(det(A))

