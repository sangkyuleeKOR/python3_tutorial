import random
import numpy as np
n = int(input("원하는 배열크기를 입력하세요 : n"))

list1 = np.full((n,n),'O')
list2 = [] # T가 들어간 곳 리스트
list3 = [] # i,j를 중점으로 5by5구역 리스트
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
        
        x = random.randint(0,n-1)
        y = random.randint(0,n-1)
        if (x,y) not in list2:
            list1[x][y] = 'X'
            print(list1)
            break
        if (x,y) in list2:
            continue
           
    while True:
        L = input("아무키나 누르세요")
        if L == 'q':
            break
        while True:
            c = random.randint(0,3)
            new_x = x + addRow[c]
            new_y = y + addCol[c]
            if (new_x,new_y) not in list2 and new_x>-1 and new_y >-1 and new_x<n and new_y<n:
                break
            if (new_x,new_y) in list2:
                continue
        list1[x][y],list1[new_x][new_y] = 'O','X'
        x,y = new_x,new_y
        print(list1)
    

          
                
        
        

        
        
    

pick()
random_walker()