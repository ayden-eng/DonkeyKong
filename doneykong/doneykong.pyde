def setup():
     size(400,400)
     background(255,255,255)
   

boxx,boxy = 100,100
x,y = 200,200
timer,n = False,0
blocksX = []
blocksY = []
n =0
frame = 1
barrleroll,m = 1,0
def draw():
     global boxx,boxy,x,y,timer,n,blocksX,blocksY,n,frame,barrleroll,m
     rect(x,y,10,10)

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
        image(barrleroll,blocksX[i],blocksY[i])
        if x <= blocksX[i] + 10 and x >= blocksX[i] - 10:
            if y >= blocksY[i] - 10 and y <= blocksY[i] + 10:
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
                        blocksX[i] += 10
                    rect(blocksX[i],blocksY[i],10,10)
     print(frame)
     #__________________________________________________________________________
     if timer == False:
        for i in range(1,200):
            m += 0.001
            if m >=5:
                m = 0
                frame += 1
                if frame == 4:
                    frame = 1
