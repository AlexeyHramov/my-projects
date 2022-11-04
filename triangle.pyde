rr = 5
 

def setup ():
    size(600,600)
    frameRate(125)
    
def draw ():
    global rr
    triangle(280-rr, 350+rr, 292, 320-rr, 304+rr, 350+rr)
    rr =  rr + 1
