#!/usr/bin/env python
# coding: utf-8

# In[1]:


class aha:
    def __init__(self, N):
        self.n = N
        
    # Find the unassigned cell with Minimum Remaining Values (MRV) heuristic
    def find_unassigned_cell(self, grid):
        min_remaining = float('inf')
        cell = None
        for i in range(self.n):
            for j in range(self.n):
                if grid[i][j] == 0:
                    remaining = self.count_remaining_values(grid, i, j)
                    if remaining < min_remaining:
                        min_remaining = remaining
                        cell = (i, j)
        return cell

    # Count the number of remaining valid values for a given cell (i, j)
    def count_remaining_values(self, grid, i, j):
        values = set(range(1, self.n + 1))
        for x in range(self.n):
            values.discard(grid[i][x])
            values.discard(grid[x][j])

        if self.n == 9:
            startRow = i - i % 3
            startCol = j - j % 3
            for a in range(3):
                for b in range(3):
                    values.discard(grid[a + startRow][b + startCol])

        elif self.n == 4:
            startRow = i - i % 2
            startCol = j - j % 2
            for a in range(2):
                for b in range(2):
                    values.discard(grid[a + startRow][b + startCol])

        elif self.n == 16:
            startRow = i - i % 4
            startCol = j - j % 4
            for a in range(4):
                for b in range(4):
                    values.discard(grid[a + startRow][b + startCol])

        return len(values)

    # Checks whether it will be legal to assign num to the given row, col
    def is_safe(self, grid, row, col, num):
        for x in range(self.n):
            if grid[row][x] == num:
                return False

        for x in range(self.n):
            if grid[x][col] == num:
                return False

        if self.n == 9:
            startRow = row - row % 3
            startCol = col - col % 3
            for i in range(3):
                for j in range(3):
                    if grid[i + startRow][j + startCol] == num:
                        return False

        elif self.n == 16:
            startRow = row - row % 4
            startCol = col - col % 4
            for i in range(4):
                for j in range(4):
                    if grid[i + startRow][j + startCol] == num:
                        return False

        elif self.n == 4:
            startRow = row - row % 2
            startCol = col - col % 2
            for i in range(2):
                for j in range(2):
                    if grid[i + startRow][j + startCol] == num:
                        return False

        return True

    # Main function to solve Sudoku using constraint propagation and backtracking
    def solve_sudoku(self, grid):
        # Find the unassigned cell with MRV heuristic
        cell = self.find_unassigned_cell(grid)
        if not cell:
            return True

        row, col = cell

        for num in range(1, self.n + 1):
            if self.is_safe(grid, row, col, num):
                grid[row][col] = num
                if self.solve_sudoku(grid):
                    return True
                grid[row][col] = 0  # If the current num doesn't lead to a solution, reset the cell and backtrack

        return False

