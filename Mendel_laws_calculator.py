# -*- coding: utf-8 -*-
"""
@author: Yago

This calculator can calculate then results of the Punnet's charts
of the desired amount of traits.

It also has an option to calculate the result of the random
cross between the offsprings, as many times as wanted. This option
is enabled by indicating a number of generations greater than 1

"""

import random

def combinations(a):
    """ Extraction of the combinations of the traits  """
    if len(a)==1:
        return [a[0][0],a[0][1]]
    else:
        c=[]
        for i in combinations(a[1:]):
            c.append(a[0][0]+i)
            c.append(a[0][1]+i)
        return c
    
def order(info):
    """
    Orders the strings of a dictionary alphabetically, having 
    the uppercase priority. It also adds the value
    to the key: if after sorting the items, two or more keys are equal,
    the values of the keys would be summed up.
    order({('AbaB' :1, 'aABb :3'}) will return
    {'AaBa' : 4}
    """
    c={}
    for i in info:
        l=''.join(sorted(i, key=lambda v: (v.upper(), v[0].islower())))
        if l in c:
            c[l] = info[i] + c[l]
        else:
            c[l]=info[i]

    return c

def tabulate(info):
    """ Generates a table with the dictionnary info """
    a=list(info.values())
    b=list(info.keys())
    j=0
    for i in a:
        print(b[j],'--------->',i,'%')
        j+=1
        
def part(a):
    """
    Converts a list of one item to a list of multiple items
    part(['AaBb']) returns ['Aa','Bb'] 
    """
    j,k,c = 0,'',[]
    for i in a:
        if j%2 == 0 and j != 0:
            c.append(k)
            k=''
        k = k + i
        j+=1
    c.append(k)    
    return c

def analysisph(info,n):
    """ Analysis of the phenotypes """
    h={}
    for i in info:
        j,p,k='',1,0
        for z in i:
            if len(j) != 0:
                if p%2 != 0:
                    if z.capitalize() == z:
                        j = j+z
                else:
                    if j[len(j)-1] != z.capitalize() and j[len(j)-1] != z:
                        j = j +z
                    
            else:
                if z.capitalize() == z:
                    j = j +z
                    k=1
                elif k==0:
                    j=j+z
            p+=1
        if j != '':
            if j in h: h[j] = h[j] + info[i]
            else: h[j] = info[i]
                
    if h != {}:
        for i in h:
            h[i]= h[i]/n *100
            
    h = dict(sorted(h.items(), key=lambda item: item[1],reverse=True))
    print('--------Phenotype---------')
    tabulate(h)

            

def analysisg(info,n):
    """ Analysis of the genotypes """
    h={}
    for i in info:
        if i in h: h[i] = h[i] + info(i)
        else: h[i] = info[i]
        
    if h != {}:
        for i in h:
            h[i]= h[i]/n *100
            
    h = dict(sorted(h.items(), key=lambda item: item[1],reverse=True))
    print('--------Genotype---------')
    tabulate(h)



def calculation(a,b,show=True):
    """ Generates a dictionary with all possibles combinations """
    if len(a) != len(b):
        raise ValueError('Both parents should have the same amount of traits')
    
    g1=combinations(a)
    g2=combinations(b)
    c={}
    
    for i in g1:
        for z in g2:
            if i+z in c:
                c[i+z]=c[i+z] +1
            else:
                c[i+z]=1
                
    c=order(c)
    if show:
        n=0
        for i in c:
           n += c[i] 
        print('-------------------------')
        print(''.join(a),'x',''.join(b))        
        analysisph(c,n)
        analysisg(c,n)
        
    return c      

def calculateGen(a,b,n=1,show=True):
    """
    Generates a dictionary with all possibles combinations
    for n generations
    """
    if n == 1:
        c = calculation(a, b)
    else:
        j = calculation(a,b,show=False)
        i=1
        while i < n:
            c={}
            for m in j:
                c[m] = j[m]
            j={}
            for l in c:
                p = random.choice(list(c.keys()))
                k = calculation(part(l),part(p),show=False)
                for h in k:
                    if h in j:
                        j[h] = j[h] + 1
                    else:
                        j[h] = k[h]
            i+=1   
        c=order(j)
        if show:

            print('-------------------------')
            print(''.join(a),'x',''.join(b),'(',n,'generations )') 
            n=0
            for i in c:
               n += c[i] 
            analysisph(c,n)
            analysisg(c,n)
    return c   

def run():        
          
  print('-------------------------')
  print('Please enter the traits leaving spaces between the different traits:\nAa Bb Cc')
  print('and not AaBbCc or Aa Bb Cc (with extra space in the back)')

  a=input('First parent: ').split(' ')
  b=input('Second Parent: ').split(' ')
  c=int(input('Number of generations: '))
  calculateGen(a,b,n=c)



run()
        
