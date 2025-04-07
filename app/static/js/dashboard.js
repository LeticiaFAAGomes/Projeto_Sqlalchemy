google.charts.load("current", { packages: ["corechart"] });
// google.charts.setOnLoadCallback(add_grafico_creditos);
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
      ["Matriculados", parsearJSON("grafico_pizza_aluno-disciplina").qtdTotal],
      ["Não matriculados", parsearJSON("grafico_pizza_aluno-disciplina").qtdDisc - parsearJSON("grafico_pizza_aluno-disciplina").qtdTotal],
    ],
    "grafico_pizza_aluno-disciplina"
  );
});

function parsearJSON(id) {
  return JSON.parse(document.getElementById(id).getAttribute("data-json"));
}

function add_grafico_area_degrau() {
  const dado = new google.visualization.DataTable();
  dado.addColumn("string", "Element");
  dado.addColumn("number", "Percentage");
  dado.addRows([["Azul", 60]]);

  const opcoes = {
    backgroundColor: "transparent",
    colors: ["green"],
  };

  var chart = new google.visualization.SteppedAreaChart(document.getElementById("creditos"));
  chart.draw(dado, opcoes);
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
