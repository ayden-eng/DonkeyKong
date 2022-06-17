import random
add_library('minim')
def setup():
    size(800,800)
    background(0, 0, 0) #Black Background
    global status, minim,gamesong,hitsong,deathsong #game songs
    minim=Minim(this) 
    gamesong = minim.loadFile("8d82b5_Sonic_Green_Hill_Zone_Theme_Song.mp3")# this is the game song 
    hitsong = minim.loadFile("puff.mp3") # this plays when you get hit
    deathsong = minim.loadFile("Mario Death - QuickSounds.com.mp3")# this plays when you die
    gamesong.loop() # this plays the theme song forever
    status = 0 #0 = Main Menu, 1 = In-Game, 2 = Help, 3 = Lose, 4 = Win, 5 = Preview
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
    global PreviewButtonHelp
    PreviewButtonHelp = loadImage("DK Preview Button.png")
    global HomeButtonPreview
    HomeButtonPreview = loadImage("DK Home Button.png")
   

boxx,boxy = 100,100 # throwing barrel x and y
x,y = 0,690 # players x and y 
X_barrel,Y_barrel = 285,95 # normal x and y 
timer,n,b = False,0,0 # timer for aninmations 
blocksX = [0] # x list for all barrels 
blocksY = [0] # y list for all barrels
n =0 # used as a delay for timers 
Key = 0 # checks for the pervouis key pressed 
frame,frame2,frame3 = 1,1,1 # frames for each animation
barrleroll,m = 1,0 # if the barrle is rolling 
mario = 0 # mario animation 
mario_Lwalk,mario_Rwalk = 1,1 # marios dircetions 
direction,jump = "left","ON" # jump direction 
Height = 0 # stop the jump 
Background = 0 # background 
Kong = 1 # kong aniamtion 
Kong_animation= 0 # frame 
Kong_animation1 = 0 # frame
On = ["on","off","off","on","off","on"] # percentage of throwing 
On1 = ["throw","off","throw","throw","off","off"] # percentage of thorwing 
lives = 3 # number of lives 
wait = False # stop the movement 
ladder = False # if mario is on a ladder 
def keyPressed (): # checks for if key was pressed 
    global Key
    Key = key

def draw():
    global ladder,Kong_animation1,On1,wait,X_barrel,Y_barrel,lives,frame3,boxx,boxy,x,y,timer,n,blocksX,blocksY,n,frame,barrleroll,m,mario,frame2,Key,b,Height 
    global mario_Lwalk,direction,mario_Rwalk,jump,Kong_animation
    global Background,Kong # assests
    global hitsong,deathsong # sounds 
    global status #Control Variables
    global GameIconMain, PlayButtonMain, HelpButtonMain, PreviewButtonHelp, HomeButtonPreview #Image Assets
    global PBm_Height, HBm_Height, PBm_Width, HBm_Width #Scaling Variables
    global PBm_X, HBm_X, PBm_Y, HBm_Y #Coordinate Variables
    if (status == 0): #Main Menu
        background(0, 0, 0) #Overlays The Hover To Prevent Button Overlapping
        image(GameIconMain, 135, -30, width / 1.5, height / 1.5) #Load Game Icon in Main Menu
        image(PlayButtonMain, PBm_X, PBm_Y, width / PBm_Width, height / PBm_Height) #Load Play Button In Main Menu
        image(HelpButtonMain, HBm_X, HBm_Y, width / HBm_Width, height / HBm_Height) #Load Help Button In Main Menu
    elif (status == 1): #In Game
        rect(x,y,10,10)
        Background = loadImage("DonkeyKongMap1.png") # loads the map
        background(0, 0, 0) # black background
        image(Background, 0, 0, width * 1, height * 1) 
        lady = loadImage("Lady 2.png") # addes the lady
        image(lady,630,80,width /10, height /15) 
        Kong = loadImage(str("DonkeyKong") + str(frame3)+str(".png"))
        image(Kong,200,48, width * 0.1, height * 0.1)
        marioL = loadImage("MarioIdle1.png")
        marioR = loadImage("MarioIdle3.png")
        mario_Lwalk = loadImage(str("LMarioWalk") + str(frame2)+str(".png"))
        mario_Rwalk = loadImage(str("RMarioWalk") + str(frame2)+str(".png"))
        if keyPressed == False or Key != 'a' and Key != 'd' and Key != 'w': # this prints mario stading still it check the direction of mario and print mario accodingly 
            if direction == "left" or direction == "left" and Key == "w" :
                image(marioL,x,y,width/17.5,height/17.5)
            if direction == "right" or direction == "Right" and Key == "w":
                image(marioR,x,y,width/17.5,height/17.5)
                #Key = 'v'
        if ladder == False: # stop jumping while on ladder 
            if Key == "j":
                jump == "ON"
            if jump == "ON":
                if Key == 'w':
                    Key = "v"
                    jump = "OFF"
                
                
            if keyPressed == True: # this makes mario move and jump
                if Key == 'w' or Key == 'a' or Key == 's' or Key == 'd':
                    if Key == 'a':
                        x -= 5
                        image(mario_Lwalk,x,y,width/17.5,height/17.5)
                        direction = "left"
                    if Key == 'd':
                        x += 5
                        image(mario_Rwalk,x,y,width/17.5,height/17.5)
                        direction = "right"
                        
            if jump == "OFF": # this is for when mario jumps 
    
                if keyPressed == True:
                    if direction == "left":
                        Key = 'a'
                    if direction == "right":
                        Key = 'd'
                    if direction == "left" or direction == "left" and Key == "w" :
                        image(mario_Lwalk,x,y,width/17.5,height/17.5)
                    if direction == "right" or direction == "Right" and Key == "w":
                        image(mario_Rwalk,x,y,width/17.5,height/17.5)
                if Height < 4: # y increases 
                    for i in range (1,200):
                        b += 0.001
                        if b >= 0.5:
                            y -= 16
                            Height += 1
                        
                            b = 0
                if Height < 8 and Height >= 4: # y decreaes 
                    for i in range (1,200):
                        b += 0.001
                        if b >= 0.5:
                            y += 8
                            Height += 0.5
                            b = 0
                            jump == "ON"
                if Height == 8:
                    Height =0
                    jump = "ON"
        print(x,y)
        lives2 = loadImage("DKlives.png") # print the hearts
        if lives >=1:
            image(lives2,0,0,width/18,height/18)
        if lives >=2:
            image(lives2,55,0,width/18,height/18)
        if lives >= 3:
            image(lives2,110,0,width/18,height/18)
        barrleroll = loadImage(str("Barrelroll") + str(frame)+str(".png")) # this makes the image of the barrle change deping on the frame
        barrleroll1 = loadImage(str("Barrelroll") + str(frame)+str(".png"))# this makes the image of the barrle change deping on the frame
        for i in range(1,len(blocksX)):
            image(barrleroll,blocksX[i],blocksY[i],width/25,height/25) # this for the collsions 
            if x <= blocksX[i] + 32 and x >= blocksX[i] - 42: 
                if y >= blocksY[i] - 45 and y <= blocksY[i] + 30: 
                    blocksY[i],blocksX[i] = -1000,-1000
                    lives -= 1
                    hitsong.play()
                    hitsong.rewind()
            if x <= X_barrel +32 and x >= X_barrel - 42: # this for the collsions 
                if y >= Y_barrel - 45 and y <= Y_barrel + 30:
                    X_barrel,Y_barrel = -1000,-1000
                    lives -= 1
                    hitsong.play()
                    hitsong.rewind()
        if timer == False: # this gets kong to throw barrles 
            for i in range(1,200):
                n += 0.001
                if n >= 20:
                    Kong_animation = random.randint(0,5)
                    if wait == False:
                        Kong_animation1 = random.randint(0,5)
                        X_barrel,Y_barrel = 285,95
                    n = 0
                  
                   
                        
    #__________________________________________________________________________
        if timer == False: # this changes the frames of the game
            for i in range(1,200):
                m += 0.001
                if m >= .4:
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
                
                if m >=.4:
                    m = 0
                    frame += 1
                    if frame == 5:
                        frame = 1
        if  x >= 604 and x <= 666: # this is all for checking if the player is on a ladder 
            if Key == "e":
                if y >= 540:
                    ladder = True
                    y -= 2
            if Key == "q":
                if y < 690 and y >= 538:
                    ladder = True
                    y += 2
        if x >= 66 and x <= 140:
            print("OK")
            if Key == "e":
                if y >= 390 and y <= 538:
                    ladder = True
                    y -= 2
            if Key == "q":
                if y >= 388 and y <= 536:
                    ladder = True
                    y += 2
        if x >= 280 and x <= 353:
            if Key == "e":
                if y <= 388 and y >= 85:
                    ladder = True
                    y -= 2
            if Key == 'q':
                if y >= 84 and y <= 386:
                    ladder = True
                    y += 2
        if x >= 579 and x <=625:
            if Key == "e":
                if y <= 388 and y >= 238:
                    ladder = True
                    y -= 2
            if Key == "q":
                if y >= 236 and y <= 386:
                    ladder = True
                    y += 2
        if x>= 687 and x <= 739:
            if Key == 'e':
                if y <= 238 and y >=85:
                    ladder = True
                    y -= 2 
            if Key == 'q':
                if y >= 83 and y <= 234:
                    ladder = True
                    y += 2
        if y <= 84 and x <= 440 and x >= 410: # this makes the player move again when on the proper y axis 
            x -= 5
        if y == 84 and x <= 664 and x >= 640:
            status = 4
        if x >= 265 and y <= 161 and y >= 388:
            x += 5
        print(status)
        if y == 540 or y == 538 or y == 539 or y == 690 or y == 388 or y == 84 or y == 236:
            ladder = False
        if x <= 92 and y <= 582 and y >=265:
            x += 5
        if y == 690 and x <= 0:
             x += 5
        if y == 690 and x >= 750 or y == 388 and x >=750:
            x -= 5
        if y <= 538 and y >= 482 and x >= 616:
            x -= 5
        if y == 84 and x <= 0:
            x += 5
        if y <= 800 and x >= 760:
            x -= 5
        
        if ladder == True: # THIS PRINTS MARIO ON THE LADDER 
                if direction == "left" or direction == "left" and Key == "w" :
                    image(marioL,x,y,width/17.5,height/17.5)
                if direction == "right" or direction == "Right" and Key == "w":
                    image(marioR,x,y,width/17.5,height/17.5)
        # THIS MOVES THE BARRLES IN THE RIGHT WHY 
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
            if blocksY[i] == 400.5 and blocksX[i] <= 307.5 and blocksX[i] >= 100:
                blocksX[i] -=3.5
  
            if blocksX[i] == 97.5 and blocksY[i] >= 399.5 and blocksY[i] <= 550:
                blocksY[i] += 3.5
            if blocksY[i] == 551 and blocksX[i] >= 97.5 and blocksX[i] <=670:
                blocksX[i] += 3.5
            if blocksX[i] == 671.5 and blocksY[i] >= 551 and blocksY[i] <= 700:
                blocksY[i] += 3.5
            if blocksY[i] == 701.5:
                blocksX[i] -= 3.5
            # THIS MAKES KONG THOW BARRLES STARIGHT DOWN
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
                    Kong_animation1 = 0
                    X_barrel,Y_barrel = 285,95
           
        if lives == 0:
            status = 3
                
    elif (status == 2): # GI SCREEN
        instructions = loadImage("DK Tutorial.png")
        image(instructions, 0, 0, width / 1, height / 1)
        image(PreviewButtonHelp, 20, 700, width / 6, height / 10.5)
        
    elif (status == 3): # GI SCREEN
        Gameover = loadImage("DeathScreen DK.png")
        image(Gameover, 0, 0)
        
    elif (status == 4): # GI SCREEN
        won = loadImage("VictoryScreen DK.png")
        image(won, 0, 0)
        
    elif (status == 5): # GI SCREEN
        background(0, 0, 0)
        futhshckisit = loadImage("DonkeyKongMap1.png")
        image(futhshckisit, 0, 0, width / 1, height / 1)
        buttonn = loadImage("DK Home Button.png")
        image(buttonn, 15, 15, width / 7.5, height / 10)

    if  status == 3: # GI SCREEN
        gamesong.pause()
        deathsong.play()
            
def mousePressed(): #Button Click Detection
    global status
    println(str(mouseX) + ', ' + str(mouseY))
    if (status == 0):
        if ((mouseX >= 262 and mouseX <= 523) and (mouseY >= 455 and mouseY <= 578)): #Play Button is clicked
            println("Play Button Was Clicked")
            status = 1
        elif ((mouseX >= 262 and mouseX <= 523) and (mouseY >= 604 and mouseY <= 727)): #Help Button is clicked
            println("Help Button Was Clicked")
            status = 2
        else: 
            println("No Button Click detected") #No Button Click Detected
    elif (status == 2):
        if ((mouseX >= 21 and mouseX <= 152) and (mouseY >= 700 and mouseY <= 775)):
            println("Preview Button Was Clicked")
            status = 5
    elif (status == 5):
        if ((mouseX >= 15 and mouseX <= 118) and (mouseY >= 18 and mouseY <= 95)):
            println("Return to home")
            status = 0
    
def mouseMoved():
    global status
    global PBm_Height, HBm_Height, PBm_Width, HBm_Width #Scaling Variables
    global PBm_X, HBm_X, PBm_Y, HBm_Y #Coordinate Variables
    if (status == 0):
        if ((mouseX >= 262 and mouseX <= 523) and (mouseY >= 455 and mouseY <= 578)):
            PBm_Height = 5.5 #Increases The Play Button Size when Mouse hovers over it
            PBm_Width = 2.75
            PBm_X = 250 #Adjusts X Position to keep Play Button centred
            PBm_Y = 450
        elif ((mouseX >= 262 and mouseX <= 523) and (mouseY >= 604 and mouseY <= 727)):
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
