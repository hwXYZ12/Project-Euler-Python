import math

rt = math.sqrt(2)
for n in range(1000):
    a = 2.0*(math.pow(3-2*rt,n))
    b = rt*math.pow(3.0-2*rt,n)
    c = 2.0*math.pow(3+2*rt,n)
    d = rt*math.pow(3+2*rt,n)
    y = (1.0/4)*(a+b+c-d)
    b = (y+1)/2
    x = 1.0/2*(math.sqrt(8*b*b-8*b+1)+1)
    print str(b)+" , x = "+str(x)