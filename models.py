from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Aluno(Base):
    __tablename__ = 'Aluno'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    endereco = relationship('Endereco', uselist=False)
    emails = relationship('Email')
    
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
    
    