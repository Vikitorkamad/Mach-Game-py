import tkinter as tk
from tkinter import messagebox
from tela_jogo import TelaJogo
from tela_instrucoes import TelaInstrucoes
from utilitarios import resetTela
class TelaPrincipal:
    def __init__(self, master):
        self.master = master
        self.master.title("The Math Game")
        self.master.geometry("800x600")
        self.master.resizable(False, False)

        # Botões para abrir as telas
        self.button_jogar = tk.Button(master, text="Jogar", command=self.abrir_tela_jogo, font=("Arial", 24))
        self.button_jogar.pack(pady=20)
        
        self.button_instrucoes = tk.Button(master, text="Instruções", command=self.abrir_tela_instrucoes, font=("Arial", 24))
        self.button_instrucoes.pack(pady=20)

        self.button_sair = tk.Button(master, text="Sair", command=self.sair_jogo, font=("Arial", 24))
        self.button_sair.pack(pady=20)

    def abrir_tela_jogo(self):
        self.master.withdraw()  # Esconde a tela principal
        tela_jogo = TelaJogo(self.master)
        self.master.deiconify()  # Mostra a tela principal novamente

    def abrir_tela_instrucoes(self):
        self.master.withdraw()  # Esconde a tela principal
        tela_instrucoes = TelaInstrucoes(self.master)
        self.master.deiconify()  # Mostra a tela principal novamente

    def sair_jogo(self):
        if messagebox.askyesno("Confirmação", "Você realmente deseja sair do jogo?"):
            self.master.destroy()