DROP DATABASE IF EXISTS infnet;
CREATE DATABASE IF NOT EXISTS infnet;
USE infnet;

CREATE TABLE IF NOT EXISTS Aluno (

	id    INT PRIMARY KEY AUTO_INCREMENT,
    nome  VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Aluno_Endereco (

	id        INT PRIMARY KEY AUTO_INCREMENT,
    rua       VARCHAR(50) NOT NULL,
    id_aluno  INT NOT NULL UNIQUE,
    
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id)
);

CREATE TABLE IF NOT EXISTS Aluno_Email (

	id        INT PRIMARY KEY AUTO_INCREMENT,
    email     VARCHAR(50) NOT NULL,
    id_aluno  INT NOT NULL,

    FOREIGN KEY (id_aluno) REFERENCES Aluno(id)
);

CREATE TABLE IF NOT EXISTS Disciplina (

	id         INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nome       VARCHAR(30) NOT NULL,
	creditos   INT NOT NULL
);

CREATE TABLE IF NOT EXISTS Aluno_Disciplina (

	id_aluno       INT NOT NULL,
	id_disciplina  INT NOT NULL,
	data           DATE NOT NULL,

	PRIMARY KEY (id_aluno, id_disciplina),

	FOREIGN KEY (id_aluno) REFERENCES Aluno(id),
	FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);

CREATE TABLE IF NOT EXISTS Professor (

	id    INT PRIMARY KEY NOT NULL AUTO_INCREMENT,
	nome  VARCHAR(50) NOT NULL
);

CREATE TABLE IF NOT EXISTS Professor_Endereco (

	id            INT PRIMARY KEY AUTO_INCREMENT,
    rua           VARCHAR(50) NOT NULL,
    id_professor  INT NOT NULL UNIQUE,
    
    FOREIGN KEY (id_professor) REFERENCES Professor(id)
);

CREATE TABLE IF NOT EXISTS Professor_Email (

	id           INT PRIMARY KEY AUTO_INCREMENT,
    email        VARCHAR(50) NOT NULL,
    id_professor INT NOT NULL,

    FOREIGN KEY (id_professor) REFERENCES Professor(id)
);

CREATE TABLE IF NOT EXISTS Professor_Disciplina (

	id_professor   INT NOT NULL,
	id_disciplina  INT NOT NULL,

	PRIMARY KEY (id_professor, id_disciplina),

	FOREIGN KEY (id_professor) REFERENCES Professor(id),
	FOREIGN KEY (id_disciplina) REFERENCES Disciplina(id)
);
