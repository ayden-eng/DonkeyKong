import random
def setup():
     size(400,400)
     background(255,255,255)
   

boxx,boxy = 100,100
x,y = 0,305
timer,n,b = False,0,0
blocksX = [0]
blocksY = [0]
n =0
Key = 0
frame,frame2,frame3 = 1,1,1
barrleroll,m = 1,0
mario = 0
mario_Lwalk,mario_Rwalk = 1,1
direction,jump = "left","ON"
Height = 0
Background = 0
Kong = 1
Kong_animation= 4
On = ["on","on","on","off","off","off"]
lives = 3
def keyPressed ():
    global Key
    Key = key

def draw():
    global lives,frame3,boxx,boxy,x,y,timer,n,blocksX,blocksY,n,frame,barrleroll,m,mario,frame2,Key,b,Height
    global mario_Lwalk,direction,mario_Rwalk,jump,Kong_animation
    global Background,Kong
    rect(x,y,10,10)
    Background = loadImage("DonkeyKongMap1.png")
    background(255,255,255)
    image(Background,30,30,width*.8,height*.8)

    Kong = loadImage(str("DonkeyKong") + str(frame3)+str(".png"))
    image(Kong,110,49)
    marioL = loadImage("MarioIdle1.png")
    marioR = loadImage("MarioIdle3.png")
    mario_Lwalk = loadImage(str("LMarioWalk") + str(frame2)+str(".png"))
    mario_Rwalk = loadImage(str("RMarioWalk") + str(frame2)+str(".png"))
    if keyPressed == False:
        if direction == "left" or direction == "left" and Key == "w" :
            image(marioL,x,y,width/20,height/20)
        if direction == "right" or direction == "Right" and Key == "w":
            image(marioR,x,y,width/20,height/20)
            #Key = 'v'
    if Key == "j":
        jump == "ON"
    if jump == "ON":
        if Key == 'w':
            Key = "v"
            jump = "OFF"
            
            
   
    if keyPressed == True:
        if Key == 'w' or Key == 'a' or Key == 's' or Key == 'd':
            if Key == 'a':
                x -= 1
                image(mario_Lwalk,x,y,width/20,height/20)
                direction = "left"
            if Key == 'd':
                x += 1
                image(mario_Rwalk,x,y,width/20,height/20)
                direction = "right"
                    
    if jump == "OFF":

        if keyPressed == True:
            if direction == "left":
                Key = 'a'
            if direction == "right":
                Key = 'd'
            if direction == "left" or direction == "left" and Key == "w" :
                image(mario_Lwalk,x,y,width/20,height/20)
            if direction == "right" or direction == "Right" and Key == "w":
                image(mario_Rwalk,x,y,width/20,height/20)
        if Height < 4:
            for i in range (1,200):
                b += 0.001
                if b >= 1:
                    y -= 8
                    Height += 1
                    
                    b = 0
        if Height < 8 and Height >= 4:
            for i in range (1,200):
                b += 0.001
                if b >= 1:
                    y += 8
                    Height += 1
                    b = 0
                    jump == "ON"
        if Height == 8:
            Height =0
            jump = "ON"
                
    barrleroll = loadImage(str("Barrelroll") + str(frame)+str(".png"))
    for i in range(1,len(blocksX)):
        image(barrleroll,blocksX[i],blocksY[i],width/25,height/25)
        if x <= blocksX[i] + 15 and x >= blocksX[i] - 18:
            if y >= blocksY[i] - 20 and y <= blocksY[i] + 15:
                lives -=1
    
    if timer == False:
        for i in range(1,200):
            n += 0.001
            if n >= 50:
                Kong_animation = random.randint(0,5)
                n = 0
     #__________________________________________________________________________
    if timer == False:
        for i in range(1,200):
            m += 0.001
            if m >= 5:
                frame2 += 1
                if frame2 == 3:
                    frame2 = 1
                if On[Kong_animation] == 'on':
                    frame3 += 1
                    if frame3 == 4:
                        Kong_animation = 4
                        frame3 = 1
                        blocksX.append(152)
                        blocksY.append(65)
                       
            if m >=5:
                m = 0
                frame += 1
                if frame == 5:
                    frame = 1

    for i in range(0,len(blocksX)):
        if blocksX[i] <= 222 and blocksY[i] == 65:
            blocksX[i] += 1
        if blocksX[i] >= 222 and blocksX[i] <= 260 and blocksY[i] <= 125:
            blocksX[i] += 0.4
            blocksY[i] += 1
        if blocksY[i] == 126 and blocksX[i] >= 154:
            blocksX[i] -= 1
        if blocksX[i] <= 154 and blocksY[i] <=186 and blocksY[i] >= 125 :
            blocksY[i] += 1
        if blocksY[i] == 187 and blocksX[i] >= 68:
            blocksX[i] -= 1
        if blocksX[i] <= 68 and blocksY[i] <= 247 and blocksY[i] >= 186:
            blocksY[i] +=1
        if blocksY[i] == 248 and blocksX[i] <= 297 :
            blocksX[i] += 1
        if blocksX[i] >= 297 and blocksY >=248 and blocksY[i] <= 308: 
            blocksY[i] += 1
        if blocksY[i] == 309:
            blocksX[i] -= 1
    if lives == 0:
        while 1==1:
            print("DEAD")
