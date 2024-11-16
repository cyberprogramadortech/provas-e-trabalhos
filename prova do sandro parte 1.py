import mysql.connector # type: ignore
from websocket_server import WebsocketServer # type: ignore

# Função para conectar ao banco de dados MySQL
def conectar_banco():
    conn = mysql.connector.connect(
        host="localhost",  
        user="root",       
        password="",       
        database="db_python"  
    )
    return conn

# Função para verificar e criar o banco de dados e a tabela, caso não existam
def configurar_banco():
    # Conectar ao MySQL sem especificar a base de dados
    conn = mysql.connector.connect(
        host="localhost",  
        user="root",       
        password=""       
    )
    cursor = conn.cursor()
    
    # Verifica se o banco de dados db_python existe
    cursor.execute("SHOW DATABASES LIKE 'db_python'")
    resultado = cursor.fetchone()
    
    if not resultado:
        print("Banco de dados 'db_python' não encontrado. Criando...")
        cursor.execute("CREATE DATABASE db_python")
    
    # Conecta novamente agora especificando o banco de dados
    conn.database = 'db_python'

    # Cria a tabela perfis caso não exista
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfis (
        id INT PRIMARY KEY,
        idPerfil INT,
        nomePerfil VARCHAR(255),
        numSeguidores INT,
        numPosts INT,
        numSeguindo INT
    )
    """)
    
    conn.commit()
    cursor.close()
    conn.close()

# Função que será chamada sempre que uma mensagem for recebida do cliente
def tratar_mensagem(cliente, servidor, mensagem):
    try:
        # Espera-se que a mensagem seja uma string com os dados separados por vírgulas
        dados = mensagem.split(',')
        
        if len(dados) == 6:
            # Extrai os dados da mensagem
            id, idPerfil, nome, numSeg, numPost, numSeguindo = dados
            
            # Conectar ao banco de dados
            conn = conectar_banco()
            cursor = conn.cursor()
            
            # Insere os dados no banco de dados
            cursor.execute(
                "INSERT INTO perfis (id, idPerfil, nomePerfil, numSeguidores, numPosts, numSeguindo) "
                "VALUES (%s, %s, %s, %s, %s, %s)", 
                (id, idPerfil, nome, numSeg, numPost, numSeguindo)
            )
            conn.commit()
            
            # Envia uma resposta de sucesso para o cliente
            servidor.send_message(cliente, "Dados inseridos com sucesso!")
            
            cursor.close()
            conn.close()
        else:
            servidor.send_message(cliente, "Erro: Dados inválidos")
    except Exception as e:
        servidor.send_message(cliente, f"Erro ao processar a mensagem: {str(e)}")

# Inicializa o servidor WebSocket
def iniciar_servidor():
    # Verifica e configura o banco de dados antes de iniciar o servidor
    configurar_banco()

    # Define a porta para o WebSocket
    servidor = WebsocketServer(8000, host='127.0.0.1')
    
    # Define a função que será chamada quando uma mensagem for recebida
    servidor.set_fn_message_received(tratar_mensagem)
    
    print("Servidor WebSocket iniciado em ws://127.0.0.1:8000")
    
    # Inicia o servidor WebSocket
    servidor.run_forever()

# Executa o servidor WebSocket
if __name__ == "__main__":
    iniciar_servidor()