import tkinter as tk

def resetTela(root):
    for widget in root.winfo_children():
        widget.destroy()  # Remove todos os widgets da tela atual