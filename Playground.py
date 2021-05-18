import tkinter as tk
from tkinter import Canvas
from PIL import ImageTk, Image

class Playground:

    def __init__(self, master) -> None:

        self.img = ImageTk.PhotoImage(Image.open("1.jpeg"))
        button = tk.Button(master, image=self.img, bg='#1f1f1f')
        button.pack()

        