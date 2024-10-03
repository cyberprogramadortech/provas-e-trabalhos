#Prova Subjetiva De Python
#Nome:Alex Sandro De Castro Queiroz Pereira Filho
#Curso:Análise e desenvolvimento de sistemas
#Professor:Sandro Costa Mesquita
#Disciplina:Linguagem De Programação 2
#Turma/Turno:Manhã
#Data:03/10/24

#Supermercado Bom Preço

import pandas as pd
import os
import json

# Inicializando os dados
produtos = {}
vendas = []

# Produtos padrão
produtos_padrao = {
    '001': {'nome': 'Arroz', 'quantidade': 10, 'preco': 5.0},
    '002': {'nome': 'Feijão', 'quantidade': 5, 'preco': 10.0},
    '003': {'nome': 'Macarrão', 'quantidade': 20, 'preco': 15.0},
    '004': {'nome': 'Biscoito', 'quantidade': 8, 'preco': 3.5},
    '005': {'nome': 'Chilito', 'quantidade': 12, 'preco': 2.0},
}

# Função para carregar produtos de um arquivo JSON
def carregar_produtos():
    global produtos
    if os.path.exists('produtos.json'):
        with open('produtos.json', 'r') as f:
            produtos = json.load(f)
    else:
        # Se o arquivo não existir, carregar produtos padrão
        produtos.update(produtos_padrao)

# Função para carregar vendas de um arquivo CSV
def carregar_vendas():
    global vendas
    if os.path.exists('vendas.csv'):
        vendas = pd.read_csv('vendas.csv').to_dict(orient='records')

# Função para salvar produtos em um arquivo JSON
def salvar_produtos():
    with open('produtos.json', 'w') as f:
        json.dump(produtos, f)

# Função para salvar vendas em um arquivo CSV
def salvar_vendas():
    df = pd.DataFrame(vendas)
    df.to_csv('vendas.csv', index=False)

def cadastrar_produto(codigo, nome, quantidade, preco):
    if codigo in produtos:
        print("Produto já cadastrado.")
    else:
        produtos[codigo] = {'nome': nome, 'quantidade': quantidade, 'preco': preco}
        print("Produto cadastrado com sucesso.")

def registrar_venda(codigo, quantidade_vendida):
    if codigo not in produtos:
        print("Produto não encontrado.")
        return
    
    if produtos[codigo]['quantidade'] >= quantidade_vendida:
        produtos[codigo]['quantidade'] -= quantidade_vendida
        valor_total = produtos[codigo]['preco'] * quantidade_vendida
        vendas.append({
            'codigo': codigo,
            'nome': produtos[codigo]['nome'],
            'quantidade': quantidade_vendida,
            'valor_total': valor_total
        })
        print("Venda registrada com sucesso.")
    else:
        print("Quantidade em estoque insuficiente.")

def atualizar_produto(codigo, novo_nome=None, nova_quantidade=None, novo_preco=None):
    if codigo not in produtos:
        print("Produto não encontrado.")
        return

    if novo_nome:
        produtos[codigo]['nome'] = novo_nome
    if nova_quantidade is not None:
        produtos[codigo]['quantidade'] = nova_quantidade
    if novo_preco is not None:
        produtos[codigo]['preco'] = novo_preco

    print("Produto atualizado com sucesso.")

def gerar_relatorio_vendas():
    df = pd.DataFrame(vendas)
    df.to_csv('relatorio_vendas.csv', index=False)
    print("Relatório de vendas gerado com sucesso.")

def gerar_relatorio_estoque():
    with open('relatorio_estoque.txt', 'w') as f:
        for codigo, info in produtos.items():
            f.write(f"Código: {codigo}, Nome: {info['nome']}, Quantidade: {info['quantidade']}\n")
    print("Relatório de estoque gerado com sucesso.")

def validar_entrada_int(mensagem):
    while True:
        try:
            valor = int(input(mensagem))
            if valor < 0:
                print("Por favor, insira um número não negativo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número inteiro.")

def validar_entrada_float(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor < 0:
                print("Por favor, insira um número não negativo.")
                continue
            return valor
        except ValueError:
            print("Entrada inválida. Por favor, insira um número decimal.")

def exibir_menu():
    carregar_produtos()
    carregar_vendas()
    
    while True:
        print("\nMenu:")
        print("1. Cadastrar Produto")
        print("2. Registrar Venda")
        print("3. Atualizar Produto")
        print("4. Gerar Relatório de Vendas")
        print("5. Gerar Relatório de Estoque")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            codigo = input("Código do produto: ")
            nome = input("Nome do produto: ")
            quantidade = validar_entrada_int("Quantidade em estoque: ")
            preco = validar_entrada_float("Preço por unidade: ")
            cadastrar_produto(codigo, nome, quantidade, preco)
            salvar_produtos()
        
        elif escolha == '2':
            codigo = input("Código do produto: ")
            quantidade_vendida = validar_entrada_int("Quantidade vendida: ")
            registrar_venda(codigo, quantidade_vendida)
            salvar_vendas()

        elif escolha == '3':
            codigo = input("Código do produto a ser atualizado: ")
            novo_nome = input("Novo nome do produto (deixe em branco para não alterar): ")
            nova_quantidade = input("Nova quantidade em estoque (deixe em branco para não alterar): ")
            novo_preco = input("Novo preço por unidade (deixe em branco para não alterar): ")
            
            # Converter para os tipos corretos
            nova_quantidade = int(nova_quantidade) if nova_quantidade else None
            novo_preco = float(novo_preco) if novo_preco else None
            
            atualizar_produto(codigo, novo_nome if novo_nome else None, nova_quantidade, novo_preco)

            salvar_produtos()

        elif escolha == '4':
            gerar_relatorio_vendas()
        
        elif escolha == '5':
            gerar_relatorio_estoque()
        
        elif escolha == '6':
            print("Saindo do sistema.")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    exibir_menu()