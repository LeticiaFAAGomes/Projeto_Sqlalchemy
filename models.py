from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import declarative_base, relationship


Base = declarative_base()


class Aluno(Base):
    __tablename__ = 'Aluno'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = relationship('Aluno_Endereco', uselist=False, cascade="all, delete")
    emails = relationship('Aluno_Email', cascade="all, delete")
    disciplinas = relationship('Disciplina', secondary='Aluno_Disciplina', back_populates='alunos')

    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self):
        return f'{self.id} {self.nome}'


class Aluno_Endereco(Base):
    __tablename__ = 'Aluno_Endereco'
    
    id = Column(Integer, primary_key=True)
    rua = Column(String, nullable=False)
    id_aluno = Column(Integer, ForeignKey('Aluno.id'))
    aluno = relationship('Aluno', back_populates='endereco')
    
    def __init__(self, rua):
        self.rua = rua
        
    def __str__(self):
        return f'{self.id} {self.rua} {self.id_aluno}'


class Aluno_Email(Base):
    __tablename__ = 'Aluno_Email'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    id_aluno = Column(Integer, ForeignKey('Aluno.id'))
    alunos = relationship('Aluno', back_populates='emails')
    
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
    professores = relationship('Professor', secondary='Professor_Disciplina', back_populates='disciplinas')
    
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
    
    
class Professor(Base):
    __tablename__ = 'Professor'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String, nullable=False)
    endereco = relationship('Professor_Endereco', uselist=False, cascade="all, delete")
    emails = relationship('Professor_Email', cascade="all, delete")
    disciplinas = relationship('Disciplina', secondary='Professor_Disciplina', back_populates='professores')
    
    def __init__(self, nome):
        self.nome = nome
        
    def __str__(self):
        return f'{self.id} {self.nome}'
    
class Professor_Endereco(Base):
    __tablename__ = 'Professor_Endereco'
    
    id = Column(Integer, primary_key=True)
    rua = Column(String, nullable=False)
    id_professor = Column(Integer, ForeignKey('Professor.id'))
    professor = relationship('Professor', back_populates='endereco')
    
    def __init__(self, rua):
        self.rua = rua
        
    def __str__(self):
        return f'{self.id} {self.rua} {self.id_aluno}'


class Professor_Email(Base):
    __tablename__ = 'Professor_Email'
    
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    id_professor = Column(Integer, ForeignKey('Professor.id'))
    professores = relationship('Professor', back_populates='emails')
    
    def __init__(self, email):
        self.email = email
        
    def __str__(self):
        return f'{self.id} {self.email} {self.id_aluno}'


class Professor_Disciplina(Base):
    __tablename__ = 'Professor_Disciplina'
    
    id_professor = Column(Integer, ForeignKey('Professor.id', ondelete='cascade'), primary_key=True)
    id_disciplina = Column(Integer, ForeignKey('Disciplina.id'), primary_key=True)
    
    def __init__(self, id_professor, id_disciplina):
        self.id_professor = id_professor
        self.id_disciplina = id_disciplina
    
    def __str__(self):
        return f'{self.id_professor} {self.id_disciplina}'
    