Highcharts.chart('container', {
  chart: {
      type: 'pie'
  },
  title: {
      text: 'Número de Contactos por comuna'
  },
  series: [{
      name: 'Dispositivos',
      data: [],
      showInLegend: true,
      dataLabels: {
          enabled: true,
          format: '{point.name}: {point.y}'
      }
  }]
});

fetch("http://127.0.0.1:5000/get-cont-por-comuna")
  .then((response) => response.json())
  .then((data) => {

    // Get the chart by ID
    const chart = Highcharts.charts.find(
      (chart) => chart && chart.renderTo.id === "container"
    );

    // Update the chart with new data
    chart.update({
      series: [
        {
          data: data,
        },
      ],
    });
  })
  .catch((error) => console.error("Error:", error));