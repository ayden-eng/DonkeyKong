def setup():
    size(400,400)
    background(255,255,255)
   
timer = False
boxx,boxy = 100,100
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
    rect(boxx,boxy,10,10)
    if x <= boxx + 10 and x >= boxx - 10:
        if y >= boxy - 10 and y <= boxy + 10:
            print "ok"
   
    print("")
