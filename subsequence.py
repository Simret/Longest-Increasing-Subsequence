def lengthofLIS(self, nums: list[int]) -> int:
        lst = [nums[0]]
        max_len = 1
        for num in nums[1:]:
            if num > lst[-1]:
                lst.append(num)
                max_len += 1
            else:
                left, right = 0, len(lst) - 1
                while left < right:
                    mid = (left + right) // 2
                    if lst[mid] < num:
                        left = mid + 1
                    else:
                        right = mid
                lst[left] = num
        return max_len
#                 ind = 0
#                 while ind < len(lst) and lst[ind] < num:
#                     ind += 1
#                 lst[ind] = num
        return max_len
    
    # def solve(grid, r = 0, c = 0):
    #     if r == 9:
    #         return True
    #     elif c == 9:
    #         return solve(grid, r + 1, 0)
    #     elif grid[r][c] != 0:
    #         return solve(grid, r, c+1)
    #     else:
    #         for k in range(1, 10):
    #             if is_valid(grid, r, c, k):
    #                 grid[r][c] = k
    #                 if solve(grid, r, c +1 ):
    #                     return True
    #                 grid[r][c] = 0
    #         return False

board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]    
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo[0])):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return (i,j) 
    return None  

def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False
    # Check column
    for i in range(len(bo)):
        
        if bo[i][pos[1]] == num and pos[0] != i:
            return False
    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
                return False
    return True


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1, 10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True
            bo[row][col] = 0
    return False




print_board(board)
solve(board)
print('_______________________')
print_board(board)