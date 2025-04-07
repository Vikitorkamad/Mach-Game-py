import tkinter as tk
from tela_principal import TelaPrincipal
from utilitarios import resetTela
def main():
    root = tk.Tk()
    TelaPrincipal(root)
    root.mainloop()
    root.resetTela()

if __name__ == "__main__":
    main()