DROP DATABASE IF EXISTS infnet;
CREATE DATABASE infnet;
USE infnet;

CREATE TABLE Aluno (

	id    INT PRIMARY KEY AUTO_INCREMENT,
    nome  VARCHAR(50) NOT NULL
);

CREATE TABLE Endereco (

	id        INT PRIMARY KEY AUTO_INCREMENT,
    rua       VARCHAR(50) NOT NULL,
    id_aluno  INT NOT NULL UNIQUE,
    
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id)
);

CREATE TABLE Email (

	id        INT PRIMARY KEY AUTO_INCREMENT,
    email     VARCHAR(50) NOT NULL,
    id_aluno  INT NOT NULL,

    FOREIGN KEY (id_aluno) REFERENCES Aluno(id)
);

CREATE TABLE Disciplina (

	id               INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nome             VARCHAR(30) NOT NULL,
	creditos         INT NOT NULL
);

CREATE TABLE Aluno_Disciplina (

	id_aluno       INT NOT NULL,
	id_disciplina  INT NOT NULL,

	PRIMARY KEY (id_aluno, id_disciplina),

	FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
	FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);

CREATE TABLE Professor (

	id               INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nome             VARCHAR(30) NOT NULL
);

CREATE TABLE Professor_Disciplina (

	id_professor   INT NOT NULL,
	id_disciplina  INT NOT NULL,

	PRIMARY KEY (id_professor, id_disciplina),

	FOREIGN KEY (id_professor) REFERENCES Professor(id),
	FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);