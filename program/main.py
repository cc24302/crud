import pyodbc
import os

global connection

def connect() -> bool:

    try:
    
        connection = pyodbc.connect(
            driver = "{SQL Server}",
            server = "regulus.cotuca.unicamp.br",
            database = "BD24302",
            uid = "BD24302",
            pwd = "BD24302"
        )
        return True
    except:
        return False
    
def insert() -> bool:
   # cursor é um objeto que permite que
   # nosso programa execute comandos SQL
   # no nosso servidor
    cursor = connection.cursor()
    codigoProduto = int(input("Digite o código do produto: "))
    nome = input(" Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))

    # Criou uma string com o comando INSERT novos dados no Banco de Dados
    command = "INSERT INTO  pratica.Produto(codigoProduto, nome, preco, inativo)" + \
              "VALUES" + f"({codigoProduto}, '{nome}', {preco}, 0)"


    try:
        # Tenta executar o comando no Banco de Dados
        # Se funcionar retorna "True"
        cursor.execute(command)
        cursor.commit()
        # Aplica as alterações no Banco de Dados
        return True
    except:
        # Se errar retorna "False"
        return False
    
def update() -> bool:
   
   pass

def delete() -> bool:
    
    pass

def select() -> bool:
    
    pass

def main():
    # Abriu a conecção com o Banco de Dados
    if connect():
        
        option = -1
        while option != 0:
            print("0 - Ecerrar programa")
            print("1 - Cadastrar novo produto")
            print("2 - Alterar um produto")
            print("3 - Excluir um produto")
            print("4 - Listar os produtos")

            option = int(input("\nDigite a opção desejada: "))

            if option == 1:
                insert()
            elif option == 2:
                update()
            elif option == 3:
                delete()
            elif option == 4:
                select()
        # Fecha a conecção com o Banco de Dados
        # NÃO ESQUECER DE FAZER ISSO
        connection.close()