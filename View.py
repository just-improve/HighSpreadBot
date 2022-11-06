import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class View(tk.Tk):

    PAD = 10

    def __init__(self, controller):
        super().__init__()
        self.controller = controller

    def main(self):
        self.mainloop()