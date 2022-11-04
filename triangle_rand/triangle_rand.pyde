rr = 5
k=random(600)
m=random(600)
n=random(20)
j=random(600)
l=random(600)
p=random(600)
r=random(600)
def setup ():
    size(1200,1200)
    frameRate(125)
  
   
def draw ():
    global rr,n,m,j,l,p,r
    triangle(k-n, m+n, r+rr, j-rr, l+rr, p+rr)
    
    n=n+2
    rr = rr + 1
    
