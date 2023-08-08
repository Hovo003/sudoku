#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class backtracking_algorithm:
    
    def __init__(self):
        pass
    
    def is_valid(self, board, row, col, num):

        for i in range(len(board)):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Check subgrid
        subgrid_size = int(len(board) ** 0.5)
        start_row, start_col = subgrid_size * (row // subgrid_size), subgrid_size * (col // subgrid_size)
        for i in range(subgrid_size):
            for j in range(subgrid_size):
                if board[start_row + i][start_col + j] == num:
                    return False

        return True

    def solve_sudoku(self, board):
        empty_cell = self.find_empty_cell(board)
        if not empty_cell:
            return True  # Puzzle solved
        else:
            row, col = empty_cell

        for num in range(1, len(board) + 1):
            if self.is_valid(board, row, col, num):
                board[row][col] = num

                if self.solve_sudoku(board):
                    return True

                board[row][col] = 0

        return False

    def find_empty_cell(self, board):
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == 0:
                    return (i, j)
        return None

