from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def inicio():
    return {"mensagem": "API do Gabriel funcionando!"}

@app.get("/meu-perfil")
def meu_perfil():
    return {
        "nome": "Gabriel Ribeiro",
        "cargo": "Desenvolvedor Back-end Python",
        "cidade": "São Lourenço da Serra, SP",
        "repositorios": 3,
        "projeto_favorito": "limpador-planilhas-automatico"
    }
@app.get("/projetos")
def meus_projetos():
    return [
        {
            "nome": "limpador-planilhas-automatico",
            "linguagem": "Python",
            "descricao": "Automatiza limpeza de planilhas"
        },
        {
            "nome": "exercicios-python-ebac",
            "linguagem": "Python",
            "descricao": "Exercícios do curso de Python"
        }
    ]
@app.get("/projetos/{nome_projeto}")
def buscar_projeto(nome_projeto: str):
    projetos = {
        "limpador-planilhas-automatico": "Automatiza limpeza de planilhas com Python",
        "exercicios-python-ebac": "Exercícios do curso de Python"
    }
    return {
        "projeto": nome_projeto,
        "descricao": projetos.get(nome_projeto, "Projeto não encontrado")
    }