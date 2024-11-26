import asyncio
import websockets

# Dados fictícios que antes estariam no MySQL
perfis = [
    {"id": 1, "idPerfil": "101", "nomePerfil": "João", "numSeguidores": 1000, "numPosts": 200, "numSeguindo": 50},
    {"id": 2, "idPerfil": "102", "nomePerfil": "Maria", "numSeguidores": 1500, "numPosts": 300, "numSeguindo": 70},
    {"id": 3, "idPerfil": "103", "nomePerfil": "Carlos", "numSeguidores": 1200, "numPosts": 250, "numSeguindo": 60},
]

# Função que será executada quando um cliente se conectar
async def handler(websocket, path):
    try:
        # Enviar os dados fictícios para o cliente (convertendo para string)
        print(f"Conexão estabelecida com {websocket.remote_address}")
        await websocket.send(str(perfis))
        print(f"Dados enviados para {websocket.remote_address}")
    except Exception as e:
        print(f"Erro ao enviar dados para o cliente: {e}")

# Função principal para iniciar o servidor
async def main():
    try:
        # Iniciar o servidor WebSocket
        server = await websockets.serve(handler, "localhost", 8765)
        print("Servidor WebSocket iniciado na porta 8765...")
        
        # Manter o servidor rodando
        await server.wait_closed()
    except Exception as e:
        print(f"Erro ao iniciar o servidor: {e}")

# Rodar o servidor WebSocket
if __name__ == "__main__":
    asyncio.run(main())  # Utiliza asyncio.run() para rodar o servidor WebSocket