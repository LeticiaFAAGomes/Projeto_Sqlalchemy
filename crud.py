from conectar_db import *
from models import *


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
        alunos = session.query(Aluno).all()
        for aluno in alunos:
            print(aluno)
            if (aluno.endereco):
                print(aluno.endereco)
            for email in aluno.emails:
                print(email)
            for disciplina in aluno.disciplinas:
                print(disciplina)
                
            print("------------------")
        
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
        