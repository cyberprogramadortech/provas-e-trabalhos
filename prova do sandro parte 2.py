import websocket # type: ignore

# Função chamada quando o cliente receber uma resposta do servidor
def on_message(ws, message):
    print(f"Resposta do servidor: {message}")

# Função chamada quando a conexão WebSocket for aberta
def on_open(ws):
    print("Conectado ao servidor WebSocket")

    # Recebe os dados do usuário
    id = input("Diga o ID: ")
    idPerfil = input("Diga o ID do perfil: ")
    nome = input("Diga o nome: ")
    numSeg = input("Diga o número de seguidores: ")
    numPost = input("Diga o número de posts: ")
    numSeguindo = input("Diga o número de seguindo: ")
    
    # Envia os dados para o servidor no formato adequado
    mensagem = f"{id},{idPerfil},{nome},{numSeg},{numPost},{numSeguindo}"
    ws.send(mensagem)

# Função chamada quando a conexão WebSocket for fechada
def on_close(ws, close_status_code, close_msg):
    print("Conexão fechada")

# Função principal para iniciar a conexão WebSocket
def iniciar_cliente():
    url_servidor = "ws://127.0.0.1:8000"
    
    # Cria a conexão WebSocket
    ws = websocket.WebSocketApp(url_servidor,
                                on_message=on_message,
                                on_open=on_open,
                                on_close=on_close)
    
    # Inicia a aplicação WebSocket
    ws.run_forever()

# Executa o cliente
if __name__ == "__main__":
    iniciar_cliente()