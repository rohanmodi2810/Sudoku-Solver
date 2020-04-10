board = [
    [0,7,0,4,0,0,3,0,0],
    [0,4,9,0,7,3,0,0,0],
    [8,0,0,0,0,0,0,4,2],
    [1,0,0,0,0,8,0,0,0],
    [5,0,0,6,1,0,0,0,7],
    [0,0,0,0,0,4,0,0,6],
    [9,2,0,0,0,0,0,0,8],
    [0,0,0,2,9,0,5,1,0],
    [0,0,7,0,0,1,0,3,0]
]

def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):
        if valid(bo, i, (row,col)):
            bo[row][col] = i

            if solve(bo):
                return True
            
            bo[row][col] = 0

    return False



def valid(bo, num, pos):
    #check row
    for j in range(9):
        if bo[pos[0]][j] == num and pos[1] != j:
            return False

    #check column
    for i in range(9):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    #check box
    J = pos[1]//3
    I = pos[0]//3
    for i in range(3):
        for j in range(3):
            if bo[I*3+i][J*3+j] == num and (I*3+i,J*3+j) != pos:
                return False

    return True

def print_board():
    for i in range(9):
        if i%3==0 and  i!=0:
            print("-------------------------------")

        for j in range(9):
            if j%3==0 and j!=0:
                print("|  ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + "  ", end="") 


def find_empty(bo):
    for i in range(9):
        for j in range(9):
            if bo[i][j] == 0:
                return (i,j)

    return None

print_board()
print()
solve(board)
print()
print_board()
print()