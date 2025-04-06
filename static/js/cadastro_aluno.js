function verificarCamposObrigatorios(dados) {
  return dados.every((dado) => dado != "");
}

function addEmail(row1) {
  const div = document.getElementById("emails");
  const row = document.createElement("div");

  row.classList.add("row");
  row.innerHTML = ` <input type="email" class="email" placeholder="Insira o e-mail do aluno" />
                    <a onclick="addEmail(this)" id="btn_email"><img src="/static/images/add.svg" alt="" /></a>`;
  div.appendChild(row);
  row1.remove();
}

function addLista(osEmails) {
  const emails = [];
  for (let i = 0; i < osEmails.length; i++) {
    emails.push(osEmails[i].value);
  }
  return emails;
}

function exibirMsg(ehSucesso = false, msg) {
  const aviso = document.getElementById("aviso");
  if (ehSucesso) {
    aviso.classList.add("sucesso");
    aviso.innerHTML = `${msg}`;
    setTimeout(() => {
      window.location.reload();
    }, 2000);
  } else {
    aviso.classList.add("erro");
    aviso.innerHTML = `${msg}`;
    setTimeout(() => {
      aviso.classList.remove("erro");
    }, 2000);
  }
}

function registrarAluno(nome, endereco, emails) {
  let validaCamposObrigatorios = verificarCamposObrigatorios([nome, endereco, emails]);
  let listaEmails = addLista(emails);

  if (validaCamposObrigatorios) {
    enviarDado({ nome: nome, endereco: endereco, emails: listaEmails }, "/dados_aluno");
    return {
      ehSucesso: true,
      msg: `${nome} foi cadastrado(a) com sucesso.`,
    };
  } else {
    return {
      ehSucesso: false,
      msg: "Todos os campos devem ser preenchidos!",
    };
  }
}

function cadastrar() {
  const nome = document.getElementById("nome").value;
  const endereco = document.getElementById("endereco").value;
  const emails = document.getElementsByClassName("email");

  msg = registrarAluno(nome, endereco, emails);
  exibirMsg(msg.ehSucesso, msg.msg);
}

function cadastrarAlunoDisciplina() {
  const selectAluno = parseInt(document.getElementById("aluno-select").value);
  const selectDisciplina = parseInt(document.getElementById("disciplina-select").value);

  if (selectAluno && selectDisciplina) {
    enviarDado({ id_aluno: selectAluno, id_disciplina: selectDisciplina }, "/dados_aluno_disciplina");
    exibirMsg(true, "A inscrição foi realizada com sucesso!");
  } else {
    exibirMsg(false, "Não foi possível realizar a inscrição.");
  }
}
