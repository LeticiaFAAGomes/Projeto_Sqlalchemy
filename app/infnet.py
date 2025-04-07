from app.crud import *
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from starlette.staticfiles  import StaticFiles


app = FastAPI()
templates = Jinja2Templates(directory='app/templates')
app.mount('/static', StaticFiles(directory='app/static'), name='static') 


@app.get('/')
async def navegar_dashboard(request:Request):
    return templates.TemplateResponse('dashboard.html', {'request': request,
                                                         'alunos': contar_dado(Aluno.id),
                                                         'professores': contar_dado(Professor.id),
                                                         'disciplinas': contar_dado(Disciplina.id),
                                                         'creditos': f'{somar_dinheiro():.2f}',
                                                         'professores_disciplinas': contar_dado(Professor_Disciplina.id_professor),
                                                         'alunos_disciplinas': contar_dado(Aluno_Disciplina.id_aluno)})


@app.post('/dados_aluno')
async def carregar_dados_aluno(request:Request):
    dados = await request.json()
    nome_aluno = dados.get('nome')
    endereco_aluno = dados.get('endereco')
    emails_aluno = dados.get('emails')
    incluir_aluno(nome=nome_aluno, endereco=endereco_aluno, emails=emails_aluno)


@app.post('/dados_aluno_disciplina')
async def carregar_dados_aluno_disciplina(request:Request):
    dados = await request.json()
    id_aluno = dados.get('id_aluno')
    id_disciplina = dados.get('id_disciplina')
    incluir_aluno_disciplina(id_aluno=id_aluno, id_disciplina=id_disciplina)    


@app.post('/dados_professor')
async def carregar_dados_professores(request:Request):
    dados = await request.json()
    nome_professor = dados.get('nome')
    endereco_professor = dados.get('endereco')
    emails_professor = dados.get('emails')
    incluir_professor(nome=nome_professor, endereco=endereco_professor, emails=emails_professor)


@app.post('/dados_professor_disciplina')
async def carregar_dados_professor_disciplina(request:Request):
    dados = await request.json()
    id_professor = dados.get('id_professor')
    id_disciplina = dados.get('id_disciplina')
    incluir_professor_disciplina(id_professor, id_disciplina)    
    
    
@app.post('/dados_disciplina')
async def carregar_dados_professores(request:Request):
    dados = await request.json()
    nome_disciplina = dados.get('nome')
    creditos_disciplina = dados.get('creditos')
    incluir_disciplinas(nome=nome_disciplina, creditos=creditos_disciplina)


@app.get('/alunos')
async def navegar_alunos(request:Request):
    return templates.TemplateResponse('aluno.html', {'request': request, 
                                                     'alunos': consultar_alunos(),
                                                     'disciplinas': consultar_disciplinas(),
                                                     'qtd_aluno': contar_dado(Aluno.id),
                                                     'qtd_aluno_disciplina': contar_dado(Aluno_Disciplina.id_aluno)})


@app.get('/professores')
async def navegar_professores(request:Request):
    return templates.TemplateResponse('professor.html', {'request': request,
                                                         'professores': consultar_professores(),
                                                         'disciplinas': consultar_disciplinas(),
                                                         'qtd_professor': contar_dado(Professor.id),
                                                         'qtd_professor_disciplina': contar_dado(Professor_Disciplina.id_professor)})


@app.get('/disciplinas')
async def navegar_disciplinas(request:Request):
    return templates.TemplateResponse('disciplina.html', {'request': request,
                                                          'disciplinas': consultar_disciplinas(),
                                                          'qtd_disciplinas': contar_dado(Disciplina.id),
                                                          'qtd_aluno_disciplina': contar_dado(Aluno_Disciplina.id_aluno),
                                                          'qtd_professor_disciplina': contar_dado(Professor_Disciplina.id_professor),
                                                          'professores_disciplinas':consultar_professor_disciplina(),
                                                          'alunos_disciplinas': consultar_aluno_disciplina()})
    