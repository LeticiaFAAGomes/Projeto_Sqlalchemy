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
