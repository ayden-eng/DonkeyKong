import random
def setup():
    size(800,800)
    background(0, 0, 0) #Black Background
    global status
    status = 0 #0 = Main Menu, 1 = In-Game, 2 = Help, 3 = Lose, 4 = Win
    #########################################################################
    global PBm_Height #Amount Main Menu Play Button Height is to be divided by during mouse hover
    global HBm_Height #Amount Main Menu Help Button Height is to be divided by during mouse hover
    PBm_Height = 6 
    HBm_Height = 6 
    global PBm_Width #Amount Main Menu Play Button Width is to be divided by during mouse hover
    global HBm_Width #Amount Main Menu Play Button Width is to be divided by during mouse hover
    PBm_Width = 3 
    HBm_Width = 3 
    #########################################################################
    global PBm_X #Main Menu Play Button X Position 
    global PBm_Y #Main Menu Play Button Y Position 
    PBm_X = 260 
    PBm_Y = 450 
    global HBm_X #Main Menu Help Button X Position
    global HBm_Y #Main Menu Help Button Y Position
    HBm_X = 260
    HBm_Y = 600
    #########################################################################
    global GameIconMain
    GameIconMain = loadImage("DonkeyKongIcon.png") #Game Icon For Display In Main Menu
    global PlayButtonMain
    PlayButtonMain = loadImage("DK Play Button.png") #Main Menu Play Button 
    global HelpButtonMain
    HelpButtonMain = loadImage("DK Help Button.png") #Main Menu Help Button
   

boxx,boxy = 100,100
x,y = 0,500
X_barrel,Y_barrel = 285,95
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
Kong_animation= 0
Kong_animation1 = 0
On = ["on","off","off","throw","off","off"]
On1 = ["off","off","off","throw","throw","off"]
lives = 3
wait = False
def keyPressed ():
    global Key
    Key = key

def draw():
    global Kong_animation1,On1,wait,X_barrel,Y_barrel,lives,frame3,boxx,boxy,x,y,timer,n,blocksX,blocksY,n,frame,barrleroll,m,mario,frame2,Key,b,Height
    global mario_Lwalk,direction,mario_Rwalk,jump,Kong_animation
    global Background,Kong
    global status #Control Variables
    global GameIconMain, PlayButtonMain, HelpButtonMain #Image Assets
    global PBm_Height, HBm_Height, PBm_Width, HBm_Width #Scaling Variables
    global PBm_X, HBm_X, PBm_Y, HBm_Y #Coordinate Variables
    if (status == 0): #Main Menu
        background(0, 0, 0) #Overlays The Hover To Prevent Button Overlapping
        image(GameIconMain, 135, -30, width / 1.5, height / 1.5) #Load Game Icon in Main Menu
        image(PlayButtonMain, PBm_X, PBm_Y, width / PBm_Width, height / PBm_Height) #Load Play Button In Main Menu
        image(HelpButtonMain, HBm_X, HBm_Y, width / HBm_Width, height / HBm_Height) #Load Help Button In Main Menu
    elif (status == 1): #In Game
        rect(x,y,10,10)
        Background = loadImage("DonkeyKongMap1.png")
        background(0, 0, 0)
        image(Background, 0, 0, width * 1, height * 1)

        Kong = loadImage(str("DonkeyKong") + str(frame3)+str(".png"))
        image(Kong,200,48, width * 0.1, height * 0.1)
        marioL = loadImage("MarioIdle1.png")
        marioR = loadImage("MarioIdle3.png")
        mario_Lwalk = loadImage(str("LMarioWalk") + str(frame2)+str(".png"))
        mario_Rwalk = loadImage(str("RMarioWalk") + str(frame2)+str(".png"))
        if keyPressed == False:
            if direction == "left" or direction == "left" and Key == "w" :
                image(marioL,x,y,width/17.5,height/17.5)
            if direction == "right" or direction == "Right" and Key == "w":
                image(marioR,x,y,width/17.5,height/17.5)
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
                    x -= 5
                    image(mario_Lwalk,x,y,width/17.5,height/17.5)
                    direction = "left"
                if Key == 'd':
                    x += 5
                    image(mario_Rwalk,x,y,width/17.5,height/17.5)
                    direction = "right"
                    
        if jump == "OFF":

            if keyPressed == True:
                if direction == "left":
                    Key = 'a'
                if direction == "right":
                    Key = 'd'
                if direction == "left" or direction == "left" and Key == "w" :
                    image(mario_Lwalk,x,y,width/17.5,height/17.5)
                if direction == "right" or direction == "Right" and Key == "w":
                    image(mario_Rwalk,x,y,width/17.5,height/17.5)
            if Height < 4:
                for i in range (1,200):
                    b += 0.001
                    if b >= 1:
                        y -= 16
                        Height += 1
                    
                        b = 0
            if Height < 8 and Height >= 4:
                for i in range (1,200):
                    b += 0.001
                    if b >= 1:
                        y += 8
                        Height += 0.5
                        b = 0
                        jump == "ON"
            if Height == 8:
                Height =0
                jump = "ON"
        
        barrleroll = loadImage(str("Barrelroll") + str(frame)+str(".png"))
        barrleroll1 = loadImage(str("Barrelroll") + str(frame)+str(".png"))
        for i in range(1,len(blocksX)):
            image(barrleroll,blocksX[i],blocksY[i],width/25,height/25)
            if x <= blocksX[i] + 32 and x >= blocksX[i] - 42 or x <= X_barrel + 32 and x >= X_barrel -42:
                if y >= blocksY[i] - 45 and y <= blocksY[i] + 30 or y >= Y_barrel - 45 and y <= Y_barrel+30:
                    lives -= 1
            
        if timer == False:
            for i in range(1,200):
                n += 0.001
                if n >= 20:
                    if wait == False:
                        Kong_animation1 = random.randint(0,5)
                        X_barrel,Y_barrel = 285,95
                    Kong_animation = random.randint(0,5)
                    n = 0
                  
                   
                        
                        
    #__________________________________________________________________________
        if timer == False:
            for i in range(1,200):
                m += 0.001
                if m >= 3:
                    frame2 += 1
                    if frame2 == 3:
                        frame2 = 1
                    if On[Kong_animation] == 'on':
                        frame3 += 1
                        if frame3 == 4:
                            Kong_animation = 4
                            frame3 = 1
                            blocksX.append(285)
                            blocksY.append(95)
                
                if m >=3:
                    m = 0
                    frame += 1
                    if frame == 5:
                        frame = 1
                
        for i in range(0,len(blocksX)):
            if blocksX[i] <= 481 and blocksY[i] == 95:
                blocksX[i] += 3.5
            if blocksX[i] >= 481 and blocksX[i] <= 596 and blocksY[i] <=246 and blocksY[i] >= 95 :
                blocksX[i] += 2.5
                blocksY[i] += 3.5
            if blocksY[i] == 249 and blocksX[i] >= 591 and blocksX[i] <= 770:
                blocksX[i] += 3.5
            if blocksX[i] >= 770 and blocksY[i] == 249:
                blocksY[i] += 1
   
            if blocksY[i] == 250 and blocksX[i] <= 800 and blocksX[i] >= 308:
                blocksX[i] -=3.5
         
            if blocksX[i] == 307.5 and blocksY[i] >= 250 and blocksY[i] <= 399:
                blocksY[i] += 3.5
        if On1[Kong_animation1] == "throw":           
                image(barrleroll,X_barrel,Y_barrel,width/25,height/25)
                wait = True
                if X_barrel >= x:
                    X_barrel -= 1
                if X_barrel <= x:
                    X_barrel += 1
                Y_barrel += 3 
                if Y_barrel >= 800:
                    wait = False
                    print("ok")
                    Kong_animation1 = 0
                    print("ok")
                    X_barrel,Y_barrel = 285,95
        print(On1[Kong_animation1],Kong_animation1,wait,X_barrel,Y_barrel)
                            

            
            # if blocksX[i] >= 222 and blocksX[i] <= 260 and blocksY[i] <= 125:
            #     blocksX[i] += 0.4
            #     blocksY[i] += 1
            # if blocksY[i] == 126 and blocksX[i] >= 154:
            #     blocksX[i] -= 1
            # if blocksX[i] <= 154 and blocksY[i] <=186 and blocksY[i] >= 125 :
            #     blocksY[i] += 1
            # if blocksY[i] == 187 and blocksX[i] >= 68:
            #     blocksX[i] -= 1
            # if blocksX[i] <= 68 and blocksY[i] <= 247 and blocksY[i] >= 186:
            #     blocksY[i] +=1
            # if blocksY[i] == 248 and blocksX[i] <= 297 :
            #     blocksX[i] += 1
            # if blocksX[i] >= 297 and blocksY >=248 and blocksY[i] <= 308: 
            #     blocksY[i] += 1
            # if blocksY[i] == 309:
            #     blocksX[i] -= 1
        if lives == 0:
            while 1==1:
                print("DEAD")
                
    elif (status == 2):
        instructions = loadImage("DK Tutorial.png")
        image(instructions, 0, 0, width / 1, height / 1)
            
            
def mousePressed(): #Button Click Detection
    global status
    println((mouseX, mouseY)) #For Mouse Click Position Testing Purposes
    if (status == 0):
        if ((mouseX >= 130 and mouseX <= 261) and (mouseY >= 203 and mouseY <= 265)): #Play Button is clicked
            println("Play Button Was Clicked")
            status = 1
        elif ((mouseX >= 130 and mouseX <= 261) and (mouseY >= 275 and mouseY <= 340)): #Help Button is clicked
            println("Help Button Was Clicked")
            status = 2
        else: 
            println("No Button Click detected") #No Button Click Detected
            
def mouseMoved():
    global status
    global PBm_Height, HBm_Height, PBm_Width, HBm_Width #Scaling Variables
    global PBm_X, HBm_X, PBm_Y, HBm_Y #Coordinate Variables
    if (status == 0):
        if ((mouseX >= 130 and mouseX <= 261) and (mouseY >= 203 and mouseY <= 265)):
            PBm_Height = 5.5 #Increases The Play Button Size when Mouse hovers over it
            PBm_Width = 2.75
            PBm_X = 250 #Adjusts X Position to keep Play Button centred
            PBm_Y = 450
        elif ((mouseX >= 130 and mouseX <= 261) and (mouseY >= 275 and mouseY <= 340)):
            HBm_Height = 5.5 #Increases The Help Button Size when Mouse hovers over it
            HBm_Width = 2.75
            HBm_X = 250 #Adjusts X Position to keep Help Button centred
            HBm_Y = 600
        else:
            PBm_Height = 6 #Restore Button Coordinates And Dimensions to Original If No Mouse Hover Is Detected
            PBm_Width = 3
            HBm_Height = 6
            HBm_Width = 3
            PBm_X = 260
            PBm_Y = 450
            HBm_X = 260
            HBm_Y = 600
