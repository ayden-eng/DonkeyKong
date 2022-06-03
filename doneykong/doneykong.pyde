def setup():
    size(400,400)
    background(255,255,255)
   
timer = False
boxx,boxy = [],[]
x,y = 200,200
n =0
def draw():
    global boxx,boxy,x,y,timer,n
    rect(x,y,10,10)

    if key == 'w':
        y -= 1
    if key == 's':
        y += 1
    if key == 'a':
        x -= 1
    if key == 'd':
        x += 1
    if 1==1:
        for i in range (1,len(boxx)):
            rect(boxx[i],boxy[i],10,10)
            if x <= boxx[i] + 10 and x >= boxx[i] - 10:
                if y >= boxy[i] - 10 and y <= boxy[i] + 10:
                    print "ok"
    if timer == False:

       for i in range(1,200):
           n += 0.001
           if n >= 30:
               n= 0 
               boxx.append(1)
               boxy.append(1)
    
               for i in range(1,len(boxx)):
                   if boxx[i] >= 0 and boxx[i] <= 150:
                      boxx[i] += 10
                   else:
                       boxy[i] += 10    
        
               
    print('')
