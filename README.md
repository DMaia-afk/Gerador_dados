# Gerador de Dados Falsos para Loja de Eletrônicos

Este projeto é um gerador simples de dados falsos para vendas em uma loja de eletrônicos, utilizando a biblioteca Faker para criar informações simuladas realistas.

## Descrição

O script `geradorfake.py` gera um arquivo JSON contendo 6000 registros de vendas fictícias para uma loja chamada "Loja de Eletrônicos XYZ". Cada registro inclui informações como nome da loja, endereço, bairro, cidade, produto vendido, valor da venda e um ID único.

## Requisitos

- Python 3.6 ou superior
- Biblioteca Faker

## Instalação

1. Clone este repositório:
   ```
   git clone https://github.com/DMaia-afk/Gerador_dados.git
   cd Gerador_dados
   ```

2. Instale as dependências:
   ```
   pip install faker
   ```

## Uso

Execute o script Python:
```
python geradorfake.py
```

Isso irá gerar um arquivo chamado `dados_vendas_6000_registros.json` no diretório atual, contendo os dados simulados.

## Estrutura dos Dados

Cada registro no JSON é um objeto com as seguintes chaves:
- `loja`: Nome da loja (fixo como "Loja de Eletrônicos XYZ")
- `endereco`: Endereço fictício da loja
- `bairro`: Bairro fictício
- `cidade`: Cidade fictícia
- `produto`: Produto vendido (sorteado de uma lista de 5 itens: Smartphone, Notebook, Tablet, Smart TV, Fone de Ouvido)
- `valor`: Valor da venda em reais (número aleatório entre 100 e 5000)
- `id_registro`: ID único do registro (de 1 a 6000)

## Exemplo de Saída

```json
[
  {
    "loja": "Loja de Eletrônicos XYZ",
    "endereco": "Rua das Flores, 123",
    "bairro": "Centro",
    "cidade": "São Paulo",
    "produto": "Smartphone",
    "valor": 1500,
    "id_registro": 1
  },
  ...
]
```

## Personalização

Você pode modificar o script para alterar:
- O número de registros: mude a variável `NUM_REGISTROS`
- O nome da loja: mude `NOME_LOJA`
- A lista de produtos: mude `ITENS_VENDAS`
- O range de valores: mude os parâmetros `min` e `max` em `fake.random_int(min=100, max=5000)`
- A semente para reprodutibilidade: mude `Faker.seed(42)`
- O locale: mude `fake = Faker('pt_BR')` para outro locale suportado pelo Faker

## Licença

Este projeto é de código aberto. Sinta-se à vontade para usar e modificar conforme necessário.

## Autor

DMaia-afk