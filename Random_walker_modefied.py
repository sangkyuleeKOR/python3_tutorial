import numpy as np
import random



def plant_trees(size_x,size_y,num_tree):
    trees = []
    none_plant_area = []
    num_tree_count = 0
    while num_tree_count != num_tree:
        while True:
            x,y = random.randint(1,size_x-2),random.randint(1,size_y-2)
            if (x,y) not in none_plant_area:
                trees.extend([(dx,dy) for dx in range(x-1,x+2,1) for dy in range(y-1,y+2,1)])
                none_plant_area.extend([(dx,dy) for dx in range(x-2,x+2,1) for dy in range(y-2,y+2,1)])
                num_tree_count+=1
                break

    init_map = np.full(size_x*size_y,'O').reshape(size_x,size_y)
    for (x,y) in trees:
        init_map[x][y] = 'T'

    return init_map, trees

def run():
    while True:
        try:
            size_x = int(input("가로를 입력하세요"))
            size_y = int(input("세로를 입력하세요"))
            num_tree = int(input("나무 개수를 입력하세요"))
            break
        except:
            print("다시 입력하세요")
            
    init_map, trees = plant_trees(size_x,size_y,num_tree)
    movable_person_xy = list({(x,y) for x in range(0,size_x-1) for y in range(0,size_y-1)} - set(trees)) # 리스트끼리 빼주려면 셋형으로 바꾸어준다음 뺀다 그다음 리스트로 다시 반환.
    addRow = [-1,1,0,0]
    addCol = [0,0,1,-1]
    x,y = random.choice(movable_person_xy)
    init_map[x][y] = 'X'
    while True:
        
        print(init_map)
        d = input("아무키나 입력하세요 q를 입력하면 종료합니다.")
        if d == 'q':
            break
        while True:
            c = random.randint(0,3)
            dx = x+addRow[c]
            dy = y+addCol[c]
            if (dx,dy) in movable_person_xy:
                break
        init_map[dx][dy] = 'X'
        init_map[x][y] = 'O'
        x,y = dx,dy
                
if __name__ == "__main__":
    run()



    
        







    


'''
def main():
    size_x = int(input("가로길이를 입력하세요"))
    size_y = int(input("세로길이를 입력하세요"))
'''   
