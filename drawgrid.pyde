size(500, 750)
def drawGrid():
    """
    This function draws a grid of horizontal and vertical lines.
    In this example we use a while loop.  Another example (shown below)
    drawGrid2() shows the same functionality but using a for loop.
    """
    
    #draw horizontal lines
    #y starts at zero and increases until it reaches height.
    y = 0
    while y <= height:  #stop when y is greater than height
        line(0, y, width, y)
        y += 20  #y = y + 20
        
    #draw vertical lines
    x = 0
    while x <= width: #stop when x is greater than width 
        line(x, 0, x, height)
        x += 20 #x = x + 20
        
#drawGrid()

def drawGrid2():
    """
    This function draws a grid of horizontal and vertical lines.
    In this example we use a for loop. This was not shown in class
    but is an alternate way to write the code above.
    """
    
    for y in range(0, height+1, 20):
        #height+1 so that y can be equal to the height
        line(0, y, width, y)
        #no need to increment y--that's done in the for loop
        
    #draw vertical lines
    for x in range(0, width+1, 20):
        line(x, 0, x, height)
        #no need to increment x -- that's done in the for loop
        
drawGrid2()
