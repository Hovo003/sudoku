#!/usr/bin/env python
# coding: utf-8

# In[3]:


import tkinter as tk
from tkinter import messagebox
from tkinter.font import Font
import random
import math

from aha_algorithm import *
from backtracking_algorithm import *

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.grid_size = 9
        self.root.configure(bg="light blue")
        
        self.generate_button()
        
        self.selected_size = tk.StringVar(value=self.grid_size)
        self.create_size_buttons()
        
        self.selected_algorithm = tk.StringVar(value='Backtracking Algorithm')
        self.create_algorithm_buttons()
        
        self.root.geometry("%dx%d" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

        self.font = Font(size=10)
        self.cells = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]

        self.create_buttons()
        self.create_grid()
        
        self.initialize_puzzle()

        self.root.configure(bg="white")
        self.root.grid_columnconfigure(0, weight=1)
        
    def generate_button(self):
        generate_frame = tk.Frame(self.root, bg="light blue", padx=10, pady=10)
        generate_frame.grid(row=2, column=0, columnspan=self.grid_size, sticky="nsew")

        generate_label = tk.Label(generate_frame, text="Generate a puzzle:", bg="light blue")
        generate_label.grid(row=0, column=0, padx=5, pady=5)

        generate_button = tk.Radiobutton(generate_frame, text='Generate a puzzle', variable = 'generate',
                                           value='generate', bg="light blue", indicatoron=0, command=self.initialize_puzzle)
        generate_button.grid(row=0, column=1, padx=5, pady=5)
            
    def create_algorithm_buttons(self):
        algorithm_frame = tk.Frame(self.root, bg="light blue", padx=10, pady=10)
        algorithm_frame.grid(row=3, column=0, columnspan=self.grid_size, sticky="nsew")

        algorithm_label = tk.Label(algorithm_frame, text="Select Algorithms:", bg="light blue")
        algorithm_label.grid(row=0, column=0, padx=5, pady=5)

        algorithms = ["Backtracking Algorithm", "AHA"]
        for i, algorithm in enumerate(algorithms):
            algorithm_button = tk.Radiobutton(algorithm_frame, text=algorithm, variable=self.selected_algorithm,
                                               value=algorithm, bg="light blue", indicatoron=0, command=lambda s=algorithm: self.solve_puzzle(s))
            algorithm_button.grid(row=0, column=i+1, padx=5, pady=5)

    def create_buttons(self):
        button_frame = tk.Frame(self.root, bg="white", padx=5, pady=5)
        button_frame.grid(row=0, column=0, columnspan=self.grid_size, sticky="nsew")
            
    def create_size_buttons(self):
            
        size_frame = tk.Frame(self.root, bg="light blue", padx=10, pady=10)
        size_frame.grid(row=1, column=0, columnspan=self.grid_size, sticky="nsew")

        size_label = tk.Label(size_frame, text="Select Size:", bg="light blue")
        size_label.grid(row=0, column=0, padx=5, pady=5)

        sizes = [4, 9, 16]
        for i, size in enumerate(sizes):
            size_button = tk.Radiobutton(size_frame, text=f'{size}x{size}', variable=self.selected_size,
                                               value=size, bg="light blue", indicatoron=0, command=lambda s=size: self.change_size(s))
            size_button.grid(row=0, column=i+1, padx=5, pady=5)

    def create_grid(self):
        grid_frame = tk.Frame(self.root, bg="white")
        grid_frame.grid(row=4, column=0, sticky="nsew", columnspan=self.grid_size)

        for i in range(self.grid_size):
            for j in range(self.grid_size):
                cell = tk.Entry(grid_frame, font=self.font, width=3, justify="center")
                cell.grid(row=i, column=j, padx=2, pady=2, ipadx=5, ipady=5)
                self.cells[i][j] = cell

    def initialize_puzzle(self):
        if initial_states_dict.get(self.grid_size):
            initial_states_list = initial_states_dict[self.grid_size]
            initial_state = random.choice(initial_states_list)
            for i in range(self.grid_size):
                for j in range(self.grid_size):
                    value = initial_state[i][j]
                    if value != 0:
                        self.cells[i][j].delete(0, tk.END)
                        self.cells[i][j].insert(0, str(value))
                    else:
                        self.cells[i][j].delete(0, tk.END)

    def change_size(self, new_size):
        self.grid_size = new_size

        for row in self.cells:
            for cell in row:
                cell.grid_forget()

        self.cells = [[None for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        self.create_grid()

        self.root.geometry("%dx%d" % (self.root.winfo_screenwidth(), self.root.winfo_screenheight()))

    def solve_puzzle(self, x):
        board = [[0 for _ in range(self.grid_size)] for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                value = self.cells[i][j].get()
                if value.isdigit() and 1 <= int(value) <= self.grid_size:
                    board[i][j] = int(value)
                else:
                    board[i][j] = 0
                
        if x == 'AHA':
            solver = aha(self.grid_size)
            if solver.solve_sudoku(board):
                for i in range(self.grid_size):
                    for j in range(self.grid_size):
                        self.cells[i][j].delete(0, tk.END)
                        self.cells[i][j].insert(0, str(board[i][j]))
            else:
                messagebox.showinfo("Sudoku Solver", "No solution found!")
            
        elif x =='Backtracking Algorithm':
            solver = backtracking_algorithm()
            if solver.solve_sudoku(board):
                for i in range(self.grid_size):
                    for j in range(self.grid_size):
                        self.cells[i][j].delete(0, tk.END)
                        self.cells[i][j].insert(0, str(board[i][j]))
            else:
                messagebox.showinfo("Sudoku Solver", "No solution found!")


if __name__ == "__main__":
    initial_states_dict = {
        4: [
            [
                [0, 0, 0, 4],
                [2, 0, 1, 0],
                [3, 0, 0, 2],
                [0, 0, 0, 0],
            ]
        ],
        9: [
            [
                [0, 0, 5, 0, 0, 0, 0, 0, 0],
                [1, 6, 0, 0, 2, 0, 0, 4, 0],           
                [3, 7, 0, 0, 0, 0, 0, 0, 0], 
                [0, 0, 0, 2, 5, 0, 1, 0, 0],  
                [0, 9, 0, 0, 0, 0, 0, 0, 0],               
                [0, 4, 0, 7, 0, 0, 6, 0, 3],            
                [0, 0, 0, 0, 0, 8, 2, 0, 0],                
                [0, 0, 4, 0, 1, 0, 0, 0, 9],               
                [0, 8, 2, 9, 0, 0, 0, 0, 6],
                ],
            ],
        16: [
            [
                [0, 6, 0, 0, 0, 0, 0, 8, 11, 0, 0, 15, 14, 0, 0, 16],
                [15, 11, 0, 0, 0, 16, 14, 0, 0, 0, 12, 0, 0, 6, 0, 0],
                [13, 0, 9, 12, 0, 0, 0, 0, 3, 16, 14, 0, 15, 11, 10, 0],
                [2, 0, 16, 0, 11, 0, 15, 10, 1, 0, 0, 0, 0, 0, 0, 0],
                [0, 15, 11, 10, 0, 0, 16, 2, 13, 8, 9, 12, 0, 0, 0, 0],
                [12, 13, 0, 0, 4, 1, 5, 6, 2, 3, 0, 0, 0, 0, 11, 10],
                [5, 0, 6, 1, 12, 0, 9, 0, 15, 11, 10, 7, 16, 0, 0, 3],
                [0, 2, 0, 0, 0, 10, 0, 11, 6, 0, 5, 0, 0, 13, 0, 9],
                [10, 7, 15, 11, 16, 0, 0, 0, 12, 13, 0, 0, 0, 0, 0, 6],
                [9, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 16, 10, 0, 0, 11],
                [1, 0, 4, 5, 9, 13, 0, 0, 7, 0, 11, 0, 3, 16, 0, 0],
                [16, 14, 0, 0, 7, 0, 10, 15, 4, 6, 1, 0, 0, 0, 13, 8],
                [11, 10, 0, 15, 0, 0, 0, 16, 9, 12, 13, 0, 0, 1, 5, 4],
                [0, 0, 12, 0, 1, 4, 6, 0, 16, 0, 0, 0, 11, 10, 0, 0],
                [0, 0, 5, 0, 8, 12, 13, 0, 10, 0, 0, 11, 2, 0, 0, 14],
                [3, 16, 0, 0, 10, 0, 0, 7, 0, 0, 6, 0, 0, 0, 12, 0],
            ],
        ]
    }
    
    root = tk.Tk()
    SudokuGUI(root)
    root.mainloop()

