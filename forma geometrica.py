#Como calcular area do quadrado com função area e funcao perimetro:

class FormaGeometrica():
  def __init__(self, lado):
      self.__lado = lado

  @property
  def area(self):
    pass

  @property
  def perimetro(self):
     pass
  
  @property
  def lado(self):
     return self.__lado
'''
class Quadrado:
  def __init__(self, lado):
    self._lado = lado

  @property
  def lado(self):
    return self._lado
  
  def area(self):
    return self._lado ** 2

  def perimetro(self):
    return 4 * self._lado

lado = int(input("Digite o lado do quadrado: "))

quadrado = Quadrado(lado)

print("A área do quadrado é:", quadrado.area())
print("O perímetro do quadrado é:", quadrado.perimetro())
'''
#Calcular area do retangulo com função area e funcao perimetro em python
'''
class retangulo:
  def __init__(self, lado1, lado2):
    self.lado1 = lado1
    self.lado2 = lado2

  @property
  def area(self):
    return self.lado1 * self.lado2

  @property
  def perimetro(self):
    return 2 * self.lado1 + 2 * self.lado2

lado1 = int(input("Digite o lado 1 do retangulo: "))
lado2 = int(input("Digite o lado 2 do retangulo: "))

ret = retangulo(lado1,lado2)

if lado1 == lado2:
    print('Os Lados são iguais. Isso é um quadrado.')
else:
  
    print("A área do retangulo é:", ret.area)
    print("O perímetro do retangulo é:", ret.perimetro)
'''

#Calcular area do circulo com função area e funcao diametro em python:
'''
from math import pi

class Circulo():
    def __init__(self, raio):
        self.__raio = raio
    
    @property
    def raio(self):
        return self.__raio
    
    @property
    def perimetro(self):
        return 2 * pi * self.__raio
    
    @property
    def diametro(self):
        return self.__raio * 2
    
    @property
    def area(self):
        return pi * self.__raio * self.__raio
    
    raio = float(input('Digite o raio do circulo: '))
c = Circulo(raio)
print(c.diametro) '''

# base , altura , lado.a , lado.b , lado.c , angulo ab , angulo ac , angulo bc
# class Triangulo:
#     def __init__(self,):
        
class Triangulo(FormaGeometrica):
    def __init__(self, base, altura, lado_a=4, lado_b=6, lado_c=9, angulo_ab=20, angulo_ac=50, angulo_bc=70):
        super().__init__(base)
        self.__altura = altura
        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c
        self.angulo_ab = angulo_ab
        self.angulo_ac = angulo_ac
        self.angulo_bc = angulo_bc

    @property
    def area(self):
        return self.altura * self.base / 2

    @property
    def altura(self):
        return self.__altura 

    @property
    def base(self):
        return super().lado

    @property
    def perimetro(self):
        return (self.base * 2 ) + (self.altura * 2 ) / 2 

t = Triangulo(10,8)
print('area: ',t.area)
print('perimetro:',t.perimetro)
