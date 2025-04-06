from conectar_db import *
from models import *
from sqlalchemy import func


session = conectar()


def incluir_aluno(nome, endereco, **emails):
    aluno = Aluno(nome)
    aluno.endereco = Aluno_Endereco(endereco)
    aluno.emails = [Aluno_Email(email) for email in emails.get('emails', [])]
    
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
        
        
def incluir_disciplinas(nome, creditos):
    disciplina = Disciplina(nome, creditos)
    
    try:    
        session.add(disciplina)
        session.commit()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
        
def consultar_disciplinas():
    materias = []
    
    try:
        disciplinas = session.query(Disciplina).all()
        for disciplina in disciplinas:
            materias.append([disciplina.id, disciplina.nome, disciplina.creditos])
            
        return materias
    
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
        
        
def incluir_professor(nome, endereco, **emails):
    professor = Professor(nome)
    professor.endereco = Professor_Endereco(endereco)
    professor.emails = [Professor_Email(email) for email in emails.get('emails', [])]
    
    try:
        session.add(professor)
        session.commit()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        

def incluir_professor_disciplina(id_professor, id_disciplina):
    try:
        session.add(Professor_Disciplina(id_professor, id_disciplina))
        session.commit()
        
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
        
def consultar_professores():
    lecionadores = []
    try:
        professores = session.query(Professor).all()
        for professor in professores:
            emails=''
            for email in professor.emails:
                emails += f'{email.email}, '
                
            lecionadores.append([professor.id, professor.nome, professor.endereco.rua, emails[:len(emails)-2]])
            
        return lecionadores
    
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
 
        
def consultar_professor_disciplina():
    professores_disciplinas = []
    try:
        professores = session.query(Professor).all()
    
        for professor in professores:
            for disciplina in professor.disciplinas:
                professores_disciplinas.append([professor.nome, disciplina.nome])
                
        return professores_disciplinas
    
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
        
        
def somar_dinheiro(col):
    try:
        return session.query(func.sum(col)).scalar()
    
    except Exception as ex:
        print(ex)
        
    finally:
        desconectar(session)
        
    