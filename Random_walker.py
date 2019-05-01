import random
import numpy as np
n = int(input("원하는 배열크기를 입력하세요 : n"))
list1 = np.full((n,n),'0')
list2 = [] # T가 들어간 곳
list3 = [] # i,j를 중점으로 5by5구역
addRow = [-1,1,0,0]
addCol = [0,0,1,-1]
count=0

def namu(i,j):
    if i>0 and j>0 and i<n-1 and j<n-1:
        for a in range(-1,2,1):
            for b in range(-1,2,1):
                list1[i+a][j+b] = 'T'
                
        for c in range(-1,2,1):
            for d in range(-1,2,1):
                list2.append((i+c,j+d))

        for e in range(-2,3,1):
            for f in range(-2,3,1):
                list3.append((i+e,j+f))
    
        
    
                
def pick():
    global count
    while True:
        
        if count==4:
            break
        i = random.randint(1,n-2)
        j = random.randint(1,n-2)
        if (i,j) in list3:
            continue
        if (i,j) not in list3:
            count+=1
            namu(i,j)
            
    return list1
    
def random_walker():
    while True:
        
        z = random.randint(0,n-1)
        v = random.randint(0,n-1)
        if (z,v) not in list2:
            list1[z][v] = 'X'
            print(list1)
            break
        if (z,v) in list2:
            continue
           
    while True:
        
        L = input("p를 누르세요")
        if L == 'p':
            
            while True:
                x = random.randint(-1,1)
                y = random.randint(-1,1)
                if(x,y) ==(0,0) or (x,y) ==(1,1) or (x,y) == (-1,-1) or (x,y) == (1,-1) or (x,y) ==(-1,1):
                    continue
                if (z+x,v+y) in list2:
                    continue

                if (z+x,v+y) not in list2:
                    if (z,v) not in list2:
                        if ((z+x>-1 and z+x<n and v+y>-1 and v+y<n))and((z>-1 and z<n and v>-1 and v<n)):
                            list1[z][v] = '0'
                            list1[z+x][v+y] = 'X'
                            z = z+x
                            v = v+x
                            print(list1)
                            break
        if L == 'q':
            break

        
        
    
pick()
random_walker()
    




# if (i,j) not in list3:
        
