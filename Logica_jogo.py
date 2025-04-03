import random

class JogoMatematica:
    def __init__(self):
        self.score = 0
        self.num1 = 0
        self.num2 = 0
        self.operacao_correta = ""

    def gerar_pergunta(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operacao_correta = random.choice(['+', '-', '*', '/'])
        resultado = self.calcular_resposta()
        return f"{self.num1} ? {self.num2} = {resultado}"

    def calcular_resposta(self):
        if self.operacao_correta == '+':
            return self.num1 + self.num2
        elif self.operacao_correta == '-':
            return self.num1 - self.num2
        elif self.operacao_correta == '*':
            return self.num1 * self.num2
        elif self.operacao_correta == '/':
            return self.num1 / self.num2 if self.num2 != 0 else None

    def verificar_resposta(self, operacao):
        if operacao == self.operacao_correta:
            self.score += 1
            return True
        else:
            self.score -= 1
            return False