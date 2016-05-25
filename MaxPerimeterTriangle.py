import sys

class Triangle(object):
    def __init__(self, sides):
        self.sides=sides
        self.triangle=self.constructTriangle()
    
    def constructTriangle(self):
        if len(self.sides)<3 or min(self.sides)<=0: return [0,0,0]
        max_triangle=[0,0,0]
        k=len(self.sides)-1
        while k>=2:
            j=k-1
            i=j-1
            if self.sides[i]+self.sides[j]<=self.sides[k]: k-=1
            else:
                max_triangle=[self.sides[i],self.sides[j],self.sides[k]]
                break
        return max_triangle
                    
    def notDegenerate(self, a, b, c):
        return a+b>c and a+c>b and b+c>a and max(a,b)-min(a,b)<c and max(a,c)-min(a,c)<b and max(b,c)-min(b,c)<a
    
    def isMaxTriangle(self, A, B):
        if max(A)>max(B): return True
        if min(A)>min(B): return True
        return False
    
    def printTriangle(self):
        if sum(self.triangle)==0: print -1
        else:
            for t in self.triangle:
                print t,

def main():
    sides=[34,1924,565,80,848,2913,819,732,431,32981,195,86340,688,563,7763,314,12608,401,4845,439,353,52,208,20372,626,805,19,984,939,53354]
    # read_input=[line.strip('\n').split(' ') for line in sys.stdin.readlines()]
    # sides=[int(d) for d in read_input[1]]
    t=Triangle(sorted(sides))
    t.printTriangle()
    
if __name__=='__main__':
    main()