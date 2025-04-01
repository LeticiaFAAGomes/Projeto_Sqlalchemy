from models import *
from conectar_db import *


def incluir_aluno_endereco_email():
    aluno = Aluno('Letícia')
    aluno.endereco = Endereco('Rua da Letícia')
    aluno.emails = [Email('leticia@email.com'), Email('leticia@al.infnet.edu.br')]
    session = conectar()
    
    try:
        session.add(aluno)
        session.commit()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
        
def consultar_aluno(id):
    session = conectar()
    
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
        
incluir_aluno_endereco_email()
consultar_aluno(1)