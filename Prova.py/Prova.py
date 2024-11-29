print("Nathan Rosendo da Silva ; Gustavo Gomes 2B")
print()
print("Resposta Pergunta 1 : Pipeline é o processo de construção automatizado.")
print()
print("Resposta Pergunta 2 : Requisitos funcionais são as ações que o sistema tem que executar. O que ele precisa fazer para atender aos usuários Ex: permitir o login com usuário e senha.; Requisitos Não Funcionais dizem como o sistema deve funcionar em termos de desempenho, segurança e outros aspectos de qualidade. Ex: ser capaz de processar até 1000 transações por segundo.")
print()
print("Resposta Pergunta 3 : Requerimento; Projeto; Implementação; Verificação; Implantação.  ")
print()

class Moto:
    def __init__(self, modelo, ano):  
        self._modelo = modelo
        self._ano = ano

    def get_modelo(self):
        return self._modelo 
    
    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_ano(self):
        return self._ano 
    
    def set_ano(self, ano):
        if ano >= 2000:
            self._ano = ano
        else:
            print("Ano inválido. Digite um ano maior que 2000.")

modelo = input("Digite o modelo da Moto solicitada (Honda, Yamaha, BMW): ")
ano = int(input("Digite o ano da Moto solicitada: "))
print()
moto = Moto(modelo, ano)

print(f"Modelo da Moto: {moto.get_modelo()}")
print(f"Ano da Moto: {moto.get_ano()}")
print()



class Bicicleta:
    def __init__(self, modelo, tipo, ano):
        self._modelo = modelo
        self._tipo = tipo
        self._ano = ano

    def get_modelo(self):
        return self._modelo
    
    def set_modelo(self, modelo):
        self._modelo = modelo

    def get_tipo(self):
        return self._tipo
    
    def set_tipo(self, tipo):
        self._tipo = tipo

    def get_ano(self):
        return self._ano
    
    def set_ano(self, ano):
        if ano > 2000:
            self._ano = ano
        else:
            print("Ano inválido. Digite um ano maior que 2000.")

    def detalhes_bicicleta(self):
        return f"Modelo: {self._modelo}, Tipo: {self._tipo}, Ano: {self._ano}"

modelo_bicicleta = input("Digite o modelo da bicicleta (Caloi, Oggi, Scott): ")
tipo_bicicleta = input("Digite o tipo da bicicleta (Montanha, Speed, Urbana): ")
ano_bicicleta = int(input("Digite o ano da bicicleta: "))
print()
bicicleta = Bicicleta(modelo_bicicleta, tipo_bicicleta, ano_bicicleta)

print(f"Detalhes da bicicleta: {bicicleta.detalhes_bicicleta()}")