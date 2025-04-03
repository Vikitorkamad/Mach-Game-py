import tkinter as tk
from Logica_jogo import JogoMatematica

class TelaJogo:
    def __init__(self, master):
        self.master = master
        self.jogo = JogoMatematica()

        # Rótulo para a pergunta
        self.question_label = tk.Label(master, text="", font=("Arial", 36))
        self.question_label.pack(pady=20)

        # Rótulo para exibir a pontuação
        self.score_label = tk.Label(master, text="Pontuação: 0", font=("Arial", 24))
        self.score_label.pack(pady=20)

        # Botões para as operações
        self.button_add = tk.Button(master, text="1. +", command=lambda: self.verificar_resposta('+'), font=("Arial", 24))
        self.button_add.pack(side=tk.LEFT, padx=20)

        self.button_subtract = tk.Button(master, text="2. -", command=lambda: self.verificar_resposta('-'), font=("Arial", 24))
        self.button_subtract.pack(side=tk.LEFT, padx=20)

        self.button_multiply = tk.Button(master, text="3. *", command=lambda: self.verificar_resposta('*'), font=("Arial", 24))
        self.button_multiply.pack(side=tk.LEFT, padx=20)

        self.button_divide = tk.Button(master, text="4. /", command=lambda: self.verificar_resposta('/'), font=("Arial", 24))
        self.button_divide.pack(side=tk.LEFT, padx=20)

        self.gerar_pergunta()  # Gera a primeira pergunta

    def gerar_pergunta(self):
        pergunta = self.jogo.gerar_pergunta()
        self.question_label.config(text=pergunta)

    def verificar_resposta(self, operacao):
        correta = self.jogo.verificar_resposta(operacao)
        self.score_label.config(text=f"Pontuação: {self.jogo.score}")

        if correta:
            self.question_label.config(text=f"Correto! {self.jogo.num1} {self.jogo.operacao_correta} {self.jogo.num2} = {self.jogo.calcular_resposta()}")
        else:
            self.question_label.config(text=f"Errado! A operação correta era: {self.jogo.operacao_correta}")

        self.master.after(2000, self.gerar_pergunta)  # Gera uma nova pergunta após 2 segundos