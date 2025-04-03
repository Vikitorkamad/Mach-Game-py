import tkinter as tk

class TelaInstrucoes:
    def __init__(self, master):
        self.master = master
        self.master.title("Instruções")
        self.master.geometry("800x600")

        self.instructions_label = tk.Label(master, text="Instruções:\n"
                                "1. Escolha a operação correta para os números apresentados.\n"
                                "2. Clique no botão correspondente à operação.\n"
                                "3. Cada resposta correta aumenta sua pontuação.\n"
                                "4. Respostas incorretas diminuem sua pontuação.\n"
                                "5. Divirta-se!", font=("Arial", 16), justify="left")
        self.instructions_label.pack(pady=20)

        self.button_voltar = tk.Button(master, text="Voltar", command=self.voltar, font=("Arial", 24))
        self.button_voltar.pack(pady=20)

    def voltar(self):
        self.master.destroy()  # Fecha a tela de instruções
        from tela_principal import TelaPrincipal
        root = tk.Tk()
        TelaPrincipal(root)
        root.mainloop()