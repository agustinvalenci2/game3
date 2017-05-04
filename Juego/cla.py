import tkinter
import math
import random
wind = tkinter.Tk()
menu = tkinter.Tk()
(distancia,levelid,GAS)=(0,0,25000)
minivanvel = [5,25,30,35,45,105]
fightvel = [5,10,15,20,25,90]
Save = open("save.txt","r+")
class enemigos:
    def collisions(self, item1,item2,push):
        global GAS
        h=90
        xp =Canvas.coords(item1)[0]
        yp =Canvas.coords(item1)[1]
        xm = Canvas.coords(item2)[0]
        ym = Canvas.coords(item2)[1]
        if(xp>=xm and xp<=xm+h and yp>=ym and yp<=ym+h or(xp+h>=xm and xp+h<=xm+h and yp>=ym and yp<=ym+h)):
            if(Canvas.coords(player)[0]<250):
                Canvas.move(player,-push,0)
            else:
                Canvas.move(player,push,0)
            GAS-=500
            if(item2==misil1 or item2 ==misil2):
                GAS=0
            if(item2==gasolina or item2==gasolina2):
                GAS+=3000
                if(item2==gasolina):
                    mons.limite_Y(gasolina,Canvas.coords(gasolina)[1])
                else:
                    mons.limite_Y(gasolina2,Canvas.coords(gasolina2)[1])
    def minivan(self,item,v):
        """
        """
        Canvas.move(item,0,v)

    def fighter(self,item,dx,dy):
        itemf = item
        if(Canvas.coords(player)[0]<Canvas.coords(itemf)[0]):
            Canvas.move(itemf,-dx,dy)
            
        elif(Canvas.coords(player)[0]>Canvas.coords(itemf)[0]):
            Canvas.move(itemf,dx,dy)
            
        if(Canvas.coords(player)[0]==Canvas.coords(itemf)[0]):
            Canvas.move(itemf,0,dy)
    def runner(self,item,v):
        itemr = item
        z = random.randint(-100,100)               
        Canvas.move(itemr,z,v)
    def cos(self,item,f,v):
        itemc = item
        y= math.sin(Canvas.coords(itemc)[1]*math.pi/(f))*400
        Canvas.move(itemc,y,v)
    def sin(self,item,f,v):
        items = item
        y= math.sin(Canvas.coords(items)[1]*math.pi/f)*50
        Canvas.move(items,y,v)
    def limite_Y(self,item,limit):
        itemY = item
        if(Canvas.coords(itemY)[1]>=limit):
            Canvas.move(itemY,0,-limit)
    def limite_X(self,item,izq,der):
        global GAS
        if(Canvas.coords(item)[0]>=der):
            Canvas.move(item,-50,0)
            if(item==player):
                GAS=GAS//10
        if(Canvas.coords(item)[0]<=izq):
            Canvas.move(item,50,0)
            if(item==player):
                GAS=GAS//10
                
def boton(item,x,y):
        h=50
        if(CC.coords(item)[0]<x and CC.coords(item)[0]+h>x and CC.coords(item)[1]<y and CC.coords(item)[1]+h>y):
             return True
        else:
            return False
def nivel(Id):
       global levelid
       menu.wm_iconify()
  
       wind.wm_deiconify()
       levelid=Id
       Canvas.focus_set()
       label.pack(side = tkinter.RIGHT)
       Canvas.pack()
       main()
def nivelselec(event):
    global levelid
    menu.focus_set()
    if(boton(boton1,event.x,event.y)):
       nivel(0)
    if(boton(boton2,event.x,event.y)):
       nivel(1)
    if(boton(boton3,event.x,event.y)):
       nivel(2)
    if(boton(boton4,event.x,event.y)):
       nivel(3)
    if(boton(boton5,event.x,event.y)):
       nivel(4)
       
def key(event):
    global levelid,distancia,Save
    """
    """
    tecla = repr(event.char)

    if(tecla=="'d'" or tecla =="'D'"):
        Canvas.move(player,15,0)
    if(tecla=="'a'" or tecla =="'A'"):
        Canvas.move(player,-15,0)
    if(tecla=="'s'" or tecla =="'S'"):
        Save.seek(0)
        score= "\nlevel:  "+str(levelid+1)+"\n"+"gas: "+str(GAS)+"\n"+ "distance: "+str(distancia)+"\nplayer: "+e.get()
        Save.write(score)
       
    
        
 
mons = enemigos()       
Canvas = tkinter.Canvas(wind,height=900,width=900,bg="black")
Canvas.bind("<Key>", key) 
play = tkinter.PhotoImage(file="player.png")
enemigo4 = tkinter.PhotoImage(file="enemigo1.png")
enemigo2 = tkinter.PhotoImage(file="enemigo2.png")
enemigo3 = tkinter.PhotoImage(file="enemigo3.png")
enemigo1 = tkinter.PhotoImage(file="enemigo4.png")
enemigo5 = tkinter.PhotoImage(file="enemigo5.png")
enemigo6 = tkinter.PhotoImage(file="enemigo6.png")
BOOM = tkinter.PhotoImage(file="Bomb_Explosion.png")
gasolina=Canvas.create_rectangle(550,-100,500,-50,fill="white")
gasolina2=Canvas.create_rectangle(350,-100,300,-50,fill="white")
mini=Canvas.create_image(450,-150,image=enemigo1)
runner=Canvas.create_image(160,-150,image=enemigo2)
fight = Canvas.create_image(350,-150,image=enemigo3)
misil1 = Canvas.create_image(150,-150,image=enemigo6)
misil2 = Canvas.create_image(750,-150,image=enemigo6)
player = Canvas.create_image(450,650,image=play)
sini=Canvas.create_image(550,-650,image=enemigo4)
sini2=Canvas.create_image(150,-650,image=enemigo5)

e = tkinter.Entry(menu)

wind.iconify()
lista =[mini,runner,sini,fight,sini2,misil1,misil2,gasolina,gasolina2]


def limit(listid):
    mons.limite_Y( lista[listid],900)
    mons.limite_X( lista[listid],0,900)
    mons.collisions(player,lista[listid],50)
def main():
    global GAS,distancia,levelid,Save
    GAS-=25  
    distancia+=10
    a.set("\n\n\n\n\n\n\n\n\n\n\nlevel:  "+str(levelid+1)+"\n\n\n\n"+" gas: "+str(GAS)+"\n\n\n\n\ndistance: "+str(distancia)+"\nplayer:\n\n\n\n\n\n\n "+e.get()+"\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    mons.minivan(lista[0],minivanvel[levelid])
    limit(0)
    mons.runner( lista[1],minivanvel[levelid]*1.3)
    limit(1)
    mons.sin( lista[2],100,minivanvel[levelid]*1.5)
    limit(2)
    mons.fighter( lista[3],fightvel[levelid],minivanvel[levelid]*2)
    limit(3)
    mons.cos( lista[4],60,minivanvel[levelid])
    limit(4)
    mons.minivan(lista[5],minivanvel[levelid])
    limit(5)   
    mons.minivan(lista[6],minivanvel[levelid])
    limit(6)
    mons.minivan(lista[7],minivanvel[levelid])
    limit(7)
    mons.minivan(lista[8],minivanvel[levelid])
    limit(8)
    mons.limite_X(player,0,900)
    
    if(distancia>5000 and levelid<=5):
        levelid+=1
        distancia=0
    if(GAS<15):
        Canvas.create_image(Canvas.coords(player)[0],Canvas.coords(player)[1],image=BOOM)
        Save.close()
        return 0
    Canvas.after(15,main)
 
CC = tkinter.Canvas(menu,height=400,width=400)
CC.bind("<Button-1>",nivelselec)
boton1 =CC.create_rectangle(100,150,150,200,fill="white")
boton2 =CC.create_rectangle(160,150,210,200,fill="light blue")
boton3 =CC.create_rectangle(220,150,270,200,fill="green")
boton4 =CC.create_rectangle(280,150,330,200,fill="purple")
boton5 =CC.create_rectangle(340,150,390,200,fill="red")
a = tkinter.StringVar()
label = tkinter.Label(wind,textvariable= a,font=("Times",12,"bold"),fg="white",bg="black")

e.pack()
CC.pack()        
        

