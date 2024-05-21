#Rápida de colocar API no ar 
# Documentação automatica
# Assincronos (eficiente, mais novo)

#Antes de começar após baixar no terminal, colocar "uvicorn nomeArquivo:app"


from fastapi import FastAPI

app = FastAPI()

vendas = {
    1: {"item": "lata", "preco_unitario": 4, "quantidade": 5},
    2: {"item": "garrafa 2L", "preco_unitario": 15, "quantidade": 5},
    3: {"item": "garrafa 750ml", "preco_unitario": 10, "quantidade": 5},
    4: {"item": "lata mini", "preco_unitario": 2, "quantidade": 5},
    
} 




@app.get("/") #não precisa passar nenhuma parametro
def home():
    return {"Vendas": len(vendas)} #Codigo 200 = OK, vai dar como response essa frase

@app.get("/vendas/{id_venda}") #diferente do flask que coloca o numero de id entre <>, esse coloca entre chaves
def pegar_venda(id_venda: int): #qual o tipo de variavel que vai ser que o FastAPI pede = id_venda: int pra mais praticidade
    return vendas[id_venda] #retorna a venda de posição do id_venda
    
    





