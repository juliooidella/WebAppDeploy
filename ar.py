class ControleArCondicionado:
    def __init__(self, cor, largura, altura, peso, marca, modelo, tipo_de_pilha):
        self.cor = cor
        self.largura = largura
        self.altura = altura
        self.peso = peso
        self.marca = marca
        self.modelo = modelo
        self.tipo_de_pilha = tipo_de_pilha
        self.ligado = False
        self.temperatura = 20

    def liga_desliga(self):
        self.ligado = not self.ligado

        if self.ligado:
            return "Ar condicionado ligado"
        else:
            return "Ar condicionado desligado"

    def aumenta_temperatura(self):
        if self.ligado:
            self.temperatura += 1
            print(f"Temperatura aumentada para {self.temperatura}")
        else:
            print("Ar condicionado desligado")

    def diminui_temperatura(self):
        if self.ligado:
            self.temperatura -= 1
            print(f"Temperatura diminuida para {self.temperatura}")
        else:
            print("Ar condicionado desligado")


# Estanciando a classe do Objeto
controle = ControleArCondicionado("branco", 20, 20, 10, "LG", "ABC", "AAA")

# Executando uma das funções dele
print(controle.liga_desliga())


# Criando uma rotina de repetição com entrada do usuário
print("Digite 1 para Ligar ou Desligar o Ar Condicionado")
print("Digite 2 para aumentar a temperatura")
print("Digite 3 para diminuir a temperatura")

while True:
    comando = input()

    if comando == "sair":
        break
    if comando == "1":
        print(controle.liga_desliga())
    elif comando == "2":
        controle.aumenta_temperatura()
    elif comando == "3":
        controle.diminui_temperatura()
    else:
        print("Comando inválido")
