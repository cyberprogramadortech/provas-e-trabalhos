import asyncio
import websockets

# Função para conectar ao servidor WebSocket e receber os dados
async def get_perfis():
    uri = "ws://localhost:8765"  # Endereço do servidor WebSocket
    try:
        # Tenta se conectar ao servidor WebSocket
        async with websockets.connect(uri) as websocket:
            # Receber os dados do servidor
            perfis = await websocket.recv()
            
            # Exibir os dados recebidos
            print("Dados recebidos do servidor:")
            print(perfis)
    except Exception as e:
        print(f"Erro na conexão: {e}")

# Iniciar o cliente
if __name__ == "__main__":
    asyncio.run(get_perfis())  # Utiliza asyncio.run() para rodar a função assíncrona