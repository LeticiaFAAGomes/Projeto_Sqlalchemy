function verificarCamposObrigatorios(dados) {
  return dados.every((dado) => dado != "");
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

function registrarDisciplina(nome, creditos) {
  let validaCamposObrigatorios = verificarCamposObrigatorios([nome, creditos]);

  if (validaCamposObrigatorios) {
    enviarDado({ nome: nome, creditos: creditos }, "/dados_disciplina");
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
  const creditos = document.getElementById("creditos").value;

  msg = registrarDisciplina(nome, creditos);
  exibirMsg(msg.ehSucesso, msg.msg);
}
