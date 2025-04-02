from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Aluno(Base):
    __tablename__ = 'Aluno'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = relationship('Endereco', uselist=False, cascade="all, delete")
    emails = relationship('Email', cascade="all, delete")
    disciplinas = relationship('Disciplina', secondary='Aluno_Disciplina', back_populates='alunos')

    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self):
        return f'{self.id} {self.nome}'


class Endereco(Base):
    __tablename__ = 'Endereco'
    
    id = Column(Integer, primary_key=True)
    rua = Column(String, nullable=False)
    id_aluno = Column(Integer, ForeignKey('Aluno.id'))
    aluno = relationship('Aluno', back_populates='endereco')
    
    def __init__(self, rua):
        self.rua = rua
        
    def __str__(self):
        return f'{self.id} {self.rua} {self.id_aluno}'


class Email(Base):
    __tablename__ = 'Email'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    id_aluno = Column(Integer, ForeignKey('Aluno.id'))
    alunos = relationship('Aluno', back_populates='emails') # 
    
    def __init__(self, email):
        self.email = email
        
    def __str__(self):
        return f'{self.id} {self.email} {self.id_aluno}'
    
    
class Disciplina(Base):
    __tablename__ = 'Disciplina'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    creditos = Column(Integer, nullable=False)
    alunos = relationship('Aluno', secondary='Aluno_Disciplina', back_populates='disciplinas')
    
    def __init__(self, nome, creditos):
        self.nome = nome
        self.creditos = creditos
        
    def __str__(self):
        return f'{self.id} {self.nome} {self.creditos}'


class Aluno_Disciplina(Base):
    __tablename__ = 'Aluno_Disciplina'
    
    id_aluno = Column(Integer, ForeignKey('Aluno.id', ondelete='cascade'), primary_key=True)
    id_disciplina = Column(Integer, ForeignKey('Disciplina.id'), primary_key=True)
    
    def __init__(self, id_aluno, id_disciplina):
        self.id_aluno = id_aluno
        self.id_disciplina = id_disciplina
        
    def __str__(self):
        return f'{self.id_aluno} {self.id_disciplina}'