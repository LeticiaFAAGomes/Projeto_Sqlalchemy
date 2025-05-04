google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(() => {
  add_grafico_pizza(
    [
      ["Cadastrados", parsearJSON("grafico_pizza_professor-disciplina").qtdDisc],
      ["Não cadastrados", parsearJSON("grafico_pizza_professor-disciplina").qtdTotal - parsearJSON("grafico_pizza_professor-disciplina").qtdDisc],
    ],
    "grafico_pizza_professor-disciplina"
  );
  add_grafico_pizza(
    [
      ["Matriculados", parsearJSON("grafico_pizza_aluno-disciplina").qtdDisc],
      ["Não matriculados", parsearJSON("grafico_pizza_aluno-disciplina").qtdTotal - parsearJSON("grafico_pizza_aluno-disciplina").qtdDisc],
    ],
    "grafico_pizza_aluno-disciplina"
  );
  // add_grafico_area_degrau(parsearJSON("creditos"), "creditos");
});

function parsearJSON(id) {
  json = JSON.parse(document.querySelector(id));
  if (json) {
    return json.getAttribute("data-json");
  }
  return 0;
}

function add_grafico_area_degrau(colunas, id) {
  const dado = new google.visualization.DataTable();
  dado.addColumn("string", "Data");
  dado.addColumn("number", "Dinheiro");
  dado.addRows(colunas);

  const opcoes = {
    backgroundColor: "transparent",
    colors: ["green"],
    hAxis: { title: "Data" },
    vAxis: { title: "Dinheiro (R$)" },
  };

  const grafico = new google.visualization.SteppedAreaChart(document.getElementById(id));
  grafico.draw(dado, opcoes);
}

function add_grafico_pizza(colunas, id) {
  const dado = new google.visualization.DataTable();
  dado.addColumn("string", "Dinheiro");
  dado.addColumn("number", "R$");
  dado.addRows(colunas);

  const opcoes = {
    width: 550,
    backgroundColor: "transparent",
    colors: ["#356cb4", "#142945"],
  };

  const grafico = new google.visualization.PieChart(document.getElementById(id));
  grafico.draw(dado, opcoes);
}

function verificarGrafico(qtd, classe, i) {
  console.log(qtd);
  if (!qtd) {
    const card = document.getElementsByClassName(classe)[i];
    const msg = document.createElement("span");
    msg.textContent = "Sem Dados";
    card.appendChild(msg);
  }
}

verificarGrafico(parsearJSON("grafico_pizza_professor-disciplina").qtdTotal, "card-grafico", 0);
verificarGrafico(parsearJSON("grafico_pizza_aluno-disciplina").qtdTotal, "card-grafico", 1);
