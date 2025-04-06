from crud import *
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles  import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static") 


@app.get("/")
async def navegar_index(request:Request):
    return templates.TemplateResponse("aluno.html", {"request": request})


@app.post('/dados_aluno')
async def carregar_dados(request:Request):
    dados = await request.json()
    nome_aluno = dados.get('nome')
    endereco_aluno = dados.get('endereco')
    emails_aluno = dados.get('emails')
    incluir_aluno(nome=nome_aluno, endereco=endereco_aluno, emails=emails_aluno)
    return {'mensagem':f'os dados de {nome_aluno} foram salvos com sucesso!'}


# incluir_aluno('Letícia', 'Rua da Letícia', emails=['leticia@email.com', 'leticia@al.infnet.edu.br'])
# incluir_aluno('Arthur', 'Rua do Arthur', emails=['arthur@email.com'])
# incluir_aluno('Augusto', 'Rua do Augusto', emails=['augusto@email.com'])

incluir_disciplinas('SQL', 400)
incluir_disciplinas('Python', 400)
incluir_disciplinas('Projeto de Bloco', 500)
incluir_disciplinas('C++', 400)

# incluir_aluno_disciplina(1, 1)
# incluir_aluno_disciplina(1, 2)
# incluir_aluno_disciplina(1, 3)
# incluir_aluno_disciplina(2, 1)
# incluir_aluno_disciplina(2, 3)

# consultar_alunos()
# excluir_aluno(1)
# consultar_alunos()
