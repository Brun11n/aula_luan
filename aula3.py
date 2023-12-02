class Carro:
    cor = "preto"
    marca = "konigsegg"
    modelo = "Agera_R"

    def ligar_motor(self):
        print("Vromm Vromm")

carro1 = Carro()
print(carro1.marca)
print(carro1.cor)
carro1.ligar_motor()
print("\n")

print("Agora será um novo carro\n")
novo_carro = Carro()

novo_carro.cor = "carbono"
print(novo_carro.cor)

novo_carro.marca = "pagani"
print(novo_carro.marca)

novo_carro.modelo = "huayra"
print(novo_carro.modelo)
carro1.ligar_motor()