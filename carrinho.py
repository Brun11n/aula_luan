class Carro:
    def __init__(self):
        self.motor_ligado = False
        self.andando = False

    def ligar_motor(self):
        if not self.motor_ligado:
            self.motor_ligado = True
            print("Motor ligado")
        else:
            print("Motor já ta ligado")

    def desligar_motor(self):
        if self.motor_ligado:
            self.motor_ligado = False
            print("Motor desligado.")
        else:
            print("Motor já ta desligado")

    def andar(self):
        if self.motor_ligado and not self.andando:
            self.andando = True
            print("Carro andando.")
        else:
            print("Carro já ta andando ")

    def parar(self):
        if self.andando:
            self.andando = False
            print("Carro parado.")
        else:
            print("Carro já ta parado")

    def status(self):
        if self.andando:
            print("Carro andando")
        else:
            print("Carro parado")
            
            
carro = Carro()
carro.ligar_motor()
carro.andar()
carro.parar()
carro.desligar_motor()
carro.status()