from crud import *


incluir_aluno('Letícia', 'Rua da Letícia', emails=['leticia@email.com', 'leticia@al.infnet.edu.br'])
incluir_aluno('Arthur', 'Rua do Arthur', emails=['arthur@email.com'])
incluir_aluno('Augusto', 'Rua do Augusto', emails=['augusto@email.com'])

incluir_disciplinas('SQL', 400)
incluir_disciplinas('Python', 400)
incluir_disciplinas('Projeto de Bloco', 500)
incluir_disciplinas('C++', 400)

incluir_aluno_disciplina(1, 1)
incluir_aluno_disciplina(1, 2)
incluir_aluno_disciplina(1, 3)
incluir_aluno_disciplina(2, 1)
incluir_aluno_disciplina(2, 3)
