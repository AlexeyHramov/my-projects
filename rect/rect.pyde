rr = 5
 

def setup ():
    size(600,600)
    frameRate(75)
def draw ():
    global rr
    rectMode(CENTER)
    rect(300,300,rr,rr)
   
    
    rr =  rr + 5
    
