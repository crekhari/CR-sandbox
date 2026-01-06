board = [["1","2",".",".","3",".",".",".","."],
 ["4",".",".","5",".",".",".",".","."],
 [".","9","1",".",".",".",".",".","3"],
 ["5",".",".",".","6",".",".",".","4"],
 [".",".",".","8",".","3",".",".","5"],
 ["7",".",".",".","2",".",".",".","6"],
 [".",".",".",".",".",".","2",".","."],
 [".",".",".","4","1","9",".",".","8"],
 [".",".",".",".","8",".",".","7","9"]]
def validSudoku(board):
    for x in range(len(board)):
        row_set = set()
        col_set = set()
        for y in range(len(board[x])):
            old_len_row = len(row_set)
            old_len_col = len(col_set)
            row_set.add(board[x][y])
            if len(row_set) == old_len_row and board[x][y] != ".":
                return False
            col_set.add(board[y][x])
            if len(col_set) == old_len_col and board[y][x] != ".":
                return False
    from collections import defaultdict
    ddict = defaultdict(set)
    for x in range(len(board)):
        for y in range(len(board[x])):
            square_coord = tuple([int(x/3), int(y/3)])
            old_len_square = len(ddict[square_coord])
            ddict[square_coord].add(board[x][y])
            if len(ddict[square_coord]) == old_len_square and board[x][y] != ".":
                return False
    return True
print(validSodoku(board))