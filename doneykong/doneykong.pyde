def setup():
     size(400,400)
     background(255,255,255)
   

boxx,boxy = 100,100
x,y = 0,0
timer,n = False,0
blocksX = [0]
blocksY = [0]
n =0
frame = 1
barrleroll,m = 1,0
mario = 0
def draw():
    global boxx,boxy,x,y,timer,n,blocksX,blocksY,n,frame,barrleroll,m,mario
    rect(x,y,10,10)
    background(255,255,255)
    mario = loadImage("MarioIdle1.png")
    if keyPressed == False:
        image(mario,x,y,width/20,height/20)
    if keyPressed == True:
        if key == 'w' or 'a' or 's' or 'd':
            if key == 'w':
                y -= 1
            if key == 's':
                y += 1
            if key == 'a':
                x -= 1
            if key == 'd':
                x += 1
    barrleroll = loadImage(str("Barrelroll") + str(frame)+str(".png"))
    for i in range(1,len(blocksX)):
        image(barrleroll,blocksX[i],blocksY[i],width/25,height/25)
        if x <= blocksX[i] + 15 and x >= blocksX[i] - 18:
            if y >= blocksY[i] - 20 and y <= blocksY[i] + 15:
                print "ok"
    
    if timer == False:
        for i in range(1,200):
            n += 0.001
            if n >= 20:
                n = 0
                blocksX.append(1)
                blocksY.append(1)
                for i in range(0,len(blocksX)):
                    if blocksX[i] >= 1:
                        blocksX[i] += 20
     #__________________________________________________________________________
    if timer == False:
        for i in range(1,200):
            m += 0.001
            if m >=5:
                m = 0
                frame += 1
                if frame == 4:
                    frame = 1
    
