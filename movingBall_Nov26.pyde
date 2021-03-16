xPos = 2
speed = 10
direction = 1
#start the program, not start the function
animate = False

def keyPressed():
    global animate
    animate = not(animate)

def setup():
    size(500, 500)
    #draw is been called three times per sec, instead of 60
    frameRate(20)
    
    
    
def draw():
    global xPos, speed, direction
    if animate:
        background(0)
        fill(random(255), random(255), random(255))
        
        if xPos >= width or xPos <= 0:
            direction = direction * -1
        xPos = xPos + speed * direction
        
        ellipse(xPos, 255, 60, 60)
    

    
