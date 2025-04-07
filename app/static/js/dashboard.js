google.charts.load("current", { packages: ["corechart"] });
google.charts.setOnLoadCallback(add_grafico_creditos);
google.charts.setOnLoadCallback(add_grafico_abc);

function add_grafico_creditos() {
  const dado = new google.visualization.DataTable();
  dado.addColumn("string", "Element");
  dado.addColumn("number", "Percentage");
  dado.addRows([
    ["Azul", 60],
    ["Verde", 40],
    ["Other", 60],
  ]);

  const opcoes = {
    backgroundColor: "transparent",
    colors: ["green"],
  };

  var chart = new google.visualization.SteppedAreaChart(document.getElementById("creditos"));
  chart.draw(dado, opcoes);
}

function add_grafico_abc() {
  const dado = new google.visualization.DataTable();
  dado.addColumn("string", "Element");
  dado.addColumn("number", "Percentage");
  dado.addRows([
    ["Azul", 60],
    ["Verde", 40],
    ["Other", 60],
  ]);

  const opcoes = {
    title: "Créditos",
    titleTextStyle: {
      color: "#fff",
      fontSize: 25,
      textAlign: "center",
    },
    backgroundColor: "transparent",
    colors: ["#356cb4"],
    hAxis: { textStyle: { color: "#fff" } },
    vAxis: { textStyle: { color: "#fff" } },
  };

  var chart = new google.visualization.SteppedAreaChart(document.getElementById("chart_div"));
  chart.draw(dado, opcoes);
}
