class Pessoa:
    def __init__(self, nome, idade, endereço, cpf, sexo):

        self.__nome = nome
        self.__idade = idade
        self.__endereço = endereço
        self.__cpf = cpf
        self.__sexo = sexo

    @property
    def nome(self):
        return self.__nome
    @property
    def idade(self):
        return self.__idade
    @property
    def endereço(self):
        return self.__endereço
    @property
    def cpf(self):
        return self.__cpf
    @property
    def sexo(self):
        return self.__sexo


class Pai(Pessoa):
   
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

p = Pai('Lealdino', 45 , 'Rua j 68 Qd.13 lt.6 Cidade Aparecida de Goiania', '745.785.705-45', 'masculino')
print(p.nome)

class Mae(Pessoa):
   
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

m = Mae('Darliane', 38 , 'Rua 8 Qd.13 lt.8 Cidade Aparecida de Goiânia', '759.430.950-27', 'feminino')
print(m.nome)
       
class Filho(Pessoa):
   
    def __init__(self, nome, idade, endereço, cpf, sexo):
        super().__init__(nome, idade, endereço, cpf, sexo)

f = Filho('Bruno', 17, 'Rua 52 Qd.3 lt.1 Cidade Aparecida de Goiânia. ', '433.738.715-15', 'masculino')
print(f.nome)