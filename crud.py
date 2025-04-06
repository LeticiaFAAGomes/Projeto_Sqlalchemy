from conectar_db import *
from models import *
from sqlalchemy import func


session = conectar()


def incluir_aluno(nome, endereco, **emails):
    aluno = Aluno(nome)
    aluno.endereco = Endereco(endereco)
    aluno.emails = [Email(email) for email in emails.get('emails', [])]
    
    try:
        session.add(aluno)
        session.commit()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
        
def consultar_aluno(id):
    try:
        aluno = session.get(Aluno, id)
        print(aluno)
        print(aluno.endereco)
        for email in aluno.emails:
            print(email)
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
        
def consultar_alunos():
    try:
        estudantes = []
        alunos = session.query(Aluno).all()
        for aluno in alunos:
            emails = ''
            for email in aluno.emails:
                emails += f'{email.email}, '
                
            estudantes.append([aluno.id, aluno.nome, aluno.endereco.rua, emails[:len(emails)-2]])
        return estudantes
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
        
def incluir_disciplinas(disciplina, creditos):
    disciplina = Disciplina(disciplina, creditos)
    try:    
        session.add(disciplina)
        session.commit()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
    
    
def incluir_aluno_disciplina(id_aluno, id_disciplina):
    
    try:
        session.add(Aluno_Disciplina(id_aluno, id_disciplina))
        session.commit()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
        
def excluir_aluno(id):
    try:
        aluno = session.get(Aluno, id)
        if (aluno):
            session.delete(aluno)
            session.commit()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
    
def contar_dado(col):
    try:
        return session.query(func.count(col)).scalar()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)