function abrir(id) {
  document.getElementById(id).style.display = "flex";
  document.body.style.overflow = "hidden";
}

function fechar(id) {
  document.getElementById(id).style.display = "none";
}

function pesquisar() {
  const tabela = document.querySelector("tbody");
  const input = document.getElementById("pesquisa").value.toLowerCase();
  const linhas = [...tabela.getElementsByTagName("tr")];
  linhas.forEach((linha) => {
    const celulas = [...linha.getElementsByTagName("td")];
    let mostrarLinha = false;
    celulas.forEach((celula) => {
      const texto = celula.textContent.toLowerCase();
      if (texto.includes(input)) {
        mostrarLinha = true;
      }
    });
    linha.style.display = mostrarLinha ? "" : "none";
  });
}

function abrirHam() {
  document.querySelector("#aside").classList.toggle("fechado");
  document.querySelector(".container").classList.toggle("completo");
}

function excluirDado(dado, endpoint) {
  enviarDado({ index: JSON.parse(dado.getAttribute("data-name")) }, endpoint);
}

async function enviarDado(dados, caminho) {
  try {
    await fetch(caminho, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(dados),
    });
  } catch (erro) {
    console.log("Não foi possível realizar o cadastro:", erro);
  }
}

function verificar_linhas() {
  tbody = document.querySelectorAll("tbody");
  td = document.querySelector("td");
  if (!td) {
    for (let i = 0; i < tbody.length; i++) {
      th = document.querySelectorAll("tr").length;
      h3 = document.createElement("td");
      h3.textContent = "Não há dados cadastrados";
      h3.classList.add("sem-dados");
      h3.setAttribute("colspan", `${th}`);
      tbody[i].appendChild(h3);
    }
  }
}
verificar_linhas();
