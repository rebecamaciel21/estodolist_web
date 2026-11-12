import mysql.connector
from mysql.connector import Error

def conectar():
    try:
        conexao = mysql.connector.connect(
        host="localhost",       #Endereço
        user="root",            #Usuário
        password="senai",       #Senha
        database="estodolist"   #Database criado
        )
        # Operador que vai manipular (conectar) os dois
        cursor = conexao.cursor(dictionary=True) #Devolve no formato Dict
        # Retorna duas informações: Conexão e Cursor
        return conexao, cursor
    
    except Error as erro:
        print(f"ERRO! Falha ao se conectar com o banco de dados: {erro}")
        return None, None
    
# ----- Função Inserir tarefa
def inserir_tarefa(nome_tarefa,descricao, categoria, data_prazo, prioridade):

    conexao, cursor = conectar() #Se conectar com BD

    #Verifica se a conexão funcionou
    if conexao is None:
        return False
    try:
        # %s SQL Parametrizando para evitar SQL Injection
        sql = "INSERT INTO tarefa (nomeTarefa, descricao, categoria, dataPrazo, prioridade) VALUES(%s, %s, %s, %s, %s)"
        # Executa o SQL Parametrizando e passa os parâmetros da função
        cursor.execute(sql,(nome_tarefa,descricao, categoria, data_prazo, prioridade))
        # Confirma as alterações
        conexao.commit()
        # Retornar TRUE para a função principal 
        return True

    except Error as erro:
        print(f"ERRO! Falha ao inserir a tarefa: {erro}")
        return False
    finally:
            cursor.close()
            conexao.close()
#-----------------------------------------------------------------------------------
#Retorna todas as tarefas cadastradas no Banco de Dados
def consultar_tarefas():
    #Chama a função conectar
    conexao, cursor = conectar()

    #Verifica se a função falhou
    if conexao is None:
        return[] #Lista vazia
     
    try: #tente executar o comando SQL
        #Selecione todas as colunas da(origem) tabela tarefa; (*)
        sql = """
               SELECT
               idTarefa AS idtarefa,
               dataPrazo AS data_prazo,
               nomeTarefa AS nome_tarefa,
               status,
               descricao,
               categoria,
               prioridade 
               FROM tarefa
              """
        # Executa o comando da variável SQL
        cursor.execute(sql)

        #Buscar todas as linhas da consulta executada
        tarefas = cursor.fetchall()

        #Retorna para a programação principal as tarefas
        return tarefas

    except Error as erro: #se der erro
        print(f"ERRO! Falha ao listar tarefas: {erro}")
        return[] #Retorna a lista vazia em caso de erro

    finally: #finalize sempre
        cursor.close() #Encerra o cursor
        conexao.close() #Encerra a conexão
#--------------------------------------------------------------------------------
#Essa função marca como concluída a tarefa indicada
def concluir_tarefa(idtarefa):

    conexao, cursor = conectar()
    if conexao is None:
        return False

    try: 
        sql = "UPDATE tarefa SET status = 'Concluída' WHERE idTarefa = %s"
        cursor.execute(sql,(idtarefa,))

        conexao.commit() #Confirma a alteração nos dados

        return True

    except Error as erro: #se der erro
        print(f"ERRO! Falha ao concluir a tarefa: {erro}")
        return[] #Retorna a lista vazia em caso de erro

    finally: #finalize sempre
            cursor.close() #Encerra o cursor
            conexao.close() #Encerra a conexão

#--------------------------------------------------------------------------------
#Essa função irá editar as informações da tarefa
def alterar_tarefa(idtarefa, nome_tarefa, descricao, categoria, data_prazo, prioridade):

    conexao, cursor = conectar()
    if conexao is None:
        return False

    try: 
        sql = """
        UPDATE tarefa 
        SET 
        nomeTarefa = %s, 
        descricao = %s, 
        categoria = %s, 
        dataPrazo = %s, 
        prioridade = %s 
        WHERE idTarefa = %s
        """
        cursor.execute(sql,(nome_tarefa, descricao, categoria, data_prazo, prioridade, idtarefa))
        

        conexao.commit() #Confirma a alteração nos dados

        return True

    except Error as erro: #se der erro
        print(f"ERRO! Falha ao editar a tarefa: {erro}")
        return[] #Retorna a lista vazia em caso de erro

    finally: #finalize sempre
            cursor.close() #Encerra o cursor
            conexao.close() #Encerra a conexão
#-------------------------------------------------------------------------------------------------
#APAGAR TAREFA
def apagar_tarefa(idtarefa):
    conexao, cursor = conectar()

    if conexao is None:
        return False

    try: 
        sql = "DELETE FROM tarefa WHERE idTarefa = %s"

        cursor.execute(sql, (idtarefa,))
        conexao.commit() #Confirma a exclusão nos dados

        return True
    
    except Error as erro: #se der erro
        print(f"ERRO! Falha ao excluir a tarefa: {erro}")
        return False #Retorna a lista vazia em caso de erro

    finally: #finalize sempre
        cursor.close() #Encerra o cursor
        conexao.close() #Encerra a conexão
