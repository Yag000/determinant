from tkinter import *
from random import randrange

def movA(event):
    global h,q
    if q != 1:
        q=-1
    if h == 0:
        move()
    h=1
def movB(event):
    global h,q
    if q != -1:
        q=1
    if h == 0:
        move()
    h=1
def movD(event):
    global h,q
    if q!=2:
        q=-2
    if h == 0: 
        move()
    h=1
def movI(event):
    global h,q
    if q != -2:
        q=2
    if h == 0:
        move()
    h=1
    
def start(x,y):
    global man

    man[0]=can1.create_rectangle(x+3,y,x+8,y,fill='red',outline='red')
    man[1]=can1.create_rectangle(x+2,y+1,x+9,y+1,fill='red',outline='red')
    man[2]=can1.create_rectangle(x+1,y+2,x+10,y+2,fill='red',outline='red')
    man[3]=can1.create_rectangle(x,y+3,x+11,y+6,fill='red',outline='red')
    man[4]=can1.create_rectangle(x+1,y+7,x+10,y+7,fill='red',outline='red')
    man[5]=can1.create_rectangle(x+2,y+8,x+9,y+8,fill='red',outline='red')
    man[6]=can1.create_rectangle(x+3,y+9,x+8,y+9,fill='red',outline='red')
    man[7]=can1.create_rectangle(x+5,y,x+6,y-2,fill='brown',outline='brown')

def colorC():
    can1.configure(bg='white')
    if power ==1:
        root.after(10,colorCh)
    else:
        can1.configure(bg='light blue')
def colorCh():
    can1.configure(bg='light blue')
    if power == 1:
        root.after(10,colorC)
    else:
        can1.configure(bg='light blue')
def rainbow():
    can1.coords(rai[0],raix+3,raiy,raix+8,raiy)
    can1.coords(rai[1],raix+2,raiy+1,raix+9,raiy+1)
    can1.coords(rai[2],raix+1,raiy+2,raix+10,raiy+2)
    can1.coords(rai[3],raix,raiy+3,raix+11,raiy+4)
    can1.coords(rai[4],raix,raiy+4,raix+11,raiy+5)
    can1.coords(rai[5],raix,raiy+5,raix+11,raiy+6)
    can1.coords(rai[6],raix,raiy+6,raix+11,raiy+7)
    can1.coords(rai[7],raix+1,raiy+7,raix+10,raiy+7)
    can1.coords(rai[8],raix+2,raiy+8,raix+9,raiy+8)
    can1.coords(rai[9],raix+3,raiy+9,raix+8,raiy+9)
    can1.coords(rai[10],raix+5,raiy,raix+6,raiy-4)
def rainbowI():
    global raix,raiy
    while 1:
        i=0
        raix,raiy=randrange(0,600),randrange(0,600)    
        if raix in range(431,465) and raiy in range(63,100):
            i=1 
        if raix  in range(451,485) and raiy in range(363,400):
            i=1         
        if raix in range(131,165) and raiy in range(463,500):
            i=1
        if raix in range(x1,x1+10) and raiy in range(y1,y1+10):
            i=1
        if i == 0:
            if raix%10 == 0 and raiy%10 == 0:
                break
    rai[0]=can1.create_rectangle(raix+3,raiy,raix+8,raiy,fill='pink',outline='pink')
    rai[1]=can1.create_rectangle(raix+2,raiy+1,raix+9,raiy+1,fill='violet',outline='violet')
    rai[2]=can1.create_rectangle(raix+1,raiy+2,raix+10,raiy+2,fill='blue',outline='blue')
    rai[3]=can1.create_rectangle(raix,raiy+3,raix+11,raiy+4,fill='green',outline='green')
    rai[4]=can1.create_rectangle(raix,raiy+4,raix+11,raiy+5,fill='yellow',outline='yellow')
    rai[5]=can1.create_rectangle(raix,raiy+5,raix+11,raiy+6,fill='orange',outline='orange')
    rai[6]=can1.create_rectangle(raix,raiy+6,raix+11,raiy+7,fill='red',outline='red')
    rai[7]=can1.create_rectangle(raix+1,raiy+7,raix+10,raiy+7,fill='pink',outline='pink')
    rai[8]=can1.create_rectangle(raix+2,raiy+8,raix+9,raiy+8,fill='violet',outline='violet')
    rai[9]=can1.create_rectangle(raix+3,raiy+9,raix+8,raiy+9,fill='blue',outline='blue')
    rai[10]=can1.create_rectangle(raix+5,raiy,raix+6,raiy-4,fill='brown',outline='brown')
    
def Power():
    global power
    power =0
    root.after(randrange(10000,30000),rainbow)
    
def rainbowC():
    global raiy,raix,power,rai,ca
    while 1:
        i=0
        raix,raiy=randrange(0,600),randrange(0,600)    
        if raix in range(431,465) and raiy in range(63,100):
            i=1 
        if raix  in range(451,485) and raiy in range(363,400):
            i=1         
        if raix in range(131,165) and raiy in range(463,500):
            i=1
        if raix in range(x1,x1+10) and raiy in range(y1,y1+10):
            i=1
        if i == 0:
            if raix%10 == 0 and raiy%10 == 0:
                break
    i=0
    while i < len(rai):
        can1.coords(rai[i],-100,-100,-110,-110)
        i+=1
    power=1
    colorC()
    root.after(8000,Power) 

def apple(x,y):
    global man
    can1.coords(man[0],x+3,y,x+8,y)
    can1.coords(man[1],x+2,y+1,x+9,y+1)
    can1.coords(man[2],x+1,y+2,x+10,y+2)
    can1.coords(man[3],x,y+3,x+11,y+6)
    can1.coords(man[4],x+1,y+7,x+10,y+7)
    can1.coords(man[5],x+2,y+8,x+9,y+8)
    can1.coords(man[6],x+3,y+9,x+8,y+9)
    can1.coords(man[7],x+5,y,x+6,y-2)
 

def arbre(x,y):
    can1.create_rectangle(x,y,x+20*0.3,y-40*0.3,fill='brown',outline='brown')
    can1.create_rectangle(x-20*0.3,y-40*0.3,x+40*0.3,y-50*0.3,fill='green',outline='green')
    can1.create_rectangle(x-30*0.3,y-50*0.3,x+50*0.3,y-70*0.3,fill='green',outline='green')
    can1.create_rectangle(x-20*0.3,y-70*0.3,x+40*0.3,y-80*0.3,fill='green',outline='green')
    can1.create_rectangle(x,y-80*0.3,x+20*0.3,y-90*0.3,fill='green',outline='green')
   
    
def change():
    global x1,y1   
    while 1:
        i=0
        x1,y1=randrange(0,600),randrange(0,600)    
        if x1 in range(431,465) and y1 in range(63,100):
            i=1 
        if x1  in range(451,485) and y1 in range(363,400):
            i=1         
        if x1 in range(131,165) and y1 in range(463,500):
            i=1
        if x1 in range(raix,raix+10) and y1 in range(raiy,raiy+10):
            i=1
        if i == 0:
            if x1%10 == 0 and y1%10 == 0:
                break
    apple(x1,y1)
    aumento()

def restart():
    global m,x,y,cu,z,h,q,u,m,p,xt,yt,x1,y1,bu,can1

    m.pack_forget()    
    bu.pack_forget()
    
    x,y=[300],[300]
    cu=[0]*1
    z,h,q,u,m,p=0,0,0,1,0,0
    xt,yt=[300],[300]
    x1,y1=randrange(0,590),randrange(0,590)
    
    can1 = Canvas(root,bg='light blue',height=600, width=600)
    can1.pack(side=LEFT, padx =5, pady =5)
    
    cu[0]=can1.create_rectangle(x[0],y[0],
                            x[0]+10,y[0]+10,fill='green',outline='green')

    while 1:
        i=0
        x1,y1=randrange(0,600),randrange(0,600)    
        if x1 in range(431,465) and y1 in range(63,100):
            i=1 
        if x1  in range(451,485) and y1 in range(363,400):
            i=1         
        if x1 in range(131,165) and y1 in range(463,500):
            i=1
        if i == 0:
            if x1%10 == 0 and y1%10 == 0:
                break
    arbre(450,100)
    arbre(470,400)
    arbre(150,500)
    start(x1,y1)


def aumento():
    global cu,x,y,u,m,up
    up=1
    i=0
    cu.append(0)
    if q > 1:
        r,t=x[len(x)-1]+10,y[len(y)-1]
    else:
        r,t=x[len(x)-1],y[len(y)-1]+10
    x.append(r)
    y.append(t)
    cu[len(cu)-1]=can1.create_rectangle(x[len(x)-1],y[len(y)-1]
                    ,x[len(x)-1]+10,y[len(y)-1]+10,fill='green',outline='green')
    i=0
    while i < len(x)-1*u:
        xt.append(0)
        yt.append(0)
        i+=1
    u+=1
    root.after(1000,uP)
    
def uP():
    global up
    up=0
    
def comprobar():
    i=0
    while i < 11:
        if raix+i in range(x[0],x[0]+10) and raiy+i in range(y[0],y[0]+10):
            rainbowC()

        i+=1
    root.after(100-2*(len(x)-1),comprobar)

def move():
    global x,y,z,q,xt,yt,bu,p,m,power
    i=0
    while i < len(x):
        if q == 2:
            xt.append(x[i])
            yt.append(y[i])
        if q== -2:
            xt.append(x[i])
            yt.append(y[i])

        if q == 1:
            yt.append(y[i])
            xt.append(x[i])
        if q == -1:
            yt.append(y[i])
            xt.append(x[i])

        xt.pop(0)
        yt.pop(0)
        i+=1
    if q == 1:
        y[0]=y[0]+10
        i+=1
    elif q ==-1:
        y[0]=y[0]-10
        i+=1
    elif q==-2:
        x[0]=x[0]+10
        i+=1
    elif q==2:
        x[0]=x[0]-10
        i+=1

    if x[0]< 0 or x[0] > 600 or y[0] < 0 or y[0]>600:
        z=1
    if power == 0:
        if x[0] in range(431,465) and y[0] in range(63,100):
            z=1 
        if x[0] in range(451,485) and y[0] in range(363,400):
            z=1         
        if x[0] in range(131,165) and y[0] in range(463,500):
            z=1
    i=1
    if up ==0:
        while i < len(x):
            s=0
            while s < 10:
                if x[0]+s in range(x[i], x[i]+10) and y[0]+s in range(y[i],y[i]+10):
                    z=1
                s+=1
            i+=1
    if z == 1:
        can1.pack_forget()
        m=Message(root,text='GAME OVER',font=('times',60,'bold'),bg='light blue',fg='red')
        m.pack()
        bu=Button(root,text='Restart',command=restart)
        bu.pack()
    i = 0
    can1.coords(cu[0],x[0],y[0],x[0]+10,y[0]+10)
    
    if len(cu) > 1:
        while i < len(cu)-1:
            can1.coords(cu[i+1],xt[i],yt[i],xt[i]+10,yt[i]+10)
            x[i+1],y[i+1] = xt[i],yt[i]
            i+=1
    i=0
    while i < 11:
        if x1+i in range(x[0],x[0]+10) and y1+i in range(y[0],y[0]+10):
            change()
        i+=1
    if z == 0:
        root.after(100-2*(len(x)-1),move)
      
            
x,y=[300],[300]
cu=[0]
raix,raiy=0,0    
z,h,q,u,m,p,up=0,0,0,1,0,0,0
xt,yt=[300],[300]
man=[0]*8
rai=[0]*11
power=0

while 1:
    i=0
    x1,y1=randrange(0,600),randrange(0,600)    
    if x1 in range(431,465) and y1 in range(63,100):
        i=1 
    if x1  in range(451,485) and y1 in range(363,400):
        i=1         
    if x1 in range(131,165) and y1 in range(463,500):
        i=1
    if i == 0:
        if x1%10 == 0 and y1%10 == 0:
            break

    
root = Tk()
root.configure(bg='black')
root.title('Snake')

can1 = Canvas(root,bg='light blue',height=600, width=600)
can1.pack(side=LEFT, padx =5, pady =5)

cu[0]=can1.create_rectangle(x[0],y[0],x[0]+10,y[0]+10,fill='green',outline='green')



start(x1,y1)

arbre(450,100)
arbre(470,400)
arbre(150,500)
 
root.bind('<Up>',movA)
root.bind('<Down>',movB)
root.bind('<Left>',movI)
root.bind('<Right>',movD)

root.after(randrange(10000,30000),rainbowI)
comprobar()

root.mainloop()
