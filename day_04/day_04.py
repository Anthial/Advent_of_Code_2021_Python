import numpy as np

#I have decided to actually put some effort into making this look nicer than day_03, because damn that was ugly

def process_input():
    """Process the input data and turn it into list and np arrays"""
    boards = []
    marked_boards = []
    order = []
    with open('input.txt', 'r') as f:
        order = [int(i) for i in f.readline().split('\n')[0].split(',')]
        f.readline() #get rit of whitespace line
        board = []
        marked_board = []
        for line in f:
            if line.startswith("\n"):
                boards.append(np.array(board))
                marked_boards.append(np.array(marked_board, dtype=bool))
                board = []
                marked_board = []
            else:
                board.append([int(i) for i in line.split()])
                marked_board.append([0]*5)
        return order, boards, marked_boards

def check_board_for_bingo(marked_board):
    for i in range(5):
        if np.all(True == marked_board[:, i]) or np.all(True == marked_board[i, :]):
            return True
    return False

def mark_marked_board(t_order, board, marked_board):
    """Set the mask for the board"""
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if column == t_order:
                marked_board[i][j] = True
                if check_board_for_bingo(marked_board):
                    return column
    return False

def do_bingo():
    order, boards, marked_boards = process_input()
    for t_order in order:
        for i, board in enumerate(boards):
            value = mark_marked_board(t_order, board, marked_boards[i])
            if value:
                return value*np.sum(np.ma.masked_array(board, marked_boards[i]))

def let_the_squid_win():
    order, boards, marked_boards = process_input()
    for t_order in order:
        new_boards = []
        new_marked_boards = []
        for i, board in enumerate(boards):
            value = mark_marked_board(t_order, board, marked_boards[i])
            if value and len(boards) == 1:
                return value*np.sum(np.ma.masked_array(board, marked_boards[i]))
            elif not value:
                new_boards.append(board)
                new_marked_boards.append(marked_boards[i])
        boards = np.array(new_boards)
        marked_boards = np.array(new_marked_boards)

if __name__ == "__main__":
    print(do_bingo())
    print(let_the_squid_win())
    
