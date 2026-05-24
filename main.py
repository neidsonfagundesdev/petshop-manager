# *************** Importa as funções de salvar cliente, buscar cliente pelo cpf 
# e listar clientes do arquivo database ***********************
from database import salvar_cliente, buscar_cliente_por_cpf, listar_clientes

# cria classe cliente
class Cliente:
    def __init__(self, nome, endereco, telefone, email, cpf):
        self.nome = nome
        self.endereco = endereco
        self.telefone = telefone
        self.email = email
        self.cpf = cpf
        self.animal = [] # lista para adicionar os pets

    def adicionar_animal(self, animal):
        return self.animal.append(animal)
        
    def listar_animais(self):
        return self.animal

    def salvar_no_banco(self):
        return salvar_cliente(self)

    @staticmethod

    def buscar_por_cpf(cpf):
        return buscar_cliente_por_cpf(cpf)

#cria classe animal
class Animal:
    def __init__(self, nome_animal, idade_animal, pelagem, porte, dono=None):
        self.nome_animal = nome_animal
        self.idade_animal = idade_animal
        self.pelagem = pelagem
        self.porte = porte
        self.dono = dono #referência ao cliente (dono) do pet

    def get_dono(self):
        return self.dono.nome if self.dono else "Sem dono"
        
#cria um cliente
cliente1 = Cliente("Michelle", "Avenida Santa Rita, caminho 55, casa 21", "(71 9 99946999)", "chellecressenti@gmail.com", "123.456.789-10")

