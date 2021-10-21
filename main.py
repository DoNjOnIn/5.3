import math

def sum(x):
    q=1
    v=q
    for i in range(6):
        R=x/i
        q*=R
        v+=q
    return v

def k(x):
    if x>-1 and x<1:
        return sum(x)/(math.e ** x)
    else:
        return (math.e**x + math.sin(x))/(math.cos(x)**2+1)

def main():
    z1 = float(input('z1='))
    z2 = float(input('z2='))
    n = float(input('n='))
    z=z1
    while z<=z2:
        s=k(z*z+1)-k(z*z-1)+2*k(z)
        print(s)
        z+=n

if __name__=='__main__':
    main()