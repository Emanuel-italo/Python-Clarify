class Carro:
    def __init__ (self, modelo, cor):
        self.modelo = modelo
        self.cor = cor
        self.velocidade = 0
    def acelerar(self, incremento):
        self.velocidade += incremento
        print(f"O carro {self.modelo} acelorou para {self.velocidade} Km/h")

    def desacelerar(self):
        while self.velocidade > 0:
            self.velocidade -= 5 
            print(f"O carro {self.modelo} desacelerou para {self.velocidade} Km/h")
        
        

    

    
meu_carro = Carro("Creta","Preto")
carro_instrutor = Carro("Suzuki jimney","Amarelo")
uber = Carro("Hb20","vermelho")

carro_instrutor.acelerar(20)
carro_instrutor.acelerar(32)
carro_instrutor.desacelerar()
