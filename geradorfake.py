import json
from faker import Faker

NUM_REGISTROS = 6000
NOME_LOJA = "Loja de Eletrônicos XYZ"
ITENS_VENDAS = ["Smartphone", "Notebook", "Tablet", "Smart TV", "Fone de Ouvido"]

Faker.seed(42)
fake = Faker('pt_BR')

def gerar_dados_venda(registro_id):
    """Retorna um Dicionário que será salvo no JSON."""
    produto = fake.random_element(ITENS_VENDAS)
    valor = fake.random_int(min=100, max=5000)
    return {
        "loja": NOME_LOJA, 
        "endereco": fake.street_address(),
        "bairro": fake.bairro(),
        "cidade": fake.city(),
        "produto": produto,
        "valor": valor,
        "id_registro": registro_id 
    }

# Geração da lista de Dicionários (formato JSON)
dados_simulados_json = []
for i in range(NUM_REGISTROS):
    dados_simulados_json.append(gerar_dados_venda(i + 1)) 

# Salvar a lista no arquivo JSON
nome_arquivo = "dados_vendas_6000_registros.json"
try:
    with open(nome_arquivo, 'w', encoding='utf-8') as f:
        # json.dump é a função que escreve o objeto Python como JSON no arquivo.
        json.dump(dados_simulados_json, f, ensure_ascii=False, indent=2)
    print(f"✅ Arquivo JSON gerado com sucesso: '{nome_arquivo}'!")
except IOError as e:
    print(f"❌ Erro ao escrever o arquivo JSON: {e}")