function abrir(id) {
  document.getElementById(id).style.display = "flex";
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

async function enviarDado(dados, caminho) {
  console.log(caminho);
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
